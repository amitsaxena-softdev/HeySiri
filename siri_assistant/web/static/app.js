const chat = document.getElementById('chat');
const form = document.getElementById('chat-form');
const input = document.getElementById('query');

function appendMessage(type, text) {
  const msg = document.createElement('div');
  msg.className = `msg ${type}`;
  msg.textContent = text;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const query = input.value.trim();
  if (!query) return;

  appendMessage('user', query);
  input.value = '';

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });

    if (!response.ok) {
      appendMessage('bot', 'Request failed.');
      return;
    }

    const data = await response.json();
    appendMessage('bot', data.text || 'No response');

    if (data.action === 'open_url' && data.url) {
      window.open(data.url, '_blank', 'noopener,noreferrer');
    }
  } catch (error) {
    appendMessage('bot', 'Unable to contact server.');
  }
});
