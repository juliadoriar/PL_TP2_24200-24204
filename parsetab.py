
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUICAO ESCREVER IDENTIFICADOR NUMERO OPERADOR_ARITMETICO PARENTESES_DIR PARENTESES_ESQ PONTO_E_VIRGULAprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULAstatement : ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULA\n    expression : IDENTIFICADOR\n               | NUMERO\n               | expression OPERADOR_ARITMETICO expression\n               | PARENTESES_ESQ expression PARENTESES_DIR\n    term : term OPERADOR_ARITMETICO factor\n            | factorfactor : PARENTESES_ESQ expression PARENTESES_DIR\n              | NUMERO\n              | IDENTIFICADOR'
    
_lr_action_items = {'IDENTIFICADOR':([0,2,3,6,7,8,12,14,15,20,],[4,4,-3,-2,9,9,9,-4,9,-5,]),'ESCREVER':([0,2,3,6,14,20,],[5,5,-3,-2,-4,-5,]),'$end':([1,2,3,6,14,20,],[0,-1,-3,-2,-4,-5,]),'ATRIBUICAO':([4,],[7,]),'PARENTESES_ESQ':([5,7,8,12,15,],[8,12,12,12,12,]),'NUMERO':([7,8,12,15,],[11,11,11,11,]),'PONTO_E_VIRGULA':([9,10,11,17,18,19,],[-6,14,-7,20,-8,-9,]),'OPERADOR_ARITMETICO':([9,10,11,13,16,18,19,],[-6,15,-7,15,15,15,-9,]),'PARENTESES_DIR':([9,11,13,16,18,19,],[-6,-7,17,19,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,],[3,6,]),'expression':([7,8,12,15,],[10,13,16,18,]),}

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
  ('expression -> expression OPERADOR_ARITMETICO expression','expression',3,'p_expression','parser_1.py',34),
  ('expression -> PARENTESES_ESQ expression PARENTESES_DIR','expression',3,'p_expression','parser_1.py',35),
  ('term -> term OPERADOR_ARITMETICO factor','term',3,'p_term','parser_1.py',48),
  ('term -> factor','term',1,'p_term','parser_1.py',49),
  ('factor -> PARENTESES_ESQ expression PARENTESES_DIR','factor',3,'p_factor','parser_1.py',56),
  ('factor -> NUMERO','factor',1,'p_factor','parser_1.py',57),
  ('factor -> IDENTIFICADOR','factor',1,'p_factor','parser_1.py',58),
]
