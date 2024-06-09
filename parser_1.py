import ply.yacc as yacc
from lexer import tokens
from ast_nodes import *

# Definição da gramática usando regras de produção
# Cada função p_XXX() corresponde a uma regra de produção


# Definição da gramática usando regras de produção
def p_program(p):
    'program : statement_list'
    p[0] = ProgramNode(p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_assign(p):
    'statement : IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULA'
    p[0] = AssignmentNode(IdentifierNode(p[1]), p[3])

def p_statement_write(p):
    'statement : ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULA'
    p[0] = WriteNode(p[3])

def p_expression(p):
    '''
    expression : IDENTIFICADOR
               | NUMERO
               | STRING
               | INTERPOLATED_STRING
               | expression OPERADOR_ARITMETICO expression
               | expression CONCATENACAO expression
               | PARENTESES_ESQ expression PARENTESES_DIR
               | ENTRADA PARENTESES_ESQ PARENTESES_DIR
               | ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR
    '''
    if len(p) == 2: 
        if isinstance(p[1], str) and p.slice[1].type == 'IDENTIFICADOR':
            p[0] = IdentifierNode(p[1])
        elif isinstance(p[1], int):
            p[0] = NumberNode(p[1])
        elif p.slice[1].type == 'STRING':
            p[0] = StringNode(p[1])
        elif p.slice[1].type == 'INTERPOLATED_STRING':
            p[0] = parse_interpolated_string(p[1])
    elif len(p) == 4:
        if p[1] == '(' and p[3] == ')':
            p[0] = p[2]
        elif p.slice[2].type == 'OPERADOR_ARITMETICO':
            p[0] = BinaryOperationNode(p[2], p[1], p[3])
        elif p.slice[2].type == 'CONCATENACAO':
            p[0] = ConcatNode(p[1], p[3])
    elif len(p) == 5 and p.slice[1].type == 'ALEATORIO':
        p[0] = AleatorioNode(p[3])
    elif len(p) == 5 and p.slice[1].type == 'ENTRADA':
        p[0] = EntradaNode()
        
        
# def p_expression_interpolated_string(p):
#     'expression : INTERPOLATED_STRING'
#     p[0] = parse_interpolated_string(p[1])
    
def parse_interpolated_string(s):
    parts = []
    while '#{' in s:
        before, after = s.split('#{', 1)
        var, after = after.split('}', 1)
        if before:
            parts.append(StringNode(before))
        parts.append(IdentifierNode(var.strip()))
        s = after
    if s:
        parts.append(StringNode(s))
    result = parts[0]
    for part in parts[1:]:
        result = ConcatNode(result, part)
    return result

# def p_term(p):
#     '''term : term OPERADOR_ARITMETICO factor
#             | factor'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = BinaryOperationNode(p[2], p[1], p[3])

# def p_factor(p):
#     '''factor : PARENTESES_ESQ expression PARENTESES_DIR
#               | NUMERO
#               | IDENTIFICADOR'''
#     if len(p) == 2:
#         if isinstance(p[1], str):
#             p[0] = IdentifierNode(p[1])
#         else:
#             p[0] = NumberNode(p[1])
#     else:
#         p[0] = p[2]

def p_error(p):
    if p:
        print(f"Erro de sintaxe! Unexpected token: {p}")
    else:
        print("Erro de sintaxe! EOF inesperado") # EOF = End of File

parser = yacc.yacc()
