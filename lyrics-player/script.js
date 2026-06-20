let lyrics = [];

const audioInput = document.getElementById("audioFile");
const audio = document.getElementById("audio");
const loadBtn = document.getElementById("loadBtn");
const lyricDisplay = document.getElementById("lyricDisplay");

audioInput.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        const url = URL.createObjectURL(file);

        audio.src = url;

    }

});

loadBtn.addEventListener("click", ()=>{

    const raw = document
        .getElementById("lyricsInput")
        .value
        .trim();

    lyrics = [];

    const lines = raw.split("\n");

    lines.forEach(line=>{

        const parts = line.split("|");

        if(parts.length===2){

            lyrics.push({
                time:parseFloat(parts[0]),
                text:parts[1]
            });

        }

    });

    alert("Lyrics Loaded!");

});

audio.addEventListener("timeupdate", ()=>{

    const current = audio.currentTime;

    for(let i=0;i<lyrics.length;i++){

        if(
            current >= lyrics[i].time &&
            (
                i===lyrics.length-1 ||
                current < lyrics[i+1].time
            )
        ){

            lyricDisplay.innerHTML =
                lyrics[i].text;

            break;
        }

    }

});
