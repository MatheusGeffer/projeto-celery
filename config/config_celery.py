from celery import Celery

""" Cria uma instância da aplicação Celery com o nome 'task',
configurando o broker para comunicação usando o protocolo AMQP do RabbitMQ
e o backend para armazenamento usando MongoDB """
app = Celery('task', broker="amqp://localhost" , backend="mongodb://root:example@localhost:27017/celery")