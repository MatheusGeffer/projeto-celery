# Projeto de Cadastro com Geração de dados fictícios 
Este é um projeto simples de cadastro de usuários que gera informações fictícias usando a biblioteca Faker, incluindo nomes, idades, e-mails e endereços. Além de uma função de geração de números validados de cpf's imaginários, O projeto também utiliza a biblioteca Celery para processamento assíncrono de tarefas e geração de CPFs válidos.

O Celery é responsável por executar a tarefa de geração de cadastros de usuários em segundo plano, permitindo que o processo principal continue sua execução sem esperar pela conclusão da tarefa.

O RabbitMQ atua como um sistema de mensagens (broker) que implementa o protocolo de mensagens avançado (AMQP). Ele desempenha um papel crucial no projeto, servindo como o broker do Celery. O RabbitMQ recebe, armazena e roteia as tarefas enviadas pelo Celery para os seus respectivos consumidores (workers) que irão executá-las.

Além disso, o projeto utiliza o MongoDB como o backend do Celery para armazenar resultados das tarefas, como por exemplo, os cadastros de usuários gerados. O MongoDB é um banco de dados NoSQL orientado a documentos que oferece uma solução flexível e escalável para armazenamento de dados.

## Funcionalidades
- O script gerar_cpf.py contém uma função para gerar CPFs válidos.
- O script task.py contém uma tarefa do Celery chamada cadastro, que gera informações de cadastro de usuários fictícios.
- O script main.py inicia um loop infinito para executar a tarefa cadastro a cada cinco minutos.
- Cada vez que a tarefa é executada, um nome aleatório, idade, e-mail, endereço e CPF são gerados usando a biblioteca Faker e a função de geração de CPF do gerar_cpf.py.
- Se a idade do usuário gerado for menor que 18 anos, uma exceção será lançada, indicando que o cadastro não foi aprovado.

## Configurações do Ambiente de Desenvolvimento
Para configurar o ambiente de desenvolvimento local, você precisará dos seguintes pré-requisitos:
- Docker instalado em seu sistema.
- Um editor de código, como por exemplo: VS Code, PyCharm.
- A linguagem de programação Python (versão: 3.11.1)
  
Este projeto requer um ambiente Docker contendo os seguintes serviços:
- RabbitMQ: Utilizado como broker para o Celery.
- MongoDB: Utilizado como backend para o Celery.

Para iniciar os serviços Docker necessários, você pode utilizar os seguintes comandos:
Pelo terminal de sua preferência navegar até o diretório do projeto, utilizar o comando 'docker-compose-mongo up' e esperar sua execução, em seguida o comando 'docker-compose-rabbitmq up' e novamente esperar sua execução. Obs: Comandos apenas para Sistema Operacional Windows, se estiver usando outro sistema diferente, favor procurar a devida execução dos comandos.

## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:
- gerar_cpf.py: Contém uma função para gerar CPFs válidos.
- task.py: Define uma tarefa do Celery chamada cadastro que gera informações de cadastro de usuários.
- main.py: Inicia um loop infinito para executar a tarefa cadastro periodicamente.
- config_celery.py: Configuração do Celery.
- requirements.txt: Arquivo contendo as dependências do projeto.
- docker-compose-mongo.yml: Arquivo de configuração para o Docker Compose, definindo o serviço MongoDB.
- docker-compose-rabbitmq.yml: Arquivo de configuração para o Docker Compose, definindo o serviço RabbitMQ.

## Como executar o Projeto
- Certifique-se de ter Docker instalado em seu sistema.
- Clone o repositório: git clone 'https://github.com/MatheusGeffer/projeto_celery.git'
- Inicie os serviços Docker.
- Instale as dependências do projeto executando pip install -r requirements.txt.
- Inicie o Celery com o comando celery -A config_celery worker --loglevel=info.
- Execute o script principal com python main.py.

## Referências e Documentações utilizadas
- Documentação Celery - https://docs.celeryq.dev/en/stable/index.html
- Estudo de funcionamento do Celery - https://www.youtube.com/watch?v=ig9hbt-yKkM&t=2234s
- Estdudo básico python + Celery, RabbitMQ - https://www.youtube.com/watch?v=G6dIr3tGpG8
- Estudo de funcionamento do MongoDB - https://www.youtube.com/watch?v=gOTMudRsf6A&t=6195s

OBS: Projeto inspirado em um trabalho da faculdade, da disciplina de Software para Sistemas e Infraestrutura, com o apoio do instrutor e orientador Profº Valdinei - (https://www.linkedin.com/in/valdineisaugo/)







