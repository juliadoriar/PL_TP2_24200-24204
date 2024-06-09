# Importa as classes necessárias do módulo `ast_nodes`
from ast_nodes import *
import random

variables = {}  # Dicionário para armazenar variáveis
functions = {}  # Dicionário para armazenar funções

def eval_program(node):
    result = None
    for statement in node.statements:
        result = eval_statement(statement)
    return result

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
    
def interpret_line(line, parser):
    try:
        # Parse the input line
        result = parser.parse(line)
        
        # Evaluate the resulting AST
        eval_program(result)
    except Exception as e:
        print(f"Erro ao processar a entrada: {e}")   

def eval_expression(node):
    if isinstance(node, BinaryOperationNode):
        left = eval_expression(node.left)
        right = eval_expression(node.right)
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
    elif isinstance(node, ConcatNode):
        left = eval_expression(node.left)
        right = eval_expression(node.right)
        return str(left) + str(right)
    elif isinstance(node, UnaryOperationNode):
        operand = eval_expression(node.operand)
        if node.operator == '+':
            return operand
        elif node.operator == '-':
            return -operand
    elif isinstance(node, IdentifierNode):
        return variables.get(node.name, 0)
    elif isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, StringNode):
        return node.value
    elif isinstance(node, AleatoryNode):
        max_value = eval_expression(node.expression)
        return random.randint(0, max_value)  # Gera um número aleatório entre 0 e o valor máximo
    elif isinstance(node, EntradaNode):
        return int(input("Digite um número: "))
    elif isinstance(node, FunctionCallNode):
        return eval_function_call(node)
    else:
        raise ValueError(f"Interpreter error: Invalid expression node: {node}")


def eval_function_call(node):
    function = functions.get(node.name)
    if not function:
        raise ValueError(f"Função {node.name} não definida")
    
    # Salva o contexto atual das variáveis
    saved_variables = variables.copy()

    # Define os parâmetros da função
    if len(function.parameters) != len(node.arguments):
        raise ValueError(f"Interpreter error: Function '{node.name}' expected {len(function.parameters)} arguments, got {len(node.arguments)}")

    for param, arg in zip(function.parameters, node.arguments):
        variables[param.name] = eval_expression(arg)

    # Avalia o corpo da função
    result = None
    for stmt in function.body:
        result = eval_statement(stmt)

    # Restaura o contexto original das variáveis
    global variables
    variables = saved_variables

    return result
    
def interpret(ast):
    return eval_program(ast)
