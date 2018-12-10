function resizeIframe(frame) {
    frame.style.height = frame.contentWindow.document.body.scrollHeight + 'px';
    frame.style.width = '100%';
    frame.style.visibility = "visible";

    const body = frame.contentWindow.document.querySelector('body');
    body.style.color = 'white';
}