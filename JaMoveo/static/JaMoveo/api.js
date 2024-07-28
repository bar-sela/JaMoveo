// DOM elements
const mainContent = document.getElementById('main-content');

// View management
let currentView = 'main';
let selectedSong = null;


// Function to show main view
window.showMainView = function(){
    currentView = 'main';
    selectedSong = null;
    mainContent.innerHTML = `
        <h1>Search any song...</h1>
        <form id="searchForm">
            <label for="song_name">Song Name:</label>
            <input type="text" id="song_name" name="song_name" required>
            <button type="submit" class="search_button">Search</button>
        </form>
        <ul id="songsList"></ul>
    `;

    document.getElementById('searchForm').addEventListener('submit', handleSearch);
}


// Function to handle search
async function handleSearch(e) {
    e.preventDefault();
    const songName = document.getElementById('song_name').value;
    try {
        const response = await fetch(`/search_songs?song_name=${encodeURIComponent(songName)}`);
        const data = await response.json();
        console.log(data)
        console.log(typeof data);
        displaySearchResults(data['matching_songs']);
    } catch (error) {
        console.error('Error searching songs:', error);
    }
}

// Function to display search results
function displaySearchResults(results) {
    currentView = 'results';

    mainContent.innerHTML = '<h2 class="results-header">Search Results</h2>';
    const ul = document.createElement('ul');
    ul.className = 'results-list';

  results.forEach(song => {
    const li = document.createElement('li');
    li.className = 'song-item';


   const img = document.createElement('img');
   img.className = 'song-image';
   img.src = `data:image/jpeg;base64,${song.photo}`;
   li.appendChild(img);

   const textNode = document.createElement('span');
   textNode.className = 'song-text';
   textNode.textContent = `${song.name} - ${song.singer}`;
   li.appendChild(textNode);
   li.onclick = () => selectSong(song)
        ul.appendChild(li);
    });

    mainContent.appendChild(ul);
}
// Function to handle song selection
function selectSong(song) {
    selectedSong = song;
    currentView = 'live';
    window.socket.send(JSON.stringify({ Song: song }));
}


// Function to handle quitting a song
window.handleQuit = function() {
   window.socket.send(JSON.stringify({ message: '<h1 class="song-title">Waiting for next song...</h1>' }));
   showMainView();

}


// Initial setup
document.addEventListener('DOMContentLoaded', showMainView);

