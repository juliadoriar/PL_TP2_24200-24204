import ply.yacc as yacc
from lexer import tokens

# Definição dos nós da AST (Abstract Syntax Tree) para representar a estrutura do programa fonte.
# A AST é uma representação hierárquica do código fonte que captura sua estrutura sintática de forma mais compacta e manipulável.
# Cada nó da AST representa uma construção sintática do programa, como uma declaração, uma expressão ou uma instrução.
# Os nós serão utilizados pelo parser para construir a árvore sintática do programa e pelo interpretador para executar o programa.
class ExpressionNode:
    pass
class ProgramNode:
    def __init__(self, statements):
        # O nó ProgramNode representa o programa como um todo.
        # Ele contém uma lista de nós que representam todas as declarações e instruções do programa.
        self.statements = statements
        
    def __str__(self):
        # Este método permite que o nó do programa seja representado como uma string.
        # Ele retorna uma string que contém a representação de todos os nós de declaração e instrução do programa.
        return "\n".join(str(stmt) for stmt in self.statements)

class AssignmentNode:
    def __init__(self, identifier, expression):
        # O nó AssignmentNode representa uma instrução de atribuição, onde um valor é atribuído a uma variável.
        # Ele armazena o identificador da variável e a expressão que será atribuída a ela.
        self.identifier = identifier  # Identificador da variável
        self.expression = expression  # Expressão atribuída à variável
        
    def __str__(self):
        # Este método permite que o nó de atribuição seja representado como uma string.
        # Ele retorna uma string que contém o identificador da variável e a expressão atribuída.
        return f"AssignmentNode({self.identifier}, {self.expression})"

class WriteNode:
    def __init__(self, expression):
        # O nó WriteNode representa uma instrução de escrita, onde o valor de uma expressão é escrito na saída.
        # Ele armazena a expressão que será escrita na saída.
        self.expression = expression  # Expressão a ser escrita na saída

class BinaryOperationNode:
    def __init__(self, operator, left, right):
        # O nó BinaryOperationNode representa uma operação binária, como adição, subtração, multiplicação ou divisão.
        # Ele armazena o operador da operação, o lado esquerdo e o lado direito da expressão.
        self.operator = operator  # Operador da operação binária
        self.left = left  # Lado esquerdo da operação
        self.right = right  # Lado direito da operação

class UnaryOperationNode:
    def __init__(self, operator, operand):
        # O nó UnaryOperationNode representa uma operação unária, como um operador de sinal positivo ou negativo.
        # Ele armazena o operador da operação e o operando da operação.
        self.operator = operator  # Operador da operação unária
        self.operand = operand  # Operando da operação

class IdentifierNode:
    def __init__(self, name):
        # O nó IdentifierNode representa um identificador, ou seja, o nome de uma variável.
        # Ele armazena o nome da variável.
        self.name = name  # Nome da variável

class NumberNode:
    def __init__(self, value):
        # O nó NumberNode representa um valor numérico, como um número inteiro ou decimal.
        # Ele armazena o valor numérico.
        self.value = value  # Valor numérico

class AleatoryNode:
    def __init__(self, expression):
        # O nó AleatoryNode representa uma expressão que determina o valor máximo para a geração de um número aleatório.
        # Ele armazena a expressão que determina o valor máximo para a aleatoriedade.
        self.expression = expression  # Expressão que determina o valor máximo para a aleatoriedade
        
class ConcatNode:
    def __init__(self, left, right):
        # O nó ConcatNode representa uma operação de concatenação de strings.
        # A concatenação é uma operação que combina duas strings em uma única string.
        self.left = left
        self.right = right

class StringNode:
    # O nó StringNode representa uma string, ou seja, uma sequência de caracteres.
    # Ele armazena o valor da string.
    def __init__(self, value):
        self.value = value
        
class EntradaNode(ExpressionNode):
    # O nó EntradaNode representa uma instrução de entrada, onde o usuário fornece um valor para uma variável.
    # Ele não armazena nenhum valor, pois a entrada é tratada externamente ao interpretar o programa.
    def __init__(self):
        pass

class AleatorioNode(ExpressionNode):
    # O nó AleatorioNode representa uma expressão que gera um número aleatório entre 0 e um valor máximo.
    # Ele armazena a expressão que determina o valor máximo para a geração do número aleatório.
    def __init__(self, expression):
        self.expression = expression
        
class InterpolatedStringNode(ExpressionNode):
    # O nó InterpolatedStringNode representa uma string interpolada, que contém expressões embutidas.
    # Ele armazena uma lista de partes da string, que podem ser strings simples ou expressões.
    def __init__(self, value):
        self.value = value

class FunctionNode:
    # O nó FunctionNode representa uma declaração de função, que define uma função no programa.
    # Ele armazena o nome da função, os parâmetros da função e o corpo da função.
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode:
    # O nó FunctionCallNode representa uma chamada de função, onde uma função é invocada com argumentos.
    # Ele armazena o nome da função e os argumentos passados para a função.
    def __init__(self, name, args):
        self.name = name
        self.args = args