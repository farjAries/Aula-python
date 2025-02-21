import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Adivinhação")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Fonte
FONTE = pygame.font.Font(None, 36)

# Função para mostrar texto na tela
def mostrar_texto(texto, x, y, cor=PRETO):
    superficie_texto = FONTE.render(texto, True, cor)
    TELA.blit(superficie_texto, (x, y))

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 5)
    tentativas = 0
    acertou = False
    palpite = ""
    mensagem = "Estou pensando em um número entre 1 e 100. Tente adivinhar!"

    rodando = True
    while rodando:
        TELA.fill(BRANCO)  # Limpa a tela com a cor branca

        # Mostra a mensagem e o número de tentativas
        mostrar_texto(mensagem, 50, 50)
        mostrar_texto(f"Tentativas: {tentativas}", 50, 100)
        mostrar_texto(f"Seu palpite: {palpite}", 50, 150)

        # Atualiza a tela
        pygame.display.flip()

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Quando o jogador pressiona Enter
                    try:
                        palpite_int = int(palpite)
                        tentativas += 1

                        if palpite_int < numero_secreto:
                            mensagem = "Muito baixo! Tente novamente."
                        elif palpite_int > numero_secreto:
                            mensagem = "Muito alto! Tente novamente."
                        else:
                            acertou = True
                            mensagem = f"Parabéns! Você acertou em {tentativas} tentativas!"
                    except ValueError:
                        mensagem = "Por favor, digite um número válido."
                    palpite = ""  # Limpa o palpite após o Enter
                elif evento.key == pygame.K_BACKSPACE:  # Permite apagar o palpite
                    palpite = palpite[:-1]
                else:
                    palpite += evento.unicode  # Adiciona o caractere digitado ao palpite

        if acertou:
            mostrar_texto(mensagem, 50, 200, VERDE)
            pygame.display.flip()
            pygame.time.wait(3000)  # Espera 3 segundos antes de fechar
            rodando = False

    pygame.quit()

if __name__ == "__main__":
    jogo_adivinhacao()