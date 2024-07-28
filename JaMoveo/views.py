import base64
import json
import os

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from JaMoveo.filles.signUpForms import RegualUserCreationForm
from core.settings import DB_FILE


def signup(request):
    if request.method =='GET':
        form = RegualUserCreationForm()
        return render(request=request, template_name = 'signup.html', context= {'form': form})

    elif request.method == 'POST':
        form = RegualUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        return render(request=request, template_name = 'signup.html', context= {'form': form})

@login_required
def mainPage(request):
    if request.user.is_admin:  # Checks if the user is an admin
        return render(request, 'admin_page.html')
    else:
        return render(request, 'user_main_page.html')


@login_required
def retrieve_songs(request):
    substring = request.GET.get('song_name', '').lower()
    matching_songs = []

    # Ensure the directory exists
    if not os.path.exists(DB_FILE):
        return JsonResponse({'error': 'Database directory not found'}, status=404)

    for filename in os.listdir(DB_FILE):
            file_path = os.path.join(DB_FILE, filename)
            with open(file_path, 'r') as f:
                try:
                    song_data = json.load(f)
                    if substring in song_data['name'].lower():
                        photo_path = song_data.get('photo')
                        photo_data = None
                        if photo_path and os.path.exists(photo_path):
                            with open(photo_path, 'rb') as img_file:
                                photo_data = base64.b64encode(img_file.read()).decode('utf-8')

                        matching_songs.append({
                            'name': song_data['name'],
                            'singer': song_data['singer'],
                            'photo': photo_data,
                            'content' :song_data['content']
                        })
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")
                except KeyError as e:
                    print(f"Missing key in JSON file {filename}: {str(e)}")

    return JsonResponse({'matching_songs': matching_songs})

