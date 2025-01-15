from typing import List
from pl0.context import Scope
from pl0.nodes import BlockNode
from pl0.nodes.base import Node

def semantic_analysis(tree: BlockNode):
    scope = Scope()
    analyze(tree, depth=0, scope=scope)
    
def analyze(nodes: List[Node] | Node, depth: int, scope: Scope):
    """
    Recorre los nodos del AST en profundidad para buscar errores semánticos.
    Parameters:
    - nodes (List[Node] | Node): Lista de nodos o un solo nodo.
    - depth (int): La profundidad del nodo actual.
    - scope (Scope): El ámbito actual.
    """
    if not isinstance(nodes, list):
        nodes = [nodes]
        #print("  " * depth, nodes[0].__getattribute__("__class__").__name__)
    for node in nodes:
        if isinstance(node, list):
            break
        print("  " * depth, node.__getattribute__("__class__").__name__)
        node.validate(scope)            
        for child in node.children:
            analyze(nodes=child, depth=depth + 1, scope=scope)
        if isinstance(node, BlockNode):
            scope.unstack()