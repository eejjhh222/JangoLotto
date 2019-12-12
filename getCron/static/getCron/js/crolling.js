$(document).ready(function(){





});

var flag = false;
var timeEvent = false;
var flag_idx = 0;

function start(){
    flag = true;
    crolling();
}

function stop(){
    flag = true;
    clearTimeout(timeEvent);
    console.log('end');
}

function crolling(){
    var url = '/test';
    var url = '/lotto/numberApi';
    var data = {
        'round' : (flag_idx+1)
    }
    var dataType = 'json';
    var async = false;
    var json_data = JSON.stringify(data);
    console.log(json_data);

    $.ajax({
            type: 'post',
            data: json_data,
            url: url,
            dataType: dataType,
            contentType : 'application/json',
            async: async,
            beforeSend: function () {
                if (typeof beforeCallback === "function") {
                    return beforeCallback();
                } else {
                    return true;
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            },
            success: function (res) {
                flag_idx++;
                $('#numberListTbl').append('<tr>'
                +'<td>'+res['round']+'</td>'
                +'<td>'+res['prize1']+'</td>'
                +'<td>'+res['prize2']+'</td>'
                +'<td>'+res['prize3']+'</td>'
                +'<td>'+res['prize4']+'</td>'
                +'<td>'+res['prize5']+'</td>'
                +'<td>'+res['prize6']+'</td>'
                +'<td>'+res['bonus']+'</td>'
                +'</tr>'
               );

                /*var ttt = new Vue({
                    el : '#numberListDiv',
                    delimiters: ['[[', ']]'],
                    data: {
                        todos: [
                          { round: res['round'] },
                          { prize1: res['prize1'] },
                          { prize2: res['prize2'] },
                          { prize3: res['prize3'] },
                          { prize4: res['prize4'] },
                          { prize5: res['prize5'] },
                          { prize6: res['prize6'] },
                          { bonus: res['bonus'] },
                        ]
                      }
                });*/

//                if(false){
                if(flag){
                    timeEvent = setTimeout(function() {
                      crolling();
                      }, 1000);

                }

                if (typeof successCallback === "function") {
                    successCallback(data);
                }
            },
            complete: function () {

            }
        });
}