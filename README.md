<h1 align="center">Gerador de QR Code para WiFi 🤳🏽📶🀫 🐍</h1>




<p align="center">
    Esse projeto consiste em um gerador de QR Code para redes WiFi. Com ele, você pode criar um código QR que pode ser facilmente escaneado para que seus amigos e familiares possam se conectar à sua rede sem precisar digitar a senha.
</p>

---

## 📖 Sobre o projeto

Este projeto consiste em um gerador de QR Code para conexão Wi-Fi. Com ele, é possível gerar um código QR que contém as informações necessárias para conectar a um determinado ponto de acesso Wi-Fi.

O projeto foi desenvolvido utilizando a linguagem de programação Python e a biblioteca qrcode. Além disso, foram utilizados os seguintes recursos:

Input do usuário para inserção das informações de rede Wi-Fi;
Manipulação de strings para gerar o conteúdo do QR Code;
Renderização do código QR com a biblioteca Pillow;
Exportação do código QR para um arquivo de imagem PNG.
O objetivo do projeto é facilitar o processo de conexão à redes Wi-Fi, tornando-o mais rápido e prático. Além disso, ele pode ser utilizado para compartilhar informações de rede com outras pessoas de forma simples e segura.


## 🛠️ Tecnologias utilizadas

- Python
- Visual Studio Code

## 📖 Como usar


Para executar o projeto, é necessário ter Python instalado em sua máquina.

Para instalar as bibliotecas necessárias, abra o terminal e execute o seguinte comando:

<pre class="command">
`pip install flask`
</pre>


Para executar o servidor Flask, execute o seguinte comando:

<pre class="command">
`python app.py`
</pre>

Instale também a biblioteca fontawesome-free para carregar o botao de mostrar a senha:

<pre class="command">
`pip install fontawesome-free`
</pre>



### 🚀 Iniciando o servidor

Para iniciar o servidor, abra o Prompt de Comando (Windows) ou o Terminal (Mac/Linux) na pasta raiz do projeto e execute o seguinte comando:
<pre class="command">
`flask run`
</pre>

Se tudo ocorrer corretamente, você verá a seguinte mensagem:
<pre class="command">
`Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
</pre>

Isso significa que o servidor foi iniciado com sucesso e você pode acessá-lo através do endereço `http://127.0.0.1:5000/` em seu navegador.


Acesse a página em seu navegador através do seguinte endereço:

http://127.0.0.1:5000/


## 🛠️ Como funciona

Ao acessar a página, preencha o nome e a senha da sua rede WiFi e clique no botão "Gerar QR Code". O servidor Flask irá processar os dados inseridos, gerar o código QR e exibir a imagem em sua página.




## 🙋 Como contribuir

1. Clone o repositório
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona uma nova feature'`)
4. Push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request


Feito com ❤️ e desenvolvido no Visual Studio Code.

