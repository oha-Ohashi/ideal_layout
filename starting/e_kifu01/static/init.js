var n_col = 10;
var n_row = 3;
var one_u = 70;
var kb_width = one_u * n_col;
var kb_height = one_u * n_row;
const keys_ps = [
    [0,1],[1,1],[2,1],[3,1],
    [6,1],[7,1],[8,1],[9,1]
];
const ps  = [            
    [0,1],[1,1],[2,1],[3,1],
    [6,1],[7,1],[8,1],[9,1]
];

$(document).ready(function(){
    $(".kb_area").width(kb_width +"px");
    $(".kb_area").height(kb_height +"px");

    for(var i=0; i<n_row; i++){
        var elm = $("<div>", {
            class: "kb_row"
        });
        elm.appendTo(".kb_area");
    }
    $(".kb_row").each(function(){
        for(var i=0; i<n_col; i++){
            var key = $("<div>",{
                class: "kb_key"
            });
            $("<div>", {
                class: "kb_cap"
            }).appendTo($(key))
            key.appendTo($(this));
        }
    });
  
    $(".kb_key").width(one_u +"px");
    $(".kb_key").height(one_u +"px");

    set_fing( $(".kb_fing").eq(0) , [9,2]);

    
    $(".kb_fing").each(function(i){
        set_fing( $(this) , keys_ps[i]);
    });
    

});

function set_fing(obj, xy){
    xy[0] = ((xy[0]+1) * one_u) - (obj.width()/2 + one_u/2);
    xy[1] = ((xy[1]+1) * one_u) - (obj.height()/2 + one_u/2);
    obj.css(
        {left: xy[0], top: xy[1]}
    );
}
function fing_set(obj, xy){
    xy[0] = ((xy[0]+1) ) - (obj.width()/2 + one_u/2);
    xy[1] = ((xy[1]+1) ) - (obj.height()/2 + one_u/2);
    obj.css(
        {left: xy[0], top: xy[1]}
    );
}