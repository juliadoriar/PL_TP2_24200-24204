from lexer import lexer
from parser_1 import parser
from interpreter import interpret
import sys
import os

def main():
    # Verifica se foi fornecido o nome do arquivo como argumento
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do arquivo de entrada como argumento.")
        return
    
    input_filename = sys.argv[1]
    output_folder = "Output"
    output_filename = os.path.join(output_folder, os.path.basename(input_filename))

    try:
        # Abre o arquivo de entrada
        with open(input_filename, 'r') as input_file:
            # Lê o conteúdo do arquivo
            data = input_file.read()
        
        # Cria o diretório de saída se ele não existir
        os.makedirs(output_folder, exist_ok=True)

        # Abre o arquivo de saída para escrever
        with open(output_filename, 'w') as output_file:
            # Redireciona a saída padrão para o arquivo de saída
            sys.stdout = output_file

            # Imprime o conteúdo do arquivo de entrada
            print("Conteúdo do arquivo de entrada:")
            print(data)

            # Envia o código fonte para o lexer
            lexer.input(data)

            # Imprime os tokens gerados pelo lexer
            print("\nTokens gerados:")
            for token in lexer:
                print(token)

            # Chama o parser para construir a árvore sintática
            ast = parser.parse(data, lexer=lexer)

            # Imprime os nós da árvore sintática
            print("\nNós da árvore sintática:")
            print(ast)

            # Interpreta o AST
            result = interpret(ast)

            # Escreve o resultado no arquivo de saída
            output_file.write("\nResultado da última operação: " + str(result))

    except FileNotFoundError:
        print(f"Arquivo '{input_filename}' não encontrado.")

    finally:
        # Restaura a saída padrão
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
