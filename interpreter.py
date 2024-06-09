# Importa as classes necessárias do módulo `ast_nodes`
from ast_nodes import *
import random

variables = {}  # Dicionário para armazenar variáveis

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
    
def interpret_line(line, parser):
    try:
        # Parse the input line
        result = parser.parse(line)
        
        # Evaluate the resulting AST
        eval_statement(result)
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


def interpret(ast):
    return eval_program(ast)
