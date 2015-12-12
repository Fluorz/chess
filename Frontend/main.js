var isDragging = false;
var oldPos = [-1, -1];

var game = [[0, '.', 1, 1], [0, '.', 1, 2], [0, '.', 1, 3], [0, '.', 1, 4], [0, '.', 1, 5], [0, '.', 1, 6], [0, '.', 1, 7], [0, '.', 1, 8], [0, '.', 2, 1], [0, '.', 2, 2], [0, '.', 2, 3], [0, '.', 2, 4], [0, '.', 2, 5], [0, '.', 2, 6], [0, '.', 2, 7], [0, '.', 2, 8], [0, '.', 3, 1], [0, '.', 3, 2], [0, '.', 3, 3], [0, '.', 3, 4], [0, '.', 3, 5], [0, '.', 3, 6], [0, '.', 3, 7], [0, '.', 3, 8], [0, '.', 4, 1], [0, '.', 4, 2], [0, '.', 4, 3], [0, '.', 4, 4], [0, '.', 4, 5], [0, '.', 4, 6], [0, '.', 4, 7], [0, '.', 4, 8], [0, '.', 5, 1], [0, '.', 5, 2], [0, '.', 5, 3], [0, '.', 5, 4], [0, '.', 5, 5], [0, '.', 5, 6], [0, '.', 5, 7], [0, '.', 5, 8], [0, '.', 6, 1], [0, '.', 6, 2], [0, '.', 6, 3], [0, '.', 6, 4], [0, '.', 6, 5], [0, '.', 6, 6], [0, '.', 6, 7], [0, '.', 6, 8], [0, '.', 7, 1], [0, '.', 7, 2], [0, '.', 7, 3], [0, '.', 7, 4], [0, '.', 7, 5], [0, '.', 7, 6], [0, '.', 7, 7], [0, '.', 7, 8], [0, '.', 8, 1], [0, '.', 8, 2], [0, '.', 8, 3], [0, '.', 8, 4], [0, '.', 8, 5], [0, '.', 8, 6], [0, '.', 8, 7], [0, '.', 8, 8]];

var html = '';
html += ' <div id="chessTable"> <table id="e"> <thead> <tr> <th> </th> <th> 1</th> <th> 2 </th> <th> 3 </th> <th> 4 </th> <th> 5 </th> <th> 6 </th> <th> 7 </th> <th> 8 </th> </tr> </thead> <tbody> ';

for (var y = 1; y < 9; y++) {
    html += '<tr><td class="num">' + y + '</td>';
    for (var x = 0; x < 9; x++) {
        game.forEach(function (e) {
            if (e[3] == y && e[2] == x) {
                html += '<td onclick="processClick(' + x + ', ' + y + ');"><img src="assets/roi32x32noir.png"></td>';
            }
        })
    }
    html += '</tr>';
}

html += '</tbody></table></div>';
$('#b').append(html);

function processClick(x, y) {
    var piece = 0;
    if (isDragging == false) {
        game.forEach(function (e) {
            if (e[2] == x && e[3] == y) {
                piece = e;
            }
        });
        console.log(piece);
        isDragging = true;
        oldPos = [piece[2], piece[3]];
    }
    else{
        sendMove(oldPos[0], oldPos[1], x, y);
    }
}

function sendMove(oldX, oldY, x, y){
    console.log('oldx ' + oldX + ' oldy ' + oldY + ' x ' + x + ' y ' + y);
    // SEND XHR REQUEST
    isDragging = false;
}