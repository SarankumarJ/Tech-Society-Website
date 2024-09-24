// Typing effect for the welcome text
document.addEventListener('DOMContentLoaded', () => {
    const typedText = document.getElementById('typing-effect');
    const text = 'Welcome to the Tech Society';
    let index = 0;

    function type() {
        if (index < text.length) {
            typedText.textContent += text.charAt(index);
            index++;
            setTimeout(type, 100);
        }
    }
    type();
});

document.addEventListener("DOMContentLoaded", function() {
    const bubbleContainer = document.querySelector('.bubbles');

    for (let i = 0; i < 15; i++) {
        const bubble = document.createElement('div');
        bubble.classList.add('bubble');
        
        const size = Math.random() * 60 + 20;
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;
        bubble.style.left = `${Math.random() * 100}vw`;
        bubble.style.animationDuration = `${Math.random() * 5 + 5}s`;

        bubbleContainer.appendChild(bubble);
    }
});
