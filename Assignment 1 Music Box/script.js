
var html_template = "<html><body><script>"

function play_notes(){
    song = document.getElementById("textBox").value;
    console.log(song);
    lines = song.split(/\r?\n/);
    console.log(lines);
    sound_delay = 0;
    compiled_script = "";
    
    for(i = 0; i < lines.length; ++i)
    {
        console.log(lines[i]);
        sound_delay = (1000 * i);
        if(lines[i][0] == 'E')
        {
            console.log("Play E")
            setTimeout(function() {
                new Audio('sounds/E.wav').play();
            }, sound_delay);
        }
        if(lines[i][1] == 'A')
        {
            console.log("Play A")
            setTimeout(function() {
                new Audio('sounds/A.wav').play();
            }, sound_delay);
        }
        if(lines[i][2] == 'D')
        {
            console.log("Play D")
            setTimeout(function() {
                new Audio('sounds/D.wav').play();
            }, sound_delay);
        }
        if(lines[i][3] == 'G')
        {
            console.log("Play G")
            setTimeout(function() {
                new Audio('sounds/G.wav').play();
            }, sound_delay);
        }
        if(lines[i][4] == 'F')
        {
            console.log("Play F")
            setTimeout(function() {
                new Audio('sounds/F.wav').play();
            }, sound_delay);
        }
        if(lines[i][5] == 'C')
        {
            console.log("Play C")
            setTimeout(function() {
                new Audio('sounds/C.wav').play();
            }, sound_delay);
        }
    }

    document.getElementById("compiled")
}

function clear_music(){
    document.getElementById("textBox").value = "";
}