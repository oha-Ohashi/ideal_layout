

var n_steps = 50;
function fing_move(fing, dist_xy, durat){
    console.log(ps[fing]);
    for(let i = 0; i < n_steps; i++){
        setTimeout(function(){
            var new_xy = [
                ps[fing][0] + dist_xy[0]*smooth(i/n_steps),
                ps[fing][1] + dist_xy[1]*smooth(i/n_steps)
            ];
            set_fing(
                $(".kb_fing").eq(fing),
                new_xy
            ) ;
            //console.log(i + " " + home_ps);
        }, (durat / n_steps) *  i);
    }
    setTimeout(function(){
        set_fing(
            $(".kb_fing").eq(fing),
            [ ps[fing][0] + dist_xy[0],
              ps[fing][1] + dist_xy[1] ]
        ) ;
    }, durat + 100);
}
function fing_step(obj, x, y){
    console.log(obj.position.left);
    obj.css(
        {left: x, top: y}
    );
}
function smooth(x){
    if(x < 0.5){
        return 2 * x * x;
    }else{
        return -2 * (-x+1)*(-x+1) + 1;
    }
}