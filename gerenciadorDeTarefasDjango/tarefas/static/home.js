document.addEventListener('DOMContentLoaded', function() {
    const btnAdd = document.querySelector('.btnAdd');
    const modal = document.getElementById('addTaskModal');
    const closeModal = document.querySelector('.closeModal');

    btnAdd.addEventListener('click', function() {
        modal.style.display = 'block';
    });

    closeModal.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});