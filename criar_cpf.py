import random

# Função que gerar cpf aleatório e validos de acordo com os calculos necessários
# https://www.calculadorafacil.com.br/computacao/validar-cpf -> referência de como calcular um cpf valido
def gerador_cpf():
    # Gera nove dígitos aleatórios para o CPF
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    # Calcula o primeiro dígito verificador do CPF
    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <=9 else 0

    # Adiciona o primeiro dígito verificador ao CPF
    dez_digitos = nove_digitos + str(digito_1)

    # Calcula o segundo dígito verificador do CPF
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Concatena os dígitos para formar o CPF completo
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_gerado_pelo_calculo
