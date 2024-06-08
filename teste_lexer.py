from lexer import lexer

# Exemplo de código para testar
data = '''
tmp_01 = 2*3+4 ;
a1_ = 12345 - (5191 * 15) ;
idade_valida? = 1;
mult_3! = a1_ * 3 ;
'''

# Inicializa o lexer com o código de exemplo
lexer.input(data)

# Itera sobre os tokens gerados e imprime-os
print("Tokens gerados:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)