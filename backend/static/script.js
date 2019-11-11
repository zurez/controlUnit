var socket = io("http://127.0.0.1:5000");
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
    
});
console.log("Pinging for GetImage")
socket.emit("getImage",{})
console.log("Pinging for GetImage Done")
function sendCommand(actionType,params){
    // console.log(actionType);
    
    socket.emit('command',{
        actionType,
        params:"ff"
    });
}

function receiveUpdate(updateString){
    console.log(updateString);
    
}

function onRecieveUSBCamFeed( data ){
    console.log(data);
    
}
socket.on("update",receiveUpdate);
socket.on("usbCamera", onRecieveUSBCamFeed)