document.addEventListener('DOMContentLoaded', function(){

    const messagesContainer = document.querySelector('#massage_container');
    const messageInput = document.querySelector('[name=message_input]');
    const messageSend = document.querySelector('[name=message_send]');
    const personeName = document.querySelector('[name=persone_name]');
    
    
    let websocketClient = new WebSocket("ws://localhost:12345");
    websocketClient.onopen = () => {
        console.log("Client connected!");
        // websocketClient.send("Hello!");
        messageSend.onclick = () => {
            jsonData = JSON.stringify({'name': personeName.value,'message': messageInput.value});
            console.log(jsonData)
            websocketClient.send(jsonData);
            messageInput.value = ''
        };
    };
    websocketClient.onmessage = (message) => {
        const newMessage = document.createElement('div');
        newMessage.innerHTML = message.data;
        messagesContainer.appendChild(newMessage);
    };
    
}, false);