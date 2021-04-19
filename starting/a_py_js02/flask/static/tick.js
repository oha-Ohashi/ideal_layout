var span = 300;
var millis = 0;
setInterval(
    function(){ 
        $.getJSON("myexperiment/abc.json", function(data){});


        console.log(millis); 
        $("#dispp").text(millis);
        millis += span;
    }     
, span);