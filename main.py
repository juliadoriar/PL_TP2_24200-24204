from lexer import lexer
from parser_1 import parser
from interpreter import interpret, interpret_line
import sys # Importa o módulo sys para acessar os argumentos da linha de comando
import os # Importa o módulo os para manipulação de arquivos e pastas

def main():
    if len(sys.argv) > 1:  # Se um arquivo de entrada foi fornecido como argumento
        input_filename = sys.argv[1]
        output_folder = "Output"
        output_filename = os.path.join(output_folder, os.path.basename(input_filename) + ".txt")

        try:
            # Abre o arquivo de entrada
            with open(input_filename, 'r') as input_file:
                # Lê o conteúdo do arquivo
                data = input_file.read()
            
            # Envia o código fonte para o lexer
            lexer.input(data)

            # Obter os tokens gerados pelo lexer
            tokens = []
            for token in lexer:
                tokens.append(token)

            # Chama o parser para construir a árvore sintática
            ast = parser.parse(data, lexer=lexer)

            # Interpreta o AST
            result = interpret(ast)

            # Cria o diretório de saída se ele não existir
            os.makedirs(output_folder, exist_ok=True)

            # Abre o arquivo de saída para escrever
            with open(output_filename, 'w') as output_file:
                # Escreve os tokens no arquivo de saída
                output_file.write("Tokens gerados:\n")
                for token in tokens:
                    output_file.write(str(token) + "\n")

                # Escreve os nós da árvore sintática no arquivo de saída
                output_file.write("\nNós da árvore sintática:\n")
                output_file.write(str(ast) + "\n")

                # Escreve o resultado da interpretação no arquivo de saída
                output_file.write("\nResultado da última operação:\n")
                output_file.write(str(result))

            print(f"Resultado da última operação foi salvo em '{output_filename}'.")
        ## Trata exceções
        # FileNotFoundError é lançado quando o arquivo de entrada não é encontrado    
        except FileNotFoundError:
            print(f"Arquivo '{input_filename}' não encontrado.")
        # Exception é lançada para outros erros
        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
    else:  # Modo interativo
        print("Modo Interativo. Digite suas instruções:")
        while True:
            try:
                line = input('>>> ') # Lê a entrada do usuário
                if line.lower() in ['exit', 'quit']: # Se o usuário digitar 'exit' ou 'quit', sai do modo interativo
                    break
                interpret_line(line, parser) # Interpreta a linha de entrada usando o parser definido anteriormente
            except Exception as e: # Trata exceções
                print(f"Erro ao processar a entrada: {e}")

if __name__ == "__main__":
    main()
