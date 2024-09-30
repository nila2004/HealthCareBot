// static/chat.js
document.getElementById('sendMessage').addEventListener('click', () => {
    let message = document.getElementById('message').value;

    if (!message) return;  // Prevent empty messages from being sent

    // Send message to the server
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({message: message})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();  // Attempt to parse response as JSON
    })
    .then(chatHistory => {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML = ''; // Clear the chat box

        // Display chat messages
        chatHistory.forEach(entry => {
            const messageElement = document.createElement('div');
            messageElement.classList.add(entry.sender === 'user' ? 'user-message' : 'bot-message');
            messageElement.textContent = `${entry.sender}: ${entry.message}`;
            chatBox.appendChild(messageElement);
        });

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;

        // Clear the input field
        document.getElementById('message').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
