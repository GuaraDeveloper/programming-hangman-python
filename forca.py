# Jogo da forca com tema de programação
# Projeto de estudo em Python (roda no terminal)

import random

palavras = [
    "python", "java", "javascript", "html", "css", "github", "linux",
    "windows", "terminal", "node", "mysql", "funcao", "variavel", "loop",
    "for", "while", "if", "else", "bug", "debug", "codigo", "algoritmo",
    "programa", "frontend", "backend", "api", "framework",
]

# sorteia a palavra e prepara o estado do jogo
palavra = random.choice(palavras)
letras_player = []
tentativas = 6

while True:
    # mostra a palavra com as letras já acertadas
    for letra in palavra:
        if letra in letras_player:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"\nVocê tem {tentativas} tentativas")

    tentativa = input("Digite sua letra: ").lower().strip()

    # valida a entrada
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra.")
        continue
    if tentativa in letras_player:
        print("Você já tentou essa letra.")
        continue

    letras_player.append(tentativa)

    # só perde tentativa se a letra não está na palavra
    if tentativa not in palavra:
        tentativas -= 1
        print(f"Você errou! Restam {tentativas} tentativas.")

    # verifica se ganhou ou perdeu
    venceu = all(letra in letras_player for letra in palavra)

    if venceu:
        print(f"Você venceu! Parabéns! A palavra era: {palavra}")
        break
    if tentativas == 0:
        print(f"Você perdeu! Quem sabe na próxima? A palavra era: {palavra}")
        break
