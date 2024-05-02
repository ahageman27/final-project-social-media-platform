document.addEventListener("DOMContentLoaded", function() {
    const socket = io.connect("http://localhost:5000");

    const chatHistory = document.getElementById("chat-history");
    const messageForm = document.getElementById("message-form");
    const messageInput = document.getElementById("message-input");

    messageForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const message = messageInput.value.trim();
        if (message !== "") {
            sendMessage(message);
            messageInput.value = "";
        }
    });

    function sendMessage(message) {
        const chatMessage = document.createElement("div");
        chatMessage.classList.add("chat-message");
        chatMessage.textContent = message;
        chatHistory.appendChild(chatMessage);

        // Send message to server
        socket.emit("chat_message", message);
    }

    socket.on("chat_message", function(message) {
        const chatMessage = document.createElement("div");
        chatMessage.classList.add("chat-message");
        chatMessage.textContent = message;
        chatHistory.appendChild(chatMessage);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    });
});
