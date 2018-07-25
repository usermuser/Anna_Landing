
var LOW = 0 
var HIGH = 1

function set_status(data){
    $.ajax({url: "/gpio/set_status",
            method: "get",
            dataType: "text",
            data: data });
    return true;
}



function get_status(port){
    $.ajax({url:"/gpio/get_status",
            method: 'get',
            dataType: "text",
            data: port,
            success: function(data){
                var parsed_data = JSON.parse(data);
                var html_id_port_status = $("#" + port.port + "_status");
                html_id_port_status.text(parsed_data.state);

            }});
    return true;
}

//var buttonLow = $("#set_pd" + number + "_low");
//console.log(buttonLow.click(function(){set_status({'status':'LOW'},
 // 'id': buttonLow.data('id')); }));

//var buttonHigh = $("#set_pd" + number + "_high");
//console.log(buttonHigh.click(function(){set_status({'status':'HIGH'}); }));
var buttonLow = $("#set_pd14_low")
$("#set_pd14_low").click(function(){set_status({'status': LOW, 'port_name': buttonLow.data('port')}); });

$("#set_pd14_high").click(function(){set_status({'status': HIGH, 'port_name': buttonLow.data('port')}); });

// $("#gpio_button111").click(function(){get_status({'port': 'PD14'});});

setInterval("get_status({'port': 'pd14'})",500);
// setInterval("get_status({'port': 'pd15'})",500);