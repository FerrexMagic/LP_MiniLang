from argparse import ArgumentParser
from functools import partial
import json

from pl0.parse import parser
from pl0.lexical import lexer
from pl0.semantic_analysis import semantic_analysis
stages = ["preprocess", "lex", "parse", "semantics", "codegen"]

def analyse(lexer, data: str) -> str:
    output = ""
    lexer.input(data)
    for tok in lexer:
        output += " " + tok.value
    return output

    
actions = {
    "preprocess": partial(analyse, lexer),
    "lex": partial(analyse, lexer),
    "parse": parser.parse,
    "semantics": semantic_analysis,
    
}


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Compiler PL/0", usage="pl0 input_file -a action -o output_file"
    )
    parser.add_argument("-a", "--action", choices=stages, default="codegen")
    parser.add_argument('input_file')
    parser.add_argument("-o", '--output', required=False, default=None)
    args = parser.parse_args()
    action = args.action
    file = args.input_file
    output = args.output
    file_contents = open(file, "r", encoding="utf-8").read()
    action_stage = stages.index(action)

    if stages.index("preprocess") < action_stage:
        file_contents = actions["preprocess"](file_contents)
        if output:
            with open(output+".pre", "w", encoding="utf-8") as f:
                f.write(file_contents)

    if stages.index("lex") <= action_stage:
        file_contents = actions["lex"](file_contents)
        if output:
            with open(output+".lex", "w", encoding="utf-8") as f:
                f.write(file_contents)

    if stages.index("parse") <= action_stage:
        tree = actions["parse"](file_contents)
        if output:
            with open(output+".ast", "w", encoding="utf-8") as f:
                json.dump(tree, f, default=lambda o: o.__dict__, indent=4)

    if stages.index("semantics") <= action_stage:
        actions["semantics"](tree)

    if stages.index("codegen") <= action_stage:
        pass

