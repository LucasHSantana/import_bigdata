# Import Big Data

## Projeto
O projeto tem como finalidade demonstrar a utilização e criação de containers docker utilizando docker-compose para inserir grande quantidade de dados num banco de dados postgreSQL.

## Tecnologias utilizadas
- [Python 3.8](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [pgAdmin](https://www.pgadmin.org/)

## Instalação
### Docker
Seguir as instruções da documentação de acordo com o sistema operacional utilizado. (Recomendado instalar o docker desktop para facilitar a utilização)
* https://docs.docker.com/engine/install/

> **Note**
> No caso de instalação no windows, pode ser necessário configurar o wsl. Se este for o caso, siga as instruções da documentação: https://docs.docker.com/desktop/windows/wsl/ 

## Utilização
### **Docker**
É necessário que a engine do docker esteja em execução, execute o docker desktop caso necessário.

### **Execução do projeto**
Abra o terminal na pasta raíz do projeto e digite:
>  `docker-compose up`

### **Verificar inserção dos dados no banco de dados**
Abra o navegador e digite:
> `localhost:16543`

### **Login**
- Usuário: `postgres@gmail.com`
- Senha: `postgres`

### **Criar novo server**
1. **Aba Geral**
    - Name: Insira qualquer nome que desejar
2. **Aba Connection**
    - Host: `postgis`
    - Port: `5432`
    - Maintenance Database: `postgres`
    - Username: `postgres`
    - Password: `postgres`

- Salvar o server
- Conectar no banco de dados _sfbike_
- Consultar a tabela _status_

---

- *** Conteúdo destinado ao estudo do Python e utilização do docker
- *** Created By: **Lucas Henrique Santana**
- *** LinkedIn: https://www.linkedin.com/in/lucas-hsantana/
