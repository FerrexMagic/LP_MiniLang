import ply.yacc as yacc
from pl0.lexical import tokens
from pl0.nodes import AssignNode, DoNode, CallProcedureNode, ExpressionNode
from pl0.nodes import IfNode, InNode, Node, ConstNode, DeclareNode, BlockNode, DeclareProcedureNode, OutNode, WhileNode
from pl0.nodes.statements import ReturnNode, PrintNode, InputNode
from pl0.nodes.base import IdNode, NumberNode, StringNode, BoolNode

precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ', 'NEQ', 'AND', 'OR', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
)

def p_programa(p):
    """programa : procdecl"""
    p[0] = p[1]

def p_block(p):
    """block : constantdecl vardecl procdecl DO statementlist"""
    p[0] = BlockNode(p[1], p[2], p[3], p[5])

def p_empty(p):
    """empty :"""
    pass

def p_expr_id(p):
    "expression : ID"
    p[0] = IdNode(p[1])

def p_expr_number(p):
    "expression : NUMBER"
    p[0] = NumberNode(p[1])

def p_expr_string(p):
    "expression : PALABRA"
    p[0] = StringNode(p[1])

def p_expr_bool(p):
    """expression : TRUE
                | FALSE"""
    p[0] = BoolNode(p[1])


def p_expr(p):
    """expression : expression PLUS expression 
                    | expression MINUS expression 
                    | expression TIMES expression 
                    | expression DIV expression """
    p[0] = ExpressionNode(p[2], p[1], p[3])

def p_constant(p):
    """constantdecl : CONST type initlist SCOLON constantdecl
                    | empty"""
    p[0] = Node()
    if len(p) == 6:
        for i in range(len(p[3])):
            p[3][i]._type = p[2] # set the type of the constant
        p[0] = [*p[3], *p[5]]
    else:
        p[0] = []

def p_initlist(p):
    """initlist : ID ASSIGN expression COLON initlist
                | ID ASSIGN expression"""
    if len(p) == 6:
        p[0] = [ConstNode("", identifier=p[1], value=p[3]), *p[5]]
    else:
        p[0] = [ConstNode("", identifier=p[1], value=p[3])]

def p_type(p):
    """type : INT
            | BOOL
            | STRING"""
    p[0] = p[1]

def p_vardecl(p):
    """vardecl : type decllist SCOLON vardecl 
            | empty""" 
    p[0] = Node()
    if len(p) == 5:
        for i in range(len(p[2])):
            p[2][i]._type = p[1] # set the type of the variable
        p[0] = [*p[2], *p[4]]
    else:
        p[0] = []

def p_decllist(p):
    """decllist : ID COLON decllist 
                 | ID """
    if len(p) == 4:
        p[0] = [DeclareNode(_type="", identifier=p[1]), *p[3]]
    else:
        p[0] = [DeclareNode(_type="", identifier=p[1])]


def p_parenbool(p):
    "boolexpr : LPAREN boolexp RPAREN"
    p[0] = p[2]

def p_boolexpr(p):
    """boolexp : expression EQ expression
                | expression GT expression
                | expression LT expression
                | expression NEQ expression  
                | expression AND expression
                | expression OR expression
                | NOT expression """
    p[0] = ExpressionNode(operator=p[2], left=p[1], right=p[3])

def p_statement_do(p):
    """statement : DO statementlist END"""
    p[0] = DoNode(statements=p[2])

def p_statement_assign(p):
    "statement : ID ASSIGN expression"
    p[0] = AssignNode(identifier=p[1], value=p[3])

def p_statement_if(p):
    """statement : IF boolexpr DO statementlist else END"""
    p[0] = IfNode(condition=p[2], body=p[4], else_body=p[5])

def p_else(p):
    """else : ELSE statement
            | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_statement_while(p):
    "statement : WHILE boolexpr statement"
    p[0] = WhileNode(condition=p[2], body=p[3])

def p_statement_call(p):
    "statement : CALL ID"
    p[0] = CallProcedureNode(p[2])

def p_statement_in(p):
    "statement : IN ID"
    p[0] = InNode(p[2])

def p_statement_out(p):
    "statement : OUT expression"
    p[0] = OutNode(p[2])

def p_statement_print(p):
    """statement : PRINT LPAREN expression RPAREN"""
    p[0] = PrintNode(p[3])


def p_statement_input(p):
    """statement : ID ASSIGN INPUT LPAREN expression RPAREN
                | ID ASSIGN INPUT LPAREN empty RPAREN"""
    p[0] = AssignNode(identifier=p[1], value=InputNode(PrintNode(p[5])))


def p_statement_return(p):
    """statement : RETURN expression
                | RETURN boolexp
                | RETURN """
    p[0] = ReturnNode(p[2])

def p_statement_empty(p):
    "statement : empty"
    p[0] = []

def p_retType(p):
    """retType : type
                | VOID"""
    p[0] = p[1]


def p_funcion(p):
    """expression : ID LPAREN param RPAREN
                | ID LPAREN RPAREN SCOLON"""
    p[0] = CallProcedureNode(p[1])

def p_param(p):
    """param : ID COLON param
            | ID"""
    if len(p) == 4:
        p[0] = [p[1], *p[3]]
    else:
        p[0] = [p[1]]

def p_proc(p):
    """proc : SUBROUTINE retType ID LPAREN varlist RPAREN block END"""
    p[0] = DeclareProcedureNode(identifier=p[3], return_type=p[2], block=p[7], param=p[5])

def p_varlist(p):
    """varlist : type ID COLON varlist
              | type ID
              | empty"""
    if len(p) == 5:
        p[0] = [DeclareNode(_type=p[1], identifier=p[2]), *p[4]]
    elif len(p) == 3:
        p[0] = [DeclareNode(_type=p[1], identifier=p[2])]
    else:
        p[0] = []


def p_procdecl(p):
    """procdecl : proc procdecl
                | empty"""
    if len(p) == 3:
        p[0] = [p[1], *p[2]]
    else:
        p[0] = []


def p_statement_list(p):
    """statementlist : statement SCOLON statementlist 
                    | statement"""
    if len(p) == 4:
        p[0] = [p[1], *p[3]]
    else:
        p[0] = [p[1]]


def p_error(p):
    print(f"Syntax error at {p.value} position {p.lexpos} line {p.lineno}")
    raise SystemExit
parser = yacc.yacc(debug=True)
