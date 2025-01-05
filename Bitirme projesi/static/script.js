function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Kullanıcı mesajını ekrana ekle
    let chatBox = document.getElementById("chat-box");
    let userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // Mesajı sunucuya gönder
    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Chatbot yanıtını ekrana ekle
        let botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = data.response;
        chatBox.appendChild(botMessage);
        
        // Otomatik kaydırma
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    // Girdi kutusunu temizle
    document.getElementById("user-input").value = "";
}
