var span = 500;
var millis = 0;


setInterval(one_roop , span);

function one_roop(){ 
        //$.getJON("myexperiment/abc.json", function(data){});
        $.ajaxSetup({ async: false });
        $.getJSON("json", function(data){
            console.log(data);
        });
        $.ajaxSetup({ async: true });

        console.log(millis); 
        $("#dispp").text(millis);
        
        
        millis += span;
    } 