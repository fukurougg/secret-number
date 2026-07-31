# 🎯 Secret Number

Um jogo simples de adivinhação desenvolvido em **Python** durante os estudos no **SENAI**, com o objetivo de praticar conceitos fundamentais da linguagem, como funções, estruturas de repetição, tratamento de exceções e geração de números aleatórios.

---

## 📖 Sobre o projeto

O **Secret Number** é um jogo em que o computador sorteia um número secreto e o jogador deve descobri-lo utilizando o menor número possível de tentativas.

A cada erro, o programa informa se o número secreto é **maior** ou **menor** que o valor informado, ajudando o jogador a chegar à resposta correta.

---

## 🎮 Como funciona

1. O programa gera um número aleatório entre **1 e 10**.
2. O jogador informa um número.
3. Se errar:

   * o jogo informa se o número secreto é maior ou menor;
   * o jogador pode tentar novamente.
4. Se acertar:

   * o jogo exibe uma mensagem de sucesso;
   * mostra a quantidade de tentativas realizadas.
5. O jogador pode escolher jogar novamente ou encerrar o programa.

---

## 🧠 Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados diversos conceitos básicos de Python, como:

* Funções (`def`)
* Estruturas de repetição (`while`)
* Estruturas condicionais (`if`, `else`)
* Tratamento de exceções (`try` / `except`)
* Entrada de dados (`input`)
* Conversão de tipos
* Geração de números aleatórios
* Organização do código em funções
* Ponto de entrada com `main()`

---

## 📂 Estrutura do código

```text
Secret Number
│
├── ask()
│   └── Recebe e valida a entrada do usuário.
│
├── random_number_function()
│   └── Gera um número aleatório entre 1 e 10.
│
├── try_try()
│   └── Controla toda a lógica da partida.
│
├── main()
│   └── Gerencia a execução do programa e permite jogar novamente.
│
└── __main__
    └── Inicia o jogo.
```

---

## ▶️ Como executar

### Pré-requisitos

* Python 3 instalado.

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/secret-number.git
```

### Entre na pasta

```bash
cd secret-number
```

### Execute

```bash
python main.py
```

---

## 💻 Exemplo de execução

```text
Coloque um valor: 5

Errou! Tente novamente.

O número secreto é maior que 5 - tentativas: 2

Coloque um valor: 8

Parabéns! Você acertou!
Número de tentativas: 2
SECRET NUMBER = 8
```

---

## 🚀 Possíveis melhorias

Este projeto foi desenvolvido para fins de aprendizado. Algumas melhorias que podem ser implementadas futuramente:

* Corrigir o sistema de números já sorteados (`all_secret`).
* Permitir escolher a dificuldade.
* Definir diferentes intervalos de números.
* Criar um sistema de pontuação.
* Adicionar níveis de dificuldade.
* Implementar limite de tentativas.
* Exibir histórico das partidas.
* Criar uma interface gráfica utilizando Tkinter ou PyQt.
* Melhorar a validação das entradas do usuário.

---

## 📚 Objetivo educacional

Este projeto foi desenvolvido durante os estudos de **Python no SENAI**, com foco na prática da lógica de programação e dos principais recursos da linguagem.

---

## 👨‍💻 Autor

FUKUROUGG

---

⭐ Caso este projeto seja útil para seus estudos, fique à vontade para utilizá-lo como referência e adaptá-lo para praticar novos conceitos da linguagem.
