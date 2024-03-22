document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('taskModal');
    const closeModal = document.querySelector('.closeModal');
    const submitButton = document.getElementById('submitButton');
    const modalTitle = document.getElementById('modalTitle');
    const taskForm = document.getElementById('taskForm');

    // Função para abrir o modal e configurar para cadastro
    function openModalForCadastro() {
        modalTitle.innerText = 'Adicionar Nova Tarefa';
        taskForm.action =  '/adicionarTarefa';
        submitButton.innerText = 'Adicionar';
        modal.style.display = 'block';
    }

    // Função para abrir o modal e configurar para edição
    window.openModalForEdicao =  function openModalForEdicao(taskId, descricao, prioridade, dataVencimento) {
        modalTitle.innerText = 'Editar Tarefa';
        taskForm.action = "/editarTarefa/" + taskId;
        submitButton.innerText = 'Salvar Alterações';
        document.getElementById('descricao').value = descricao;
        document.getElementById('prioridade').value = prioridade;
        const data = new Date(dataVencimento);
        const dataInput = document.getElementById('dataVencimento');
        dataInput.value = data.toISOString().slice(0, 10);
        document.getElementById('task_id').value = taskId;
        modal.style.display = 'block';
    }
    window.openModalParaExcluir = function openModalParaExcluir(id) {
        console.log('perguntar se vai apagar a tarefa', id)
        document.getElementById('modalConfirmacao').style.display = 'block';
    }

    closeModal.addEventListener('click', function () {
        modal.style.display = 'none';
        
    });
    
    document.getElementById('fecharConfirmacao').addEventListener('click', function(){
        document.getElementById('modalConfirmacao').style.display = 'none'
    })
    console.log('teste', closeModal)

    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

    // Abre o modal para adicionar nova tarefa
    document.querySelector('.btnAdd').addEventListener('click', openModalForCadastro);



  
});