########## ANALISADOR LÉXICO ########## 

# O lexer é responsável por analisar o texto de entrada e dividir o código fonte em "tokens"
# Tokens são os elementos como palavras-chave, identificadores, números e símbolos especiais
# O lexer identifica padrões no texto de entrada usando expressões regulares e produz tokens 
# correspondentes a esses padrões
# Ele também remove espaços em branco e comentários, que são irrelevantes para a análise sintática
# A saída do lexer é uma sequência de tokens que é usada como entrada para o parser.


import ply.lex as lex

tokens = (
    'IDENTIFICADOR', 'NUMERO', 'OPERADOR_ARITMETICO', 'ATRIBUICAO',
    'PARENTESES_ESQ', 'PARENTESES_DIR', 'PONTO_E_VIRGULA',
    'ESCREVER', 'STRING', 'CONCATENACAO', 'INTERPOLATED_STRING',
    'ENTRADA', 'ALEATORIO', 'COMMA', 'COLON', 'FUNCAO', 'FIM'
)

t_OPERADOR_ARITMETICO = r'\+|\-|\*|\/'
t_ATRIBUICAO = r'='
t_PARENTESES_ESQ = r'\('
t_PARENTESES_DIR = r'\)'
t_PONTO_E_VIRGULA = r';'
t_CONCATENACAO = r'\<\>'
t_ESCREVER = r'escrever' 
t_COMMA = r','
t_COLON = r':'
t_FUNCAO = r'funcao'
t_FIM = r'fim'



# Expressão regular que reconhece espaços em branco e tabulações e os ignora.
t_ignore = ' \t'

# Expressão regular que reconhece strings interpoladas 
def t_INTERPOLATED_STRING(t):
    r'".*?\#\{.*?\}.*?"'
    t.value = t.value[1:-1]  # Remove as aspas da string reconhecida
    return t

# Expressão regular que reconhece strings simples.
def t_STRING(t):
    r'".*?"'
    t.value = t.value[1:-1]  # Remove as aspas da string reconhecida
    return t

# Expressão regular que reconhece identificadores, variaveis, funções , etc.
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*[!?]?' # Definido em enunciado
    if t.value == 'ESCREVER':
        t.type = 'ESCREVER'
    elif t.value == 'ENTRADA':
        t.type = 'ENTRADA'
    elif t.value == 'ALEATORIO':
        t.type = 'ALEATORIO'
    return t

# Expressão regular que reconhece números inteiros.
def t_NUMERO(t):
    r'\d+' # Combina um ou mais dígitos
    t.value = int(t.value)  # Converte o valor do token para um inteiro
    return t

# Expressão regular que reconhece novas linhas.
def t_newline(t):
    r'\n+' # Combina uma ou mais ocorrências de '\n'
    t.lexer.lineno += t.value.count('\n')  # Conta e atualiza o número de linhas


# Expressão regular que reconhece comentários.
def t_COMENTARIO(t):
    r'\-\-.*|{-.+?-}' # Combina comentários de linha e de bloco
    pass  # Passa a ignorar se for reconhecido um comentário


# Função de tratamento de erros para caracteres não reconhecidos
def t_error(t):
    print(f"Caractere não reconhecido '{t.value[0]}' na linha {t.lineno}")  
    t.lexer.skip(1)  # Ignora o caractere ilegal e avança para o próximo caractere


# Inicializa o lexer
lexer = lex.lex()
