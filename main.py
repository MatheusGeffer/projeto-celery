from task import cadastro
import time

# Loop infinito para publicar informações periodicamente
while True:
    result = cadastro.delay()  # Chama a função 'cadastro' como uma tarefa assíncrona
    print("Publicando informação...")  # Exibe uma mensagem indicando que a informação está sendo publicada
    time.sleep(3)  # Aguarda 3 segundos antes de publicar a próxima informação


