
# Desafio IGS

Olá, Meu nome é João Teixeira de Loiola Netto e o intuito deste repositório é apresentar minha resolução ao desafio solicitado.

**Uma pequena nota**: Por motivos pessoais eu iniciei a criação do projeto já tarde da noite, porém fiz tudo que foi solicitado. No desenvolvimento do projeto eu estive pensando em incluir testes unitários e até um deployer com Docker porém por se tratar de uma aplicação simples não vi utilidade para realizar tais operações.

O que foi realizado:
   * Prrenchimento automático de dados no banco (Fixtures)
   * Documentação Swagger (Não me aprofundei muito na documentação por conta de ser uma aplicação simples e não havia muito tempo)
   * Facilidade de criação das operações de CRUD com DjangoRest

Espero que gostem da aplicação e obrigado pela oportunidade :)

# Iniciando o projeto 
Considerando que já foi realiado o clone do repositório e já estamos dentro do diretório do mesmo, vamos seguir os seguintes passo...
	
# 1 - Carregar Bibliotecas

**Nota**: Aconselho a criação de uma virtualenv para garantir que as bibliotecas instaladas neste projeto não gerem conflitos com as bibliotecas instaladas na máquina que rodará o mesmo.

Baixe as bibliotecas para executar esse projeto usando o comando (pode demorar um pouco):
> $ pip install -r requirements.txt

# 2 - Entrar no diretório do projeto (website)
> $ cd website
	
# 3 - Criar banco de dados

> $ py manage.py makemigrations core

> $ py manage.py migrate


# 4 - Cadastrar dados ao banco (Fixtures)

> $ py manage.py loaddata fixtures/departament.json --app core.Departament
 
> $ py manage.py loaddata fixtures/collaborator.json --app core.Collaborator


# 5 - Rodar aplicação
> $ py manage.py runserver

