// info img to player converter
function doFirst(){

    var btn = document.getElementById('playButton');
    var img = document.getElementById('img');

    var showVideoDiv = document.getElementById('showVideoDiv');
    var myMovie = document.getElementById('myMovie');

    var centerside = document.getElementById("centerside");

    btn.addEventListener('click', playVideo, false);
}

function playVideo(){
    img.style.display = 'none';
    btn.style.display = 'none';
    showVideoDiv.style.display = 'block';
    trailer.play();
    centerside.style.paddingTop="0px";
}
window.addEventListener('load',doFirst,false);