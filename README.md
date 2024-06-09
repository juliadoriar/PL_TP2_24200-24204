# PL_TP2_24200-24204
Este repositório é utilizado para armazenar o desenvolvimento do segundo trabalho prático da disciplina Processamento de Linguagens.


## Descrição do Projeto

Este projeto implementa um interpretador para uma linguagem de programação simples, incluindo um analisador léxico, um analisador sintático (parser) e um interpretador. A linguagem possui recursos básicos, como atribuição de variáveis, expressões aritméticas, instruções de escrita e manipulação de strings.

## Componentes do Projeto

### Lexer (Analisador Léxico)

O lexer é responsável por analisar o texto de entrada e dividir o código fonte em "tokens". Tokens são os elementos como palavras-chave, identificadores, números e símbolos especiais. Ele também remove espaços em branco e comentários.

### Parser (Analisador Sintático)

O parser é responsável por criar uma árvore sintática a partir dos tokens produzidos pelo lexer. Ele define as regras gramaticais da linguagem e usa essas regras para construir a estrutura hierárquica do código fonte.

### AST Node

O AST Node define os nós da árvore sintática abstrata (AST) usada para representar a estrutura do código fonte. Cada nó representa uma parte do código, como uma expressão, uma declaração de variável ou uma instrução de escrita.

### Interpreter (Interpretador)

O interpretador recebe a árvore sintática criada pelo parser e a utiliza para executar as instruções do programa. Ele avalia as expressões aritméticas, atribui valores às variáveis, manipula strings e realiza outras operações definidas pela linguagem.

## Como Executar o Projeto

O projeto pode ser executado em dois modos:

- **Modo Arquivo:** Execute o script `main.py` fornecendo um arquivo de entrada como argumento.


Claro, aqui está um exemplo de como o README.md pode ser estruturado com informações sobre os componentes do projeto, incluindo o AST Node e a função principal (main):

markdown
Copy code
# Trabalho de Processamento de Linguagens (PL)

## Descrição do Projeto

Este projeto implementa um interpretador para uma linguagem de programação simples, incluindo um analisador léxico, um analisador sintático (parser) e um interpretador. A linguagem possui recursos básicos, como atribuição de variáveis, expressões aritméticas, instruções de escrita e manipulação de strings.

## Componentes do Projeto

### Lexer (Analisador Léxico)

O lexer é responsável por analisar o texto de entrada e dividir o código fonte em "tokens". Tokens são os elementos como palavras-chave, identificadores, números e símbolos especiais. Ele também remove espaços em branco e comentários.

### Parser (Analisador Sintático)

O parser é responsável por criar uma árvore sintática a partir dos tokens produzidos pelo lexer. Ele define as regras gramaticais da linguagem e usa essas regras para construir a estrutura hierárquica do código fonte.

### AST Node

O AST Node define os nós da árvore sintática abstrata (AST) usada para representar a estrutura do código fonte. Cada nó representa uma parte do código, como uma expressão, uma declaração de variável ou uma instrução de escrita.

### Interpreter (Interpretador)

O interpretador recebe a árvore sintática criada pelo parser e a utiliza para executar as instruções do programa. Ele avalia as expressões aritméticas, atribui valores às variáveis, manipula strings e realiza outras operações definidas pela linguagem.

## Como Executar o Projeto

O projeto pode ser executado em dois modos:

- **Modo Arquivo:** Execute o script `main.py` fornecendo um arquivo de entrada como argumento.

EX: python main.py arquivo_de_entrada.txt

- **Modo Interativo:** Execute o script `main.py` sem argumentos para iniciar o modo interativo.

EX: python main.py