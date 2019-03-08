# djangoapi-reactfrontend
api com django restframework e frontend com react e utilizando o docker para levantar a aplicação.


Está é uma simples aplicação de cadastro de pedido de itens, feita com uma api django rest framework no backend
e com react trabalhando no frontend. A aplicação não está completa, a parte do frontend tem pouquissimas coisas feitas 
mas eu pretendo fazer mais e melhora-la (vocÊs também podem, bom que aprendo mais também)

Bom,
Para rodar está aṕlicação instale as seguintes ferramentas:

<strong>Docker</strong> <br>
<strong>Docker-compose</strong> <br>
<strong>Git</strong> <br>

Após instalado essas ferramentas, de um git clone neste projeto e rode os seguintes comandos no terminal:

<strong>docker-compose build</strong> <br>
<strong>docker-compose run api python3 manage.py migrate</strong> <br>
<strong>docker-compose run frontend npm install packge.json</strong><br>

Agora que já configurou o ambiente você pode subir a aplicação com o seguinte comando:

<strong>docker-compose up</strong> <br>
ou com <br>
<strong>docker-compose up -d </strong> (desta forma a aba do seu terminal fica livre para rodar outros comandos ) <br>

Toda vez que você precisar instalar ou rodar algum comando do backend ou do frontend, rode com o seguinte comando:

exemplo de como criar uma app no django:
<strong> docker-compose run api python3 django-admin startapp [nome de sua app]</strong><br>
<br>
execplo de como instalar um pacote pra o frontend
<strong> docker-compose run frontend npm install [o pacote] </strong> <br>

É isto galera, uma busca de aprendizado prático para minha programação em django com aplicaçes rest full com restframework. E aprender um framework de frontend que é o react.

Como sempre sintam-se livres para modificar, melhorar e me ensinar como melhorar minha programação ou também para tirar dúvidas sobre como fiz algo. 
