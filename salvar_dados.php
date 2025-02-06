<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = $_POST['nome'];
    $email = $_POST['email'];

    // Salvar os dados no arquivo data.txt
    $dados = "Nome: $nome, Email: $email\n";
    file_put_contents('data.txt', $dados, FILE_APPEND); // 'FILE_APPEND' adiciona ao final do arquivo

    // Responder ao cliente
    echo "Dados salvos com sucesso!";
}
?>
