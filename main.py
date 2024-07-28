def remove_chords_key(song_data):
    for section in song_data:
        for item in section:
            if 'chords' in item:
                del item['chords']
    print(song_data)

# Example song data
song_data = [
    [
        {"lyrics": "Hey"},
        {"lyrics": "Jude", "chords": "F"},
        {"lyrics": "don't"},
        {"lyrics": "make"},
        {"lyrics": "it"},
        {"lyrics": "bad", "chords": "C"}
    ],
    [
        {"lyrics": "Take"},
        {"lyrics": "a"},
        {"lyrics": "sad", "chords": "C7"},
        {"lyrics": "song", "chords": "C4/7"},
        {"lyrics": "and"},
        {"lyrics": "make"},
        {"lyrics": "it"},
        {"lyrics": "better", "chords": "F"}
    ],
    [
        {"lyrics": "Remember", "chords": "Bb"},
        {"lyrics": "to"},
        {"lyrics": "let"},
        {"lyrics": "her"},
        {"lyrics": "into"},
        {"lyrics": "your"},
        {"lyrics": "heart", "chords": "F"}
    ],
    [
        {"lyrics": "Then"},
        {"lyrics": "you"},
        {"lyrics": "can"},
        {"lyrics": "start", "chords": "C"},
        {"lyrics": "to"},
        {"lyrics": "make", "chords": "C7"},
        {"lyrics": "it"},
        {"lyrics": "better", "chords": "F"}
    ]
]

# Remove 'chords' keys in place
remove_chords_key(song_data)

# Print the modified song data
for section in song_data:
    print(section)
