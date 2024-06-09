
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALEATORIO ATRIBUICAO CONCATENACAO ENTRADA ESCREVER IDENTIFICADOR INTERPOLATED_STRING NUMERO OPERADOR_ARITMETICO PARENTESES_DIR PARENTESES_ESQ PONTO_E_VIRGULA STRINGprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULAstatement : ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULA\n    expression : IDENTIFICADOR\n               | NUMERO\n               | STRING\n               | INTERPOLATED_STRING\n               | expression OPERADOR_ARITMETICO expression\n               | expression CONCATENACAO expression\n               | PARENTESES_ESQ expression PARENTESES_DIR\n               | ENTRADA PARENTESES_ESQ PARENTESES_DIR\n               | ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR\n    '
    
_lr_action_items = {'IDENTIFICADOR':([0,2,3,6,7,8,14,18,19,20,23,30,],[4,4,-3,-2,9,9,9,-4,9,9,9,-5,]),'ESCREVER':([0,2,3,6,18,30,],[5,5,-3,-2,-4,-5,]),'$end':([1,2,3,6,18,30,],[0,-1,-3,-2,-4,-5,]),'ATRIBUICAO':([4,],[7,]),'PARENTESES_ESQ':([5,7,8,14,15,16,19,20,23,],[8,14,14,14,22,23,14,14,14,]),'NUMERO':([7,8,14,19,20,23,],[11,11,11,11,11,11,]),'STRING':([7,8,14,19,20,23,],[12,12,12,12,12,12,]),'INTERPOLATED_STRING':([7,8,14,19,20,23,],[13,13,13,13,13,13,]),'ENTRADA':([7,8,14,19,20,23,],[15,15,15,15,15,15,]),'ALEATORIO':([7,8,14,19,20,23,],[16,16,16,16,16,16,]),'PONTO_E_VIRGULA':([9,10,11,12,13,24,25,26,27,28,31,],[-6,18,-7,-8,-9,30,-10,-11,-12,-13,-14,]),'OPERADOR_ARITMETICO':([9,10,11,12,13,17,21,25,26,27,28,29,31,],[-6,19,-7,-8,-9,19,19,19,19,-12,-13,19,-14,]),'CONCATENACAO':([9,10,11,12,13,17,21,25,26,27,28,29,31,],[-6,20,-7,-8,-9,20,20,20,20,-12,-13,20,-14,]),'PARENTESES_DIR':([9,11,12,13,17,21,22,25,26,27,28,29,31,],[-6,-7,-8,-9,24,27,28,-10,-11,-12,-13,31,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,],[3,6,]),'expression':([7,8,14,19,20,23,],[10,17,21,25,26,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser_1.py',11),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser_1.py',15),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser_1.py',16),
  ('statement -> IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULA','statement',4,'p_statement_assign','parser_1.py',23),
  ('statement -> ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULA','statement',5,'p_statement_write','parser_1.py',27),
  ('expression -> IDENTIFICADOR','expression',1,'p_expression','parser_1.py',32),
  ('expression -> NUMERO','expression',1,'p_expression','parser_1.py',33),
  ('expression -> STRING','expression',1,'p_expression','parser_1.py',34),
  ('expression -> INTERPOLATED_STRING','expression',1,'p_expression','parser_1.py',35),
  ('expression -> expression OPERADOR_ARITMETICO expression','expression',3,'p_expression','parser_1.py',36),
  ('expression -> expression CONCATENACAO expression','expression',3,'p_expression','parser_1.py',37),
  ('expression -> PARENTESES_ESQ expression PARENTESES_DIR','expression',3,'p_expression','parser_1.py',38),
  ('expression -> ENTRADA PARENTESES_ESQ PARENTESES_DIR','expression',3,'p_expression','parser_1.py',39),
  ('expression -> ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR','expression',4,'p_expression','parser_1.py',40),
]
