######### ANALISADOR SINTÁTICO #########
# O analisador sintático é responsável por analisar a estrutura do código fonte e construir a 
# árvore sintática do programa.
# O analisador sintático é composto por regras de produção que definem a estrutura da gramática da linguagem.
# Cada regra de produção é implementada como uma função Python que define como os tokens da entrada
# são combinados para formar a estrutura da árvore sintática.
# Cada função p_???() corresponde a uma regra de produção

import ply.yacc as yacc
from lexer import tokens
from ast_nodes import *

# Definição da gramática usando regras de produção
def p_program(p):
    'program : statement_list'
    p[0] = ProgramNode(p[1])


# A função 'p_statement_list' define a regra de produção 'statement_list' que pode ser composta por
# uma lista de 'statement' seguidos por um único 'statement', ou apenas um único 'statement'.

# Se a produção corresponder à primeira regra (statement_list statement), então 'p' terá três elementos:
        # p[0]: statement_list (a lista de declarações até agora, que estamos construindo)
        # p[1]: statement_list (a lista de declarações acumulada)
        # p[2]: statement (a nova declaração que estamos adicionando à lista)
        
# Se a produção corresponder à segunda regra (statement),
        # então 'p' terá apenas dois elementos:
        # p[0]: statement_list (a lista de declarações que estamos construindo)
        # p[1]: statement (a única declaração)
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# A função p_statement_assign especifica que uma declaração (statement) é composta por um identificador, 
# seguido por um operador de atribuição (=), seguido por uma expressão e, finalmente, um ponto e vírgula. 
def p_statement_assign(p):
    'statement : IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULA'
    p[0] = AssignmentNode(IdentifierNode(p[1]), p[3])

# A função p_statement_write especifica que uma declaração (statement) é composta pela palavra-chave 'escrever',
# seguida por um parêntese esquerdo, uma expressão, um parêntese direito e um ponto e vírgula.
# A declaração 'escrever' é usada para imprimir o valor de uma expressão na saída padrão.
def p_statement_write(p):
    'statement : ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULA'
    p[0] = WriteNode(p[3]) # Cria um nó de escrita com a expressão como argumento

# A função p_statement_function especifica que uma declaração (statement) é composta pela palavra-chave 'funcao',
# seguida por um identificador, parêntese esquerdo, uma lista de parâmetros, parêntese direito, dois pontos,
# uma declaração ou uma lista de declarações e a palavra-chave 'fim'.
# A declaração 'funcao' é usada para definir uma nova função no programa.
def p_statement_function(p):
    '''statement : FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement FIM
                 | FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement_list FIM'''
    if len(p) == 9:
        p[0] = FunctionNode(p[2], p[4], [p[7]])
    else:
        p[0] = FunctionNode(p[2], p[4], p[7])
    functions[p[2]] = p[0]

# A função p_param_list define uma regra de produção para listas de parâmetros em declarações de função.
# Uma lista de parâmetros pode ser composta por uma lista de parâmetros seguida por uma vírgula e um identificador,
# ou apenas um identificador.
def p_param_list(p):
    '''param_list : param_list COMMA IDENTIFICADOR
                  | IDENTIFICADOR
                  | empty'''
    if len(p) == 4: # Se houver três elementos na lista de tokens
        p[0] = p[1] + [p[3]] # Adiciona o identificador à lista de parâmetros
    elif len(p) == 2 and p[1] is not None: # Se houver apenas um elemento na lista de tokens e não for um valor vazio
        p[0] = [p[1]] # Cria uma lista com esse elemento
    else: # Se não houver elementos na lista de tokens ou for um valor vazio
        p[0] = [] # Retorna uma lista vazia

