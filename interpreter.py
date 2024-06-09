# Importa as classes necessárias do módulo `ast_nodes`
from ast_nodes import *
import random

variables = {}  # Dicionário para armazenar variáveis
functions = {}  # Dicionário para armazenar funções

# Esta função recebe um nó de programa como entrada e avalia cada instrução 
# contida nesse programa. Ela itera sobre as instruções do programa, chamando 
# a função eval_statement(statement) para avaliar cada uma delas. O resultado 
# da última instrução avaliada é armazenado na variável result, que é retornada ao final da função.
def eval_program(node):
    result = None
    for statement in node.statements:
        result = eval_statement(statement)
    return result

# Esta função recebe um nó de declaração como entrada e avalia o tipo de declaração
# que foi fornecida. Dependendo do tipo de declaração, a função executa a ação apropriada.
# Por exemplo, se a declaração for uma atribuição, a função avalia a expressão à direita
# do operador de atribuição e armazena o valor na variável associada ao identificador.
# Se a declaração for uma instrução de escrita, a função avalia a expressão a ser escrita
# e imprime o resultado na saída padrão.
def eval_statement(node):
    if isinstance(node, AssignmentNode):
        value = eval_expression(node.expression)
        variables[node.identifier.name] = value
        return value  # Retorna o resultado da última operação
    elif isinstance(node, WriteNode):
        result = eval_expression(node.expression)
        print(result)
        return result  # Retorna o resultado da última operação
    elif isinstance(node, FunctionNode):
        functions[node.name] = node
        return None
    elif isinstance(node, FunctionCallNode):
        return eval_function_call(node)
    
# Responsável por interpretar uma única linha de entrada no modo interativo
def interpret_line(line, parser):
    try: 
        # Tenta analisar a linha de entrada fornecida e retorna o resultado como uma árvore sintática abstrata (AST).
        result = parser.parse(line) 
        
        # Se a análise sintática for bem-sucedida, a função eval_program chamada para avaliar o programa representado pela árvore sintática. Esta função executa todas as instruções contidas no programa e retorna o resultado da última instrução avaliada.
        eval_program(result)
    except Exception as e: # Qualquer exceção que ocorrer durante o processo de interpretação é tratada e uma mensagem de erro é exibida
        print(f"Erro ao processar a entrada: {e}")   

# Esta função avalia uma expressão representada por um nó da AST e retorna o valor resultante.
def eval_expression(node):
    # Se o nó atual da AST for uma operação binária
    if isinstance(node, BinaryOperationNode):
        # Avalia recursivamente as expressões à esquerda e à direita da operação
        left = eval_expression(node.left)
        right = eval_expression(node.right)
        # Aplica a operação aos valores obtidos e retorna o resultado
        if node.operator == '+':
            return left + right
        elif node.operator == '-':
            return left - right
        elif node.operator == '*':
            return left * right
        elif node.operator == '/':
            if right != 0:  # Verifica se o divisor não é zero
                return left / right
            else:
                raise ValueError("Interpreter error: Division by zero")
    # Se o nó atual da AST for um nó de concatenação de strings
    elif isinstance(node, ConcatNode):
        # Avalia recursivamente as expressões à esquerda e à direita da concatenação
        left = eval_expression(node.left)
        right = eval_expression(node.right)
        # Concatena as strings resultantes e retorna o resultado
        return str(left) + str(right)
    # Se o nó atual da AST for uma operação unária, que é um operador de sinal positivo ou negativo
    elif isinstance(node, UnaryOperationNode):
        # Avalia recursivamente o operando da operação
        operand = eval_expression(node.operand)
        # Aplica a operação ao operando e retorna o resultado
        if node.operator == '+':
            return operand
        elif node.operator == '-':
            return -operand
    # Se o nó atual da AST for um identificador
    elif isinstance(node, IdentifierNode):
        # Retorna o valor associado ao identificador na tabela de variáveis
        return variables.get(node.name, 0)
    # Se o nó atual da AST for um número
    elif isinstance(node, NumberNode):
        # Retorna o valor do número
        return node.value
    # Se o nó atual da AST for uma string
    elif isinstance(node, StringNode):
        # Retorna o valor da string
        return node.value
    # Se o nó atual da AST for um nó de número aleatório
    elif isinstance(node, AleatoryNode):
        # Avalia recursivamente a expressão associada ao limite superior do intervalo
        max_value = eval_expression(node.expression)
        return random.randint(0, max_value)  # Gera um número aleatório entre 0 e o valor máximo
    elif isinstance(node, EntradaNode):
        # Se o nó atual da AST for um nó de entrada de dados
        return int(input("Digite um número: ")) # Solicita ao usuário que insira um número e retorna o valor inserido
    # Se o nó atual da AST for uma chamada de função
    elif isinstance(node, FunctionCallNode):
        return eval_function_call(node)
    else:
        raise ValueError(f"Interpreter error: Invalid expression node: {node}") # Lança uma exceção se o nó de expressão for inválido


def eval_function_call(node):
    function = functions.get(node.name)
    if not function:
        raise ValueError(f"Função {node.name} não definida")
    
    # Cria um novo escopo para as variáveis locais da função
    local_variables = {}
    
    # Mapeia argumentos para parâmetros
    for param, arg in zip(function.params, node.args):
        local_variables[param.name] = eval_expression(arg)
    
    # Salva o estado atual das variáveis globais
    global_variables_backup = variables.copy()
    
    # Substitui as variáveis globais com as variáveis locais da função
    variables.update(local_variables)
    
    # Executa o corpo da função
    result = None
    for statement in function.body:
        result = eval_statement(statement)
    
    # Restaura as variáveis globais
    variables.clear()
    variables.update(global_variables_backup)
    
    return result

# Função principal que interpreta a AST
# Recebe o nó raiz da árvore sintática como argumento
def interpret(ast):
    return eval_program(ast)
