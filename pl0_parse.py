import ply.yacc as yacc
from pl0_lex import tokens
from pl0.nodes import AssignNode, BeginNode, CallProcedureNode, ExpressionNode, IfNode, InNode, Node, ConstNode, DeclareNode, BlockNode, DeclareProcedureNode, OutNode, WhileNode
precedence = (
    ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
)
def p_programa(p):
    """programa : block"""
    p[0] = p[1]
    
def p_block(p):
    """block : constantdecl vardecl procdecl statement"""
    p[0] = BlockNode(p[1],p[2],p[3], p[4])
def p_empty(p):
    """empty :"""    


def p_expr(p):
    """expression : expression PLUS expression 
                    | expression MINUS expression 
                    | expression TIMES expression 
                    | expression DIV expression 
                    | LPAREN expression RPAREN 
                    | ID 
                    | NUMBER"""
    ...
def p_constant(p):
    """constantdecl : CONST initlist SCOLON
                    | empty"""
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []
    
def p_initlist(p):
    """initlist : ID EQ NUMBER COLON initlist
                | ID EQ NUMBER"""
    if len(p) == 6:
        p[0] = [ConstNode("int", p[1], p[3]), *p[5]]
    else:
        p[0] = [ConstNode("int", p[1], p[3])]
    
def p_type(p):
    """type : INT 
            | BOOL """
    p[0] = p[1]
def p_vardecl(p):
    """ vardecl : type decllist SCOLON vardecl 
                | empty""" 
    p[0] = Node()
    if len(p) == 5:
        for i in range(len(p[2])):
            p[2][i].type = p[1] # set the type of the variable
        p[0] = [*p[2], *p[4]]
    else:
        p[0] = []
    

def p_decllist(p):
    """ decllist : ID COLON decllist 
                 | ID """
    if len(p) == 4:
        p[0] = [DeclareNode("", p[1]), *p[3]]
    else:
        p[0] = [DeclareNode("", p[1])]
    


def p_boolexpr(p):
    """boolexp : expression EQ expression
                | expression GT expression
                | expression GE expression
                | expression LT expression
                | expression LE expression   
                | ODD expression"""
    p[0] = ExpressionNode(p[2], p[1], p[3])


def p_statement_begin(p):
    "statement : BEGIN statementlist END"
    p[0] = BeginNode(p[2])
    
def p_statement_assign(p):
    "statement : ID ASSIGN expression"
    p[0] = AssignNode(p[1], p[3])
def p_statement_if(p):
    """statement : IF boolexp THEN statement
                 | IF boolexp THEN statement ELSE statement"""
    if len(p) == 5:
        p[0] = IfNode(condition=p[2], body=p[4])
    else:
        p[0] = IfNode(condition=p[2], body=p[4], else_body=p[6])
    
def p_statement_while(p):
    "statement : WHILE boolexp DO statement"
    p[0] = WhileNode(condition=p[2], body=p[4])
def p_statement_call(p):
    "statement : CALL ID"
    p[0] = CallProcedureNode(p[1])
def p_statement_in(p):
    "statement : IN ID"
    p[0] = InNode(p[2])
def p_statement_out(p):
    """statement : OUT expression
                | OUT boolexp"""
    p[0] = OutNode(p[2])
def p_statement_empty(p):
    """ statement : empty"""
    p[0] = []
    
def p_proc(p):
    "proc : PROC ID SCOLON block SCOLON"
    p[0] = DeclareProcedureNode(p[2])
    p[0].add_children(p[4])

def p_procdecl(p):
    """procdecl : proc procdecl
                | empty
                """
    if len(p) == 3:
        p[0] = [p[1], *p[2]]
    else:
        p[0] = []

def p_statement_list(p):
    """ statementlist : statement SCOLON statementlist 
                      | statement"""
    if len(p) == 4:
        p[0] = [p[1], *p[3]]
    else:
        p[0] = [p[1]]
parser = yacc.yacc(debug=True)


s = """
const FIN = 5, SUMA = 1, RESTA = 2, MULT = 3, DIV = 4;
int x, j;
int y;
procedure suma;
 begin
    z := z + x;
  end;
begin
    fin := 0;
    while fin = 0 do
    begin
        in op;
        in y;
        if op = SUMA
            then call suma
        else if op = RESTA
            then call resta
        else if op = MULT
            then call MULT
        else if op = DIV
            then call DIV
        else
            fin := 1;
    end;
end;"""

result = parser.parse(s)
print(result)