$(document).ready(function(){
    var data_all;
    $.getJSON("myexperiment/abc.json", function(data){
        console.log(data);
        data_all = data;
    });
    

    setTimeout(function(){

        console.log(data_all);
        $("#title_h2").text("layout: "+ data_all.layout);
        $("#textp").text("text: "+ data_all.text);
        disp_30_legends(data_all.keys);
        data_all.history.forEach(e => {
            //console.log(e.xy);
            set_fing_move(e);
        }); 
        ////YEEEEHAAAAAAAAHAHAHAHHHHHHHH
        //fing_move(3, [9,0], 2000);
        fing_press(2, 500);
        //fing_move(5, [0,-1], 1000);
        //fing_move(6, [0,-1], 1500);
        //fing_move(7, [0,-1], 2000);
    }, 500);
});

function set_fing_move(arg){
    setTimeout(function(){
        console.log(arg);
        fing_move(arg.finger, arg.xy, arg.duration);
    }, arg.start);
}