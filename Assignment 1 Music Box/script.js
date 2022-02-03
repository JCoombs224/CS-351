
var html_template = "<html><body><script>"

function play_notes(){
    song = document.getElementById("textBox").value;
    console.log(song);
    lines = song.split("\r?\n");
    sound_delay = 0;
    compiled_script = "";
    
    for(i = 0; i < lines.length; ++i)
    {
        console.log(lines[i]);
    }

    document.getElementById("compiled")
}