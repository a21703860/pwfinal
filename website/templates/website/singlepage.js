function showSection(section) {
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => document.querySelector('#content').innerHTML = text);
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            showSection(this.dataset.section);
        };
    });
});