

var n_steps = 50;
function fing_move(fing, dist_xy, durat){
    //console.log("original:" +ps[fing] + "dist: " + dist_xy);
    if(ps[fing][0] == dist_xy[0] && ps[fing][1] == dist_xy[1] ){
        fing_press(fing, durat);
        console.log("criri");
    }else{
        for(let i = 0; i < n_steps; i++){
            setTimeout(function(){
                var new_xy = [
                    ps[fing][0] + (dist_xy[0] - ps[fing][0])*smooth(i/n_steps),
                    ps[fing][1] + (dist_xy[1] - ps[fing][1])*smooth(i/n_steps)
                ];
                set_fing(
                    $(".kb_fing").eq(fing),
                    new_xy
                ) ;
                //console.log(i + " " + home_ps);
            }, (durat / n_steps) *  i);
        }
        setTimeout(function(){
            ps[fing] = dist_xy;
        }, durat );
    }
}

function smooth(x){
    if(x < 0.5){
        return 2 * x * x;
    }else{
        return -2 * (-x+1)*(-x+1) + 1;
    }
}

function fing_press(fing, durat){
    $(".kb_fing").eq(fing).css("background-color", "crimson");
    setTimeout(() => {
        $(".kb_fing").eq(fing).css("background-color", "transparent");
    }, durat);
}