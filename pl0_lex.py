from ply import lex
from argparse import ArgumentParser

states = (("inblock", "inclusive"),)

kw = {
    "INT": "int",
    "IF": "if",
    "ELSE": "else",
    "IN": "in",
    "OUT": "out",
    "DO": "do",
    "THEN": "then",
    "PROC": "procedure",
    "BEGIN": "begin",
    "END": "end",
    "CALL": "call",
    "CONST": "const",
    "ODD": "odd",
    "WHILE": "while",
    "BOOL": "bool"
}
reserved = {v: k for k, v in kw.items()}

tokens = [
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV",
    "SCOLON",
    "ASSIGN",
    "EQ",
    "GT",
    "GE",
    "LE",
    "LT",
    "ID",
    "NUMBER",
    "COLON",
    "LPAREN",
    "RPAREN",
    *reserved.values(),
]
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIV = r"/"
t_SCOLON = r";"
t_ASSIGN = r":="
t_EQ = r"="
t_GE = r">="
t_GT = r">"
t_LT = r"<"
t_LE = r"<="

t_NUMBER = r"\d+"
t_COLON = r","


def t_inblock_ID(t):
    r"[a-zA-Z][_|\w]*"
    if t.value == kw["PROC"]:
        raise lex.LexError(
            f"Lex error cannot have a procedure definition inside a block at line {t.lexer.lineno}"
        )
    return t_ID(t)


def t_ID(t):
    r"[a-zA-Z][_|\w]*"
    if t.value == kw["BEGIN"]:
        if t.lexer.depth > 7:
            raise ValueError("Lex error, can't have more than depth 7")
        t.lexer.depth += 1
        t.lexer.push_state("inblock")
    if t.value == kw["END"]:
        t.lexer.depth -= 1
        t.lexer.pop_state()
    t.type = reserved.get(t.value, "ID")
    # print(t)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r"\r?\n"
    t.lexer.lineno += 1


t_ignore = " \t"


example = """
const FIN = 5, SUMA = 1, RESTA = 2, MULT = 3, DIV = 4;
int op;
int fin;
int y;
int x;
        procedure a ;
            begin
                x := x + y;
                out x;
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
end;
"""
lexer = lex.lex()
lexer.depth = 0


def analyse(input_file):
    # with open(input_file, encoding="ascii") as file:
    # lexer.input(file.read())
    lexer.input(example)
    while True:
        t = lexer.token()
        if not t:
            break
        print(t)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Lexical Analyzer PL/0", usage="pl0_lex in_file -o output_file"
    )
    # parser.add_argument('input_file')
    # parser.add_argument("-o", '--output')
    args = parser.parse_args()
    # analyse(args.input_file, args.output)
    analyse("")
