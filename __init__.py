import os


def respostaProcessada(nome, resposta):

    if resposta == '1':
       return print(
            f"{os.linesep}{nome}, Desenvolvimento web, análise de dados, automação, app científicas e muito mais...{os.linesep}")
    elif resposta == '2':
       return print(f'{os.linesep}{nome}  Em geral, leva cerca de dois a seis meses para aprender os fundamentos básicos.{os.linesep}')
    elif resposta == '3':
       return print(f'{os.linesep}{nome} A tua assimilação, foco e desempenho é o que você vão  te transformar e conseguir fazer coisa com a linguagem.{os.linesep}')
    elif resposta == '4':
       return print(f'{os.linesep}{nome} O melhor local para aprender essa maravilha de linguagem é na plataforma da linguagem com sua documentação{os.linesep}')
    else:
      return  print(' O menu só tem 4 opções, [1 - 2- 3- 4], escolha só entre esses')

def chatbot():

    print('Olá')
    name = str(input('Qual é o teu nome?'))
    print('Em que posso ajudar ou o que gostaria de saber {}?'.format(name))
    while True:
        #Menu de opções
        resposta =  input(
            f'Vale apena aprender python? {os.linesep}[1] - O que gostaria de fazer com python? {os.linesep} [2] - Quanto tempo leva para conseguir pegar bem?{os.linesep}[3] - O que vai me mostrar se estou bom ou não?{os.linesep}[4] - Qual plataforma é bom para estudar Python?{os.linesep}')
        #Processar a resposta
        respostaProcessada(name, resposta)

if __name__ == '__main__':
    chatbot()