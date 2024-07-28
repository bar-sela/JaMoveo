
const socket = new WebSocket(`wss://${window.location.host}/ws`);
window.socket = socket;


     socket.onmessage = function(event) {
        const data = JSON.parse(event.data);

        if (data.message) {
            if (isAdmin === false){
                const contentElement = document.getElementById('main-content');
                contentElement.innerHTML = data.message;
            }
        }
        else{

            messageHandler(data)
            }
    };




function messageHandler(data) {
    const contentElement = document.getElementById('main-content');
    console.log(data)
    // Clear previous content
    contentElement.innerHTML = '';

    // Create and append song title
    const songTitleElement = document.createElement('h1');
    songTitleElement.classList.add('song-title');
    songTitleElement.innerHTML = `Now Playing: ${data.Song.name} by ${data.Song.singer}`;
    contentElement.appendChild(songTitleElement);

    // Create and append song details
    const songDetailsElement = document.createElement('div');
    songDetailsElement.id = 'song-details';


data.Song.content.forEach(section => {
    const sectionElement = document.createElement('div');
    sectionElement.classList.add('section');

    const chordsRow = document.createElement('div');
    chordsRow.classList.add('chords-row');

    const lyricsRow = document.createElement('div');
    lyricsRow.classList.add('lyrics-row');

    section.forEach(item => {
        const chordElement = document.createElement('div');
        chordElement.textContent = item.chords || '';
        chordElement.classList.add('chord');

        const lyricsElement = document.createElement('div');
        lyricsElement.textContent = item.lyrics;
        lyricsElement.classList.add('lyrics');

        chordsRow.appendChild(chordElement);
        lyricsRow.appendChild(lyricsElement);
    });

    sectionElement.appendChild(chordsRow);
    sectionElement.appendChild(lyricsRow);

    songDetailsElement.appendChild(sectionElement);
});

contentElement.appendChild(songDetailsElement);

addQuitButton(contentElement)
toggleScrolling(contentElement)





   function addQuitButton(contentElement) {
    // Create and append Quit button if isAdmin is true
    if (isAdmin) {
        const quitButton = document.createElement('button');
        quitButton.classList.add('button');
        quitButton.textContent = 'Quit';
        quitButton.onclick = function() {
            // Handle the quit button click event
            window.handleQuit();
            // You can add more actions here, such as closing the WebSocket connection or navigating to another page
        };
        contentElement.appendChild(quitButton);
    }
}

function toggleScrolling(contentElement) {
    const toggleScrollButton = document.createElement('button');
    toggleScrollButton.textContent = 'Start Scrolling';
    toggleScrollButton.classList.add('button');

    contentElement.appendChild(toggleScrollButton);

    let isScrolling = false;
    let scrollInterval;

    toggleScrollButton.addEventListener('click', () => {
        if (isScrolling) {
            clearInterval(scrollInterval);
            toggleScrollButton.textContent = 'Start Scrolling';
        } else {
            scrollInterval = setInterval(() => {
                window.scrollBy(0, 1);
            }, 50);
            toggleScrollButton.textContent = 'Stop Scrolling';
        }
        isScrolling = !isScrolling;
    });
    }
}