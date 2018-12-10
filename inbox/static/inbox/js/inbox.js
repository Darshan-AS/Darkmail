window.onload = function () {
    const messages = document.getElementsByClassName('message');
    for (let i = 0; i < messages.length; i++) {
        const message = messages[i];
        message.onclick = function () {
            document.location.href = this.dataset.url;
        }
    }
};