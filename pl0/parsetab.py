
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTEQNEQANDORNOTleftPLUSMINUSleftTIMESDIVAND AND ASSIGN BOOL BOOL CALL CALL COLON CONST CONST DIV DO DO ELSE ELSE END END EQ FALSE FALSE GT ID IF IF IN IN INPUT INPUT INT INT LPAREN LT MINUS NEQ NOT NOT NUMBER ODD ODD OR OR OUT OUT PALABRA PLUS PRINT PRINT RETURN RETURN RPAREN SCOLON STRING STRING SUBROUTINE SUBROUTINE THEN THEN TIMES TRUE TRUE VOID VOID WHILE WHILEprograma : procdeclblock : constantdecl vardecl procdecl DO statementlistempty :expression : IDexpression : NUMBERexpression : PALABRAexpression : TRUE\n                | FALSEexpression : expression PLUS expression \n                    | expression MINUS expression \n                    | expression TIMES expression \n                    | expression DIV expression constantdecl : CONST type initlist SCOLON constantdecl\n                    | emptyinitlist : ID ASSIGN expression COLON initlist\n                | ID ASSIGN expressiontype : INT\n            | BOOL\n            | STRINGvardecl : type decllist SCOLON vardecl \n            | emptydecllist : ID COLON decllist \n                 | ID boolexpr : LPAREN boolexp RPARENboolexp : expression EQ expression\n                | expression GT expression\n                | expression LT expression\n                | expression NEQ expression  \n                | expression AND expression\n                | expression OR expression\n                | NOT expression statement : DO statementlist ENDstatement : ID ASSIGN expressionstatement : IF boolexpr DO statementlist else ENDelse : ELSE statement\n            | emptystatement : WHILE boolexpr statementstatement : CALL IDstatement : IN IDstatement : OUT expressionstatement : PRINT LPAREN expression RPARENstatement : ID ASSIGN INPUT LPAREN expression RPAREN\n                | ID ASSIGN INPUT LPAREN empty RPARENstatement : RETURN expression\n                | RETURN boolexp\n                | RETURN statement : emptyretType : type\n                | VOIDexpression : ID LPAREN param RPAREN\n                | ID LPAREN RPAREN SCOLONparam : ID COLON param\n            | IDproc : SUBROUTINE retType ID LPAREN varlist RPAREN block ENDvarlist : type ID COLON varlist\n              | type ID\n              | emptyprocdecl : proc procdecl\n                | emptystatementlist : statement SCOLON statementlist \n                    | statement'
    
