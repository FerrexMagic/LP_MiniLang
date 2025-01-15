import abc
from typing import List

from pl0.exceptions import SemanticException
from pl0.context import Scope
class Node(abc.ABC):
    """
    Abstract base class representing a node.

    This class serves as a blueprint for creating various types of nodes. 
    It is intended to be subclassed, and the subclasses should implement 
    the abstract methods defined in this class.

    Attributes:
        children (list): The children nodes of the node.

    Methods:
        (To be defined by subclasses)
    """
    def __init__(self):
        """
        Construct a node.

        This method constructs a node with the given symbol table.

        Args:
            None
        Returns:
            None
        """
        self.children = []
    def validate(self, scope: Scope) -> bool:
        """
        Abstract method to validate the node.

        This method should be implemented by subclasses to validate the node.

        Args:
            scope (list): The current scope.

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        return True
    def add_children(self, children: List["Node"]|"Node") -> None:
        """
        Add children nodes to the node.
        """
        if isinstance(children, (list, tuple,)):
            self.children.extend(children)
        else:
            self.children.append(children)

class ExpressionNode(Node):

    def __init__(self, operator: str, left: Node, right: Node) -> None:
        super().__init__()
        self.operator = operator
        self.left = left
        self.right = right
        self.children = [left, right]
    
    def validate(self, scope):
        
        tipo = [self.getClass(self.left), self.getClass(self.right)]

        if tipo[0] == "IdNode":
            tipo[0] = {
                "string": "StringNode",
                "int": "NumberNode",
                "bool": "BoolNode"
            }.get(self.getTipo(scope, self.left), None)
        if tipo[1] == "IdNode":
            tipo[1] = {
                "string": "StringNode",
                "int": "NumberNode",
                "bool": "BoolNode"
            }.get(self.getTipo(scope, self.right), None)

        

        matriz = {
            ("StringNode", "StringNode"): ["+", "-", "*", "/", "==", "!=", ">", "<", "&&", "||", "!"],
            ("StringNode", "NumberNode"): ["+", "-"],
            ("StringNode", "BoolNode"): [],
            ("NumberNode", "StringNode"): [],
            ("NumberNode", "NumberNode"): ["+", "-", "*", "/", "==", "!=", ">", "<", "&&", "||", "!"],
            ("NumberNode", "BoolNode"): [],
        }

        operadores_permitidos = matriz.get((tipo[0], tipo[1]), [])
        
        if self.operator not in operadores_permitidos:
            raise SemanticException(f"Operacion invalida {self.operator} entre {tipo[0]} y {tipo[1]}")
        return True


    def getTipo(self, scope: Scope, val: Node):
        return scope.get_symbol(val.identifier).type

    def getClass(self, val:Node):
        return val.__class__.__name__
     


class NumberNode(Node):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

class StringNode(Node):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

class BoolNode(Node):
    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = value

class IdNode(Node):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.identifier = identifier

    def validate(self, scope: Scope) -> bool:
        sym = scope.get_symbol(self.identifier)
        if not sym:
            raise SemanticException(f"Variable {self.identifier} no esta declarada")
        return True