from faker import Faker
from criar_cpf import gerador_cpf
from config.config_celery import app

# Define a função cadastro como uma tarefa assíncrona do Celery
@app.task
def cadastro():
    # Cria uma instância do Faker configurada para gerar dados em português brasileiro
    fake = Faker(locale='pt_BR')
    # Gera um nome aleatório
    nome = fake.name()
    # Gera uma idade aleatória entre 1 e 99 anos
    idade = fake.random_int(min=1, max=99)
    # Verifica se a idade gerada é menor que 18 anos
    if idade < 18:
        # Se a idade for menor que 18, lança uma exceção com uma mensagem de erro
        mensagem_erro = f"A idade de {nome} é menor que 18 anos. Cadastro não aprovado!"
        raise ValueError(mensagem_erro)
    # Gera um endereço de email aleatório
    email = fake.email()
    # Gera um endereço aleatório
    endereco = fake.address()
    # Gera um CPF válido utilizando a função gerador_cpf
    cpf = gerador_cpf()

    # Cria um dicionário com os dados gerados
    p1 = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "endereco": endereco,
        "cpf": cpf
    }

    # Retorna o dicionário com os dados gerados
    return p1