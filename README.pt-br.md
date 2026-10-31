# Forca Dev (Python)

[Read in English](README.md)

Jogo da forca que roda no terminal, com palavras do mundo da programação (python, debug, framework e outras).

## Como funciona

- O jogo sorteia uma palavra e mostra um `_` para cada letra escondida.
- Você digita uma letra por vez e tem 6 tentativas.
- Cada letra errada custa uma tentativa. Letras repetidas e entradas inválidas (números, mais de uma letra) são ignoradas.
- Você vence ao descobrir a palavra inteira e perde quando as tentativas acabam.

## Como executar

É preciso ter o Python 3 instalado.

```
python forca.py
```

Você também pode colar o código no [Google Colab](https://colab.research.google.com) e executar por lá.

## Conceitos praticados

Variáveis, listas, laços (`while` e `for`), condicionais, entrada do usuário, validação de entrada, formatação de texto e o módulo `random`.

## Observações

- Este é um projeto de estudo. Os textos do jogo e a lista de palavras estão em português, e as palavras não têm acento.
- Possíveis melhorias: desenho da forca em ASCII, níveis de dificuldade e uma versão usando classes.
