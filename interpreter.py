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
        print(eval_expression(node.expression))

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
    elif isinstance(node, AleatoryNode):
        max_value = eval_expression(node.expression)
        return random.randint(0, max_value)  # Gera um número aleatório entre 0 e o valor máximo

def interpret(ast):
    return eval_program(ast)
