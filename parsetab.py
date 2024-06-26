
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALEATORIO ATRIBUICAO COLON COMMA CONCATENACAO ENTRADA ESCREVER FIM FUNCAO IDENTIFICADOR INTERPOLATED_STRING NUMERO OPERADOR_ARITMETICO PARENTESES_DIR PARENTESES_ESQ PONTO_E_VIRGULA STRINGprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : IDENTIFICADOR ATRIBUICAO expression PONTO_E_VIRGULAstatement : ESCREVER PARENTESES_ESQ expression PARENTESES_DIR PONTO_E_VIRGULAstatement : FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement FIM\n                 | FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement_list FIMparam_list : param_list COMMA IDENTIFICADOR\n                  | IDENTIFICADOR\n                  | empty\n    expression : IDENTIFICADOR\n               | NUMERO\n               | STRING\n               | INTERPOLATED_STRING\n               | expression OPERADOR_ARITMETICO expression\n               | expression CONCATENACAO expression\n               | PARENTESES_ESQ expression PARENTESES_DIR\n               | function_call\n               | ENTRADA PARENTESES_ESQ PARENTESES_DIR\n               | ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR\n    function_call : IDENTIFICADOR PARENTESES_ESQ arg_list PARENTESES_DIRarg_list : arg_list COMMA expression\n                | expression\n                | emptyempty :'
    
_lr_action_items = {'IDENTIFICADOR':([0,2,3,6,7,8,9,16,21,22,23,24,25,28,41,43,45,47,50,51,52,53,],[4,4,-3,10,-2,11,11,11,30,11,-4,11,11,11,-5,48,11,4,-3,4,-6,-7,]),'ESCREVER':([0,2,3,7,23,41,47,50,51,52,53,],[5,5,-3,-2,-4,-5,5,-3,5,-6,-7,]),'FUNCAO':([0,2,3,7,23,41,47,50,51,52,53,],[6,6,-3,-2,-4,-5,6,-3,6,-6,-7,]),'$end':([1,2,3,7,23,41,52,53,],[0,-1,-3,-2,-4,-5,-6,-7,]),'ATRIBUICAO':([4,],[8,]),'PARENTESES_ESQ':([5,8,9,10,11,16,18,19,22,24,25,28,45,],[9,16,16,21,22,16,27,28,16,16,16,16,16,]),'FIM':([7,23,41,50,51,52,53,],[-2,-4,-5,52,53,-6,-7,]),'NUMERO':([8,9,16,22,24,25,28,45,],[13,13,13,13,13,13,13,13,]),'STRING':([8,9,16,22,24,25,28,45,],[14,14,14,14,14,14,14,14,]),'INTERPOLATED_STRING':([8,9,16,22,24,25,28,45,],[15,15,15,15,15,15,15,15,]),'ENTRADA':([8,9,16,22,24,25,28,45,],[18,18,18,18,18,18,18,18,]),'ALEATORIO':([8,9,16,22,24,25,28,45,],[19,19,19,19,19,19,19,19,]),'PONTO_E_VIRGULA':([11,12,13,14,15,17,29,36,37,38,39,44,46,],[-11,23,-12,-13,-14,-18,41,-15,-16,-17,-19,-21,-20,]),'OPERADOR_ARITMETICO':([11,12,13,14,15,17,20,26,34,36,37,38,39,40,44,46,49,],[-11,24,-12,-13,-14,-18,24,24,24,24,24,-17,-19,24,-21,-20,24,]),'CONCATENACAO':([11,12,13,14,15,17,20,26,34,36,37,38,39,40,44,46,49,],[-11,25,-12,-13,-14,-18,25,25,25,25,25,-17,-19,25,-21,-20,25,]),'PARENTESES_DIR':([11,13,14,15,17,20,21,22,26,27,30,31,32,33,34,35,36,37,38,39,40,44,46,48,49,],[-11,-12,-13,-14,-18,29,-25,-25,38,39,-9,42,-10,44,-23,-24,-15,-16,-17,-19,46,-21,-20,-8,-22,]),'COMMA':([11,13,14,15,17,21,22,30,31,32,33,34,35,36,37,38,39,44,46,48,49,],[-11,-12,-13,-14,-18,-25,-25,-9,43,-10,45,-23,-24,-15,-16,-17,-19,-21,-20,-8,-22,]),'COLON':([42,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,47,],[2,51,]),'statement':([0,2,47,51,],[3,7,50,7,]),'expression':([8,9,16,22,24,25,28,45,],[12,20,26,34,36,37,40,49,]),'function_call':([8,9,16,22,24,25,28,45,],[17,17,17,17,17,17,17,17,]),'param_list':([21,],[31,]),'empty':([21,22,],[32,35,]),'arg_list':([22,],[33,]),}

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
  ('statement -> FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement FIM','statement',8,'p_statement_function','parser_1.py',31),
  ('statement -> FUNCAO IDENTIFICADOR PARENTESES_ESQ param_list PARENTESES_DIR COLON statement_list FIM','statement',8,'p_statement_function','parser_1.py',32),
  ('param_list -> param_list COMMA IDENTIFICADOR','param_list',3,'p_param_list','parser_1.py',40),
  ('param_list -> IDENTIFICADOR','param_list',1,'p_param_list','parser_1.py',41),
  ('param_list -> empty','param_list',1,'p_param_list','parser_1.py',42),
  ('expression -> IDENTIFICADOR','expression',1,'p_expression','parser_1.py',52),
  ('expression -> NUMERO','expression',1,'p_expression','parser_1.py',53),
  ('expression -> STRING','expression',1,'p_expression','parser_1.py',54),
  ('expression -> INTERPOLATED_STRING','expression',1,'p_expression','parser_1.py',55),
  ('expression -> expression OPERADOR_ARITMETICO expression','expression',3,'p_expression','parser_1.py',56),
  ('expression -> expression CONCATENACAO expression','expression',3,'p_expression','parser_1.py',57),
  ('expression -> PARENTESES_ESQ expression PARENTESES_DIR','expression',3,'p_expression','parser_1.py',58),
  ('expression -> function_call','expression',1,'p_expression','parser_1.py',59),
  ('expression -> ENTRADA PARENTESES_ESQ PARENTESES_DIR','expression',3,'p_expression','parser_1.py',60),
  ('expression -> ALEATORIO PARENTESES_ESQ expression PARENTESES_DIR','expression',4,'p_expression','parser_1.py',61),
  ('function_call -> IDENTIFICADOR PARENTESES_ESQ arg_list PARENTESES_DIR','function_call',4,'p_function_call','parser_1.py',114),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','parser_1.py',118),
  ('arg_list -> expression','arg_list',1,'p_arg_list','parser_1.py',119),
  ('arg_list -> empty','arg_list',1,'p_arg_list','parser_1.py',120),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',142),
]
