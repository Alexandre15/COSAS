// URL da lista do SharePoint
const siteUrl = "https://eaton.sharepoint.com/sites/PROJETOS_LOGISTICA";
const listName = "transportadoras";

// Função para obter itens da lista
function getListItems() {
    const url = `${siteUrl}/_api/web/lists/getbytitle('${listName}')/items`;

    fetch(url, {
        method: 'GET',
        headers: {
            "Accept": "application/json; odata=verbose",
            "Authorization": "Bearer " + "alexandrelfagundes@eaton.com" // Substitua pelo seu token de acesso
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na resposta da rede');
        }
        return response.json();
    })
    .then(data => {
        displayItems(data.d.results);
    })
    .catch(error => {
        console.error('Houve um problema com a requisição Fetch:', error);
    });
}

// Função para exibir itens na lista
function displayItems(items) {
    const itemList = document.getElementById('itemList');
    itemList.innerHTML = '';

    items.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = item.Title; // Substitua 'Title' pelo campo que deseja exibir
        itemList.appendChild(listItem);
    });
}

// Carrega os itens ao iniciar a página
window.onload = getListItems;