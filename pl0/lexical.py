from ply import lex


kw = {
    "INT": "int",
    "IF": "if",
    "ELSE": "else",
    "IN": "in",
    "OUT": "out",
    "DO": "do",
    "THEN": "then",
    "END": "end",
    "CALL": "call",
    "CONST": "const",
    "ODD": "odd",
    "WHILE": "while",
    "BOOL": "bool",
    "RETURN": "return",
    "SUBROUTINE": "subroutine",
    "STRING": "string",
    "AND": "and",
    "OR": "or",
    "NOT": "not",
    "TRUE": "true",
    "FALSE": "false",
    "PRINT": "print",
    "INPUT": "input",
    "VOID": "void",
}
reserved = {}
for k, v in kw.items():
    reserved[v] = k
    reserved[v.upper()] = k
    


tokens = [
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV",
    "SCOLON",
    "ASSIGN",
    "EQ",
    "GT",
    "LT",
    "NEQ",
    "ID",
    "NUMBER",
    "COLON",
    "LPAREN",
    "RPAREN",
    "PALABRA",
    *reserved.values(),
]

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIV = r"/"
t_SCOLON = r";"
t_EQ = r"=="
t_ASSIGN = r"="
t_GT = r">"
t_LT = r"<"
t_NEQ = r"!="
t_NUMBER = r"\d+"
t_COLON = r","


def t_COMMENT(t):
    r"\#[^\n]*"
    pass

def t_ID(t):
    r"[a-zA-Z][_|\w]*"
    t.type = reserved.get(t.value, "ID")
    return t

def t_PALABRA(t):
    r'\"[^\"]*\"'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r"\r?\n"
    t.lexer.lineno += 1


t_ignore = " \t"


lexer = lex.lex()
lexer.depth = 0


