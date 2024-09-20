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