_lr_action_items = {'SUBROUTINE':([0,3,18,21,23,25,26,28,37,39,53,55,],[5,5,-3,-3,-14,-54,5,-21,-3,-3,-20,-13,]),'$end':([0,1,2,3,4,6,25,],[-3,0,-1,-3,-59,-58,-54,]),'DO':([3,4,6,18,21,23,25,26,28,31,36,37,39,41,53,55,63,65,67,85,107,121,],[-3,-59,-58,-3,-3,-14,-54,-3,-21,36,41,-3,-3,41,-20,-13,41,85,41,41,-24,41,]),'VOID':([5,],[9,]),'INT':([5,14,18,21,22,23,24,37,39,55,],[10,10,-3,10,10,-14,10,10,-3,-13,]),'BOOL':([5,14,18,21,22,23,24,37,39,55,],[11,11,-3,11,11,-14,11,11,-3,-13,]),'STRING':([5,14,18,21,22,23,24,37,39,55,],[12,12,-3,12,12,-14,12,12,-3,-13,]),'ID':([7,8,9,10,11,12,16,27,29,36,38,40,41,47,48,49,52,63,64,66,67,71,74,75,76,77,78,79,80,85,90,91,92,93,94,95,105,107,115,121,],[13,-48,-49,-17,-18,-19,19,33,35,44,33,56,44,68,69,56,56,44,56,56,44,56,56,97,35,56,56,56,56,44,56,56,56,56,56,56,56,-24,97,44,]),'LPAREN':([13,45,46,50,56,84,],[14,66,66,71,75,105,]),'RPAREN':([14,15,17,19,24,30,56,58,59,60,61,75,86,89,96,97,98,101,102,103,104,105,109,110,111,112,113,114,116,117,118,119,123,],[-3,18,-57,-56,-3,-55,-4,-5,-6,-7,-8,99,107,108,-31,-53,116,-9,-10,-11,-12,-3,-25,-26,-27,-28,-29,-30,-50,-51,124,125,-52,]),'CONST':([18,39,],[22,22,]),'COLON':([19,33,56,57,58,59,60,61,97,101,102,103,104,116,117,],[24,38,-4,76,-5,-6,-7,-8,115,-9,-10,-11,-12,-50,-51,]),'END':([20,36,41,42,43,51,52,56,58,59,60,61,62,63,67,68,69,70,72,73,81,82,83,85,88,96,101,102,103,104,106,107,108,109,110,111,112,113,114,116,117,120,121,122,124,125,126,127,],[25,-3,-3,-2,-61,-47,-46,-4,-5,-6,-7,-8,81,-3,-3,-38,-39,-40,-44,-45,-32,-60,-33,-3,-37,-31,-9,-10,-11,-12,-3,-24,-41,-25,-26,-27,-28,-29,-30,-50,-51,126,-3,-36,-42,-43,-34,-35,]),'SCOLON':([32,33,34,36,41,43,51,52,54,56,57,58,59,60,61,63,67,68,69,70,72,73,81,83,85,88,96,99,100,101,102,103,104,107,108,109,110,111,112,113,114,116,117,124,125,126,],[37,-23,39,-3,-3,63,-47,-46,-22,-4,-16,-5,-6,-7,-8,-3,-3,-38,-39,-40,-44,-45,-32,-33,-3,-37,-31,117,-15,-9,-10,-11,-12,-24,-41,-25,-26,-27,-28,-29,-30,-50,-51,-42,-43,-34,]),'ASSIGN':([35,44,],[40,64,]),'IF':([36,41,63,67,85,107,121,],[45,45,45,45,45,-24,45,]),'WHILE':([36,41,63,67,85,107,121,],[46,46,46,46,46,-24,46,]),'CALL':([36,41,63,67,85,107,121,],[47,47,47,47,47,-24,47,]),'IN':([36,41,63,67,85,107,121,],[48,48,48,48,48,-24,48,]),'OUT':([36,41,63,67,85,107,121,],[49,49,49,49,49,-24,49,]),'PRINT':([36,41,63,67,85,107,121,],[50,50,50,50,50,-24,50,]),'RETURN':([36,41,63,67,85,107,121,],[52,52,52,52,52,-24,52,]),'NUMBER':([40,49,52,64,66,71,74,77,78,79,80,90,91,92,93,94,95,105,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'PALABRA':([40,49,52,64,66,71,74,77,78,79,80,90,91,92,93,94,95,105,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'TRUE':([40,49,52,64,66,71,74,77,78,79,80,90,91,92,93,94,95,105,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'FALSE':([40,49,52,64,66,71,74,77,78,79,80,90,91,92,93,94,95,105,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'ELSE':([43,51,52,56,58,59,60,61,63,67,68,69,70,72,73,81,82,83,85,88,96,101,102,103,104,106,107,108,109,110,111,112,113,114,116,117,124,125,126,],[-61,-47,-46,-4,-5,-6,-7,-8,-3,-3,-38,-39,-40,-44,-45,-32,-60,-33,-3,-37,-31,-9,-10,-11,-12,121,-24,-41,-25,-26,-27,-28,-29,-30,-50,-51,-42,-43,-34,]),'NOT':([52,66,],[74,74,]),'PLUS':([56,57,58,59,60,61,70,72,83,87,89,96,101,102,103,104,109,110,111,112,113,114,116,117,118,],[-4,77,-5,-6,-7,-8,77,77,77,77,77,77,-9,-10,-11,-12,77,77,77,77,77,77,-50,-51,77,]),'MINUS':([56,57,58,59,60,61,70,72,83,87,89,96,101,102,103,104,109,110,111,112,113,114,116,117,118,],[-4,78,-5,-6,-7,-8,78,78,78,78,78,78,-9,-10,-11,-12,78,78,78,78,78,78,-50,-51,78,]),'TIMES':([56,57,58,59,60,61,70,72,83,87,89,96,101,102,103,104,109,110,111,112,113,114,116,117,118,],[-4,79,-5,-6,-7,-8,79,79,79,79,79,79,79,79,-11,-12,79,79,79,79,79,79,-50,-51,79,]),'DIV':([56,57,58,59,60,61,70,72,83,87,89,96,101,102,103,104,109,110,111,112,113,114,116,117,118,],[-4,80,-5,-6,-7,-8,80,80,80,80,80,80,80,80,-11,-12,80,80,80,80,80,80,-50,-51,80,]),'EQ':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,90,90,-9,-10,-11,-12,-50,-51,]),'GT':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,91,91,-9,-10,-11,-12,-50,-51,]),'LT':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,92,92,-9,-10,-11,-12,-50,-51,]),'NEQ':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,93,93,-9,-10,-11,-12,-50,-51,]),'AND':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,94,94,-9,-10,-11,-12,-50,-51,]),'OR':([56,58,59,60,61,72,87,101,102,103,104,116,117,],[-4,-5,-6,-7,-8,95,95,-9,-10,-11,-12,-50,-51,]),'INPUT':([64,],[84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'procdecl':([0,3,26,],[2,6,31,]),'proc':([0,3,26,],[3,3,3,]),'empty':([0,3,14,18,21,24,26,36,37,39,41,63,67,85,105,106,121,],[4,4,17,23,28,17,4,51,28,23,51,51,51,51,119,122,51,]),'retType':([5,],[7,]),'type':([5,14,21,22,24,37,],[8,16,27,29,16,27,]),'varlist':([14,24,],[15,30,]),'block':([18,],[20,]),'constantdecl':([18,39,],[21,55,]),'vardecl':([21,37,],[26,53,]),'decllist':([27,38,],[32,54,]),'initlist':([29,76,],[34,100,]),'statementlist':([36,41,63,85,],[42,62,82,106,]),'statement':([36,41,63,67,85,121,],[43,43,43,88,43,127,]),'expression':([40,49,52,64,66,71,74,77,78,79,80,90,91,92,93,94,95,105,],[57,70,72,83,87,89,96,101,102,103,104,109,110,111,112,113,114,118,]),'boolexpr':([45,46,],[65,67,]),'boolexp':([52,66,],[73,86,]),'param':([75,115,],[98,123,]),'else':([106,],[120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> procdecl','programa',1,'p_programa','parse.py',15),
  ('block -> constantdecl vardecl procdecl DO statementlist','block',5,'p_block','parse.py',19),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',23),
  ('expression -> ID','expression',1,'p_expr_id','parse.py',27),
  ('expression -> NUMBER','expression',1,'p_expr_number','parse.py',31),
  ('expression -> PALABRA','expression',1,'p_expr_string','parse.py',35),
  ('expression -> TRUE','expression',1,'p_expr_bool','parse.py',39),
  ('expression -> FALSE','expression',1,'p_expr_bool','parse.py',40),
  ('expression -> expression PLUS expression','expression',3,'p_expr','parse.py',45),
  ('expression -> expression MINUS expression','expression',3,'p_expr','parse.py',46),
  ('expression -> expression TIMES expression','expression',3,'p_expr','parse.py',47),
  ('expression -> expression DIV expression','expression',3,'p_expr','parse.py',48),
  ('constantdecl -> CONST type initlist SCOLON constantdecl','constantdecl',5,'p_constant','parse.py',52),
  ('constantdecl -> empty','constantdecl',1,'p_constant','parse.py',53),
  ('initlist -> ID ASSIGN expression COLON initlist','initlist',5,'p_initlist','parse.py',63),
  ('initlist -> ID ASSIGN expression','initlist',3,'p_initlist','parse.py',64),
  ('type -> INT','type',1,'p_type','parse.py',71),
  ('type -> BOOL','type',1,'p_type','parse.py',72),
  ('type -> STRING','type',1,'p_type','parse.py',73),
  ('vardecl -> type decllist SCOLON vardecl','vardecl',4,'p_vardecl','parse.py',77),
  ('vardecl -> empty','vardecl',1,'p_vardecl','parse.py',78),
  ('decllist -> ID COLON decllist','decllist',3,'p_decllist','parse.py',88),
  ('decllist -> ID','decllist',1,'p_decllist','parse.py',89),
  ('boolexpr -> LPAREN boolexp RPAREN','boolexpr',3,'p_parenbool','parse.py',97),
  ('boolexp -> expression EQ expression','boolexp',3,'p_boolexpr','parse.py',101),
  ('boolexp -> expression GT expression','boolexp',3,'p_boolexpr','parse.py',102),
  ('boolexp -> expression LT expression','boolexp',3,'p_boolexpr','parse.py',103),
  ('boolexp -> expression NEQ expression','boolexp',3,'p_boolexpr','parse.py',104),
  ('boolexp -> expression AND expression','boolexp',3,'p_boolexpr','parse.py',105),
  ('boolexp -> expression OR expression','boolexp',3,'p_boolexpr','parse.py',106),
  ('boolexp -> NOT expression','boolexp',2,'p_boolexpr','parse.py',107),
  ('statement -> DO statementlist END','statement',3,'p_statement_do','parse.py',111),
  ('statement -> ID ASSIGN expression','statement',3,'p_statement_assign','parse.py',115),
  ('statement -> IF boolexpr DO statementlist else END','statement',6,'p_statement_if','parse.py',119),
  ('else -> ELSE statement','else',2,'p_else','parse.py',123),
  ('else -> empty','else',1,'p_else','parse.py',124),
  ('statement -> WHILE boolexpr statement','statement',3,'p_statement_while','parse.py',131),
  ('statement -> CALL ID','statement',2,'p_statement_call','parse.py',135),
  ('statement -> IN ID','statement',2,'p_statement_in','parse.py',139),
  ('statement -> OUT expression','statement',2,'p_statement_out','parse.py',143),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','parse.py',147),
  ('statement -> ID ASSIGN INPUT LPAREN expression RPAREN','statement',6,'p_statement_input','parse.py',152),
  ('statement -> ID ASSIGN INPUT LPAREN empty RPAREN','statement',6,'p_statement_input','parse.py',153),
  ('statement -> RETURN expression','statement',2,'p_statement_return','parse.py',158),
  ('statement -> RETURN boolexp','statement',2,'p_statement_return','parse.py',159),
  ('statement -> RETURN','statement',1,'p_statement_return','parse.py',160),
  ('statement -> empty','statement',1,'p_statement_empty','parse.py',164),
  ('retType -> type','retType',1,'p_retType','parse.py',168),
  ('retType -> VOID','retType',1,'p_retType','parse.py',169),
  ('expression -> ID LPAREN param RPAREN','expression',4,'p_funcion','parse.py',174),
  ('expression -> ID LPAREN RPAREN SCOLON','expression',4,'p_funcion','parse.py',175),
  ('param -> ID COLON param','param',3,'p_param','parse.py',179),
  ('param -> ID','param',1,'p_param','parse.py',180),
  ('proc -> SUBROUTINE retType ID LPAREN varlist RPAREN block END','proc',8,'p_proc','parse.py',187),
  ('varlist -> type ID COLON varlist','varlist',4,'p_varlist','parse.py',191),
  ('varlist -> type ID','varlist',2,'p_varlist','parse.py',192),
  ('varlist -> empty','varlist',1,'p_varlist','parse.py',193),
  ('procdecl -> proc procdecl','procdecl',2,'p_procdecl','parse.py',203),
  ('procdecl -> empty','procdecl',1,'p_procdecl','parse.py',204),
  ('statementlist -> statement SCOLON statementlist','statementlist',3,'p_statement_list','parse.py',212),
  ('statementlist -> statement','statementlist',1,'p_statement_list','parse.py',213),
]
