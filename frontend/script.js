document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
  
    // Configure Showdown for better Markdown support
    const converter = new showdown.Converter({
      simpleLineBreaks: true,
      ghCompatibleHeaderId: true,
      tables: true,
      strikethrough: true,
      tasklists: true
    });
  
    // Send button click event
    sendButton.addEventListener('click', () => {
      const message = userInput.value.trim();
      if (!message) return;
      appendMessage('user', message);
      userInput.value = '';
      sendToAPI(message);
    });
  
    // Allow "Enter" to send message
    userInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendButton.click();
      }
    });
  
    // Append a new message to the chat
    function appendMessage(sender, content) {
      const messageWrapper = document.createElement('div');
      messageWrapper.classList.add('message', sender);
  
      const messageContent = document.createElement('div');
      messageContent.classList.add('message-content');
  
      if (sender === 'bot') {
        // Convert Markdown to HTML
        const html = converter.makeHtml(content);
        messageContent.innerHTML = html;
      } else {
        // User message as plain text
        messageContent.textContent = content;
      }
  
      messageWrapper.appendChild(messageContent);
      chatMessages.appendChild(messageWrapper);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  
    // Show loading spinner
    function showLoadingSpinner() {
      const loadingDiv = document.createElement('div');
      loadingDiv.classList.add('loading', 'bot');
      loadingDiv.innerHTML = `<div class="spinner"></div>`;
      chatMessages.appendChild(loadingDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      return loadingDiv;
    }
  
    // Remove loading spinner
    function removeLoadingSpinner(spinnerDiv) {
      if (spinnerDiv && spinnerDiv.parentNode) {
        spinnerDiv.parentNode.removeChild(spinnerDiv);
      }
    }
  
    // Send message to your real API endpoint
    async function sendToAPI(message) {
      const spinnerDiv = showLoadingSpinner();
  
      try {
        // Example: Adjust endpoint, headers, and body as needed
        const response = await fetch('http://127.0.0.1:8000/api/core/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            user_id: 'myUserId',
            message: message
          })
        });
  
        removeLoadingSpinner(spinnerDiv);
  
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        // Assuming your API returns something like { "veris_response": "Markdown text" }
        if (data.veris_response) {
          appendMessage('bot', data.veris_response);
        } else {
          appendMessage('bot', 'Sorry, I did not understand that.');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        removeLoadingSpinner(spinnerDiv);
        appendMessage('bot', 'An error occurred. Please try again later.');
      }
    }
  
    // Initial greeting from Veris
    appendMessage('bot', 'Hello! I\'m **Veris**. How can I help you today?');
  });
  