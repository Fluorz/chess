var isDragging = false;
var oldPos = [-1, -1];
var playerTurn = -1;
var url = -1;
var id = -1;
var ready = false;

var processClick = function(x, y){
    if(ready === true){
        if(isDragging === false){
            oldPos = [x, y];
            isDragging = true;
        }
        else{
            sendMove(oldPos[0], oldPos[1], x, y);
        }   
    }
    else{
        alert('The game isn\'t ready. Please wait for another player to join.');
    }
};

// Proud of this one
var getIndexFromPosition = function(x, y){
    if(y == 1){
        return x - 1;
    }
    else{
        return ((((y - 1) * 8) + x) - 1);
    }
};

var sendMove = function(oldX, oldY, x, y){
    var array = {'oldX': oldX, 'oldY': oldY, 'x': x, 'y': y, 'id': id};
    console.log(array);
    $.post('http://localhost:8000/move/' + url + '/' + id, {'move': JSON.stringify(array)}, function(data){
        console.log(data);
    });
    isDragging = false;
};

$(function(){
    
    var game = {};
    
    /*
    ONLY FUNCTIONS THAT MATTER
    */
    
    var createAndJoinGame = function(){
        create(function(){
            join(function(){
                console.log('id : ' + id + ' url : ' + url);     
                getGameState(function(data){
                     refresh(data, function(){
                         setInterval(function(){
                             getGameState(function(temp){
                                 refresh(temp); 
                             });
                         }, 10000);
                     });
                });
            });
        });
    };
    
    var joinExistingGame = function(uniqueurl){
        url = uniqueurl;
        join(function(){
            console.log('id : ' + id + ' url : ' + url);    
            getGameState(function(data){
                refresh(data, function(){
                    setInterval(function(){
                        getGameState(function(temp){
                            refresh(temp)
                        });
                    }, 10000);
                });
            });
        });
    };
    
    $('#join').click(function(){
        joinExistingGame($('#idInput').val());
    });
    
    $('#create').click(function(){
        createAndJoinGame();
    });
    
    
    /*
    THESE FUNCTIONS ARE 'PRIVATE', AND SHOULDNT BE CALLED
    */
    
    var create = function(cb){
        $.ajax('http://localhost:8000/createnewgame').done(function(data){
            if(data != 'False'){
                var parsed = JSON.parse(data);
                url = parsed.uniqueurl;
                cb();
            }
            else{
                console.log('wtf');
            }
        });
    };
    
    var join = function(cb){
        $.ajax('http://localhost:8000/joingame/' + url).done(function(data){
            if(data != 'False'){
                var parsed = JSON.parse(data);
                id = parsed.id;
                cb();
            }
            else{
                console.log('wtf2');
            }
        });
    };
    
    var render = function(){
        var html = '';
        html += ' <div id="chessTable"> <table id="e"> <thead> <tr> <th> </th> <th> 1</th> <th> 2 </th> <th> 3 </th> <th> 4 </th> <th> 5 </th> <th> 6 </th> <th> 7 </th> <th> 8 </th> </tr> </thead> <tbody> ';
        
        var x = 1;
        var y = 1;
        for(var i = 0; i < game.board.length; i++){
            if(x > 8){
                html += '</tr>';
                x = 1;
                y++;
            }
            if (x == 1){
                html += '<tr><td class="num">' + y + '</td>';
            }
            //html += '<td onclick="processClick(' + x + ', ' + y + ');"><img src="assets/roi32x32noir.png"></td>';
            var index = getIndexFromPosition(y, x);
            if(game.board[index] != 'E'){
                html += '<td onclick="processClick(' + x + ', ' + y + ');">' + game.board[index] + '</td>'; // (y, x) et pas (x, y). Pourquoi? Je ne sais pas. Mais ça march
            }
            else{
                html += '<td onclick="processClick(' + x + ', ' + y + ');"></td>';
            }
            x++;
        }
        html += '</tbody></table></div>';
        $('#b').append(html);
    };
    
    var getGameState = function(cb){
        console.log('getting game state');
        $.ajax('http://localhost:8000/gameupdate/' + url).done(function(data){
            cb(JSON.parse(data));
        });
    };
    
    var flushHtml = function(){
        $("#b").empty();
    };
    
    var refresh = function(newB, cb) { // cb is optional, not using it in the main setInterval
        if(newB.board != game.board){
            game = newB;
            flushHtml();
            render();
            if(cb !== undefined){ // Only calling the cb if it is needed
                cb();
            }
        }
        else {
            console.log('same');
            if(cb !== undefined){ // Same 
                cb();    
            }
        }
        ready = game.ready;
    };
    
    var stopRefreshing = function(){
        clearInterval(refreshInterval);
    };
});






