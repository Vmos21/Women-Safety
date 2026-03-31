const sessionId = "session_" + Math.random().toString(36).substr(2, 9);

const severityIcons = {
  LOW: "🟢",
  MODERATE: "🟡",
  HIGH: "🟠",
  CRITICAL: "🔴"
};

function appendMessage(role, text, severity = null) {
  const container = document.getElementById("chat-container");

  const wrapper = document.createElement("div");
  wrapper.className = `message ${role}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  wrapper.appendChild(bubble);

  if (severity && role === "bot") {
    const badge = document.createElement("div");
    badge.className = `severity-badge ${severity.level}`;
    badge.textContent = `${severityIcons[severity.level] || "⚪"} ${severity.level} SEVERITY`;
    wrapper.appendChild(badge);

    if (severity.reason) {
      const reason = document.createElement("div");
      reason.className = "severity-reason";
      reason.textContent = severity.reason;
      wrapper.appendChild(reason);
    }
  }

  container.appendChild(wrapper);
  container.scrollTop = container.scrollHeight;
}

function showTyping() {
  const container = document.getElementById("chat-container");
  const typing = document.createElement("div");
  typing.className = "message bot";
  typing.id = "typing-indicator";
  typing.innerHTML = `<div class="typing"><span></span><span></span><span></span></div>`;
  container.appendChild(typing);
  container.scrollTop = container.scrollHeight;
}

function removeTyping() {
  const el = document.getElementById("typing-indicator");
  if (el) el.remove();
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const btn = document.getElementById("send-btn");
  const text = input.value.trim();
  if (!text) return;

  appendMessage("user", text);
  input.value = "";
  btn.disabled = true;
  showTyping();

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, session_id: sessionId })
    });

    const data = await res.json();
    removeTyping();
    appendMessage("bot", data.reply, data.severity);
  } catch (err) {
    removeTyping();
    appendMessage("bot", "Sorry, something went wrong. Please try again.");
  } finally {
    btn.disabled = false;
    input.focus();
  }
}

document.getElementById("user-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});