# Esta função define uma regra de produção para expressões na gramática
def p_expression(p):
    '''
    expression : IDENTIFICADOR
               | NUMERO
               | STRING
               | INTERPOLATED_STRING
               | expression OPERADOR_ARITMETICO expression
               | expression CONCATENACAO expression
               | PARENTESES_ESQ expression PARENTESES_DIR
               | function_call
               | ENTRADA PARENTESES_ESQ PARENTESES_DIR
               | ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR
    '''
    # Verifica o número de elementos na lista de tokens
    if len(p) == 2: # Se há apenas um token na expressão
        if isinstance(p[1], str) and p.slice[1].type == 'IDENTIFICADOR':
            p[0] = IdentifierNode(p[1]) # Se o token é uma string e é um identificador, cria um nó de identificador
        elif isinstance(p[1], int):
            p[0] = NumberNode(p[1]) # Se o token é um inteiro, cria um nó de número
        elif p.slice[1].type == 'STRING':
            p[0] = StringNode(p[1]) # Se o token é uma string, cria um nó de string
        elif p.slice[1].type == 'INTERPOLATED_STRING':
            p[0] = parse_interpolated_string(p[1]) # Se o token é uma string interpolada, chama uma função para analisá-la
    elif len(p) == 4:  # Se há três elementos na lista de tokens
        if p[1] == '(' and p[3] == ')':
            p[0] = p[2] # Se a expressão é cercada por parênteses, retorna a expressão sem os parênteses
        elif p.slice[2].type == 'OPERADOR_ARITMETICO':
            p[0] = BinaryOperationNode(p[2], p[1], p[3]) # Se há uma operação aritmética, cria um nó de operação binária 
        elif p.slice[2].type == 'CONCATENACAO':
            p[0] = ConcatNode(p[1], p[3]) # Se há uma operação de concatenação de strings, cria um nó de concatenação
    elif len(p) == 5 and p.slice[1].type == 'ALEATORIO': # Se há cinco elementos na lista de tokens e o primeiro token é ALEATORIO
        p[0] = AleatorioNode(p[3]) # Cria um nó de aleatório com a expressão como argumento
    elif len(p) == 5 and p.slice[1].type == 'ENTRADA': # Se há cinco elementos na lista de tokens e o primeiro token é ENTRADA
        p[0] = EntradaNode()  # Cria um nó de entrada sem argumentos
        
# Esta função analisa strings interpoladas e cria um nó de árvore sintática para representá-las    
def parse_interpolated_string(s):
    parts = []
    while '#{' in s: 
        before, after = s.split('#{', 1)
        var, after = after.split('}', 1)
        if before:
            parts.append(StringNode(before)) # Adiciona a parte da string antes da variável
        parts.append(IdentifierNode(var.strip())) # Adiciona a variável
        s = after # Atualiza a string para a parte restante
    if s:
        parts.append(StringNode(s))
    result = parts[0]
    for part in parts[1:]:
        result = ConcatNode(result, part)
    return result

def p_function_call(p):
    '''function_call : IDENTIFICADOR PARENTESES_ESQ arg_list PARENTESES_DIR'''
    p[0] = FunctionCallNode(p[1], p[3])

# Esta função define uma regra de produção para listas de argumentos em chamadas de função
def p_arg_list(p):
    '''arg_list : arg_list COMMA expression
                | expression
                | empty'''
    # Verifica o número de elementos na lista de tokens
    if len(p) == 4:
        # Se houver três elementos na lista de tokens
        # e o segundo elemento for uma vírgula,
        # adiciona a expressão à lista de argumentos
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] is not None:
        # Se houver apenas um elemento na lista de tokens
        # e não for um valor vazio, cria uma lista com esse elemento
        p[0] = [p[1]]
    else:
        # Se não houver elementos na lista de tokens ou for um valor vazio,
        # retorna uma lista vazia
        p[0] = []

# A regra de produção 'empty' é usada para representar uma produção vazia, ou seja, 
# uma produção que não gera nenhum nó na árvore sintática.
def p_empty(p):
    'empty :'
    p[0] = None

# Função de tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe! Unexpected token: {p}")
    else:
        print("Erro de sintaxe! EOF inesperado") # EOF = End of File

# Cria o parser
parser = yacc.yacc()
