from pl0.nodes.base import Node, NumberNode, StringNode, BoolNode
from pl0.context import Scope, Symbol
from pl0.exceptions import SemanticException
from llvmlite import ir
class ConstNode(Node):
    """
    Class representing a constant node.

    This class represents a constant node in the abstract syntax tree.

    Attributes:
        identifier (str): The identifier to which the value is assigned.
        value (int): The value to be assigned to the identifier.

    Methods:
        validate: Validate the node.
    """
    def __init__(self, _type: str, identifier: str, value: int) -> None:
        """
        Construct a constant node.

        This method constructs a constant node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self._type = _type
        self.identifier = identifier
        self.value = value

    def validate(self, scope: Scope) -> bool:
        """
        Validate the node.

        This method validates the constant node, a constant node is valid if the variable has not been declared before in the current scope
        note that the variable can be declared in an outer scope and used in an inner scope.

        Args:
            None

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        if scope.contains(self.identifier):
            raise SemanticException(f"Constante '{self.identifier}' ya esta declarada en este ambito.")
        
        if (self._type == "int" and isinstance(self.value, NumberNode) or 
            self._type == "string" and isinstance(self.value, StringNode) or 
            self._type == "bool" and isinstance(self.value, BoolNode)):
            scope.add_symbol(Symbol(self.identifier, self._type,is_constant=True))
            return True
        else:
            raise SemanticException(f"El tipo de la constante '{self.identifier}' no coincide con el valor asignado '{self._type}'.")
    
        
class DeclareNode(Node):
    """
    Class representing a declaration node.

    This class represents an assignment node in the abstract syntax tree.

    Attributes:
        identifier (str): The identifier to which the value is assigned.
        value (int): The value to be assigned to the identifier.

    Methods:
        validate: Validate the node.
    """
    def __init__(self, _type: str, identifier: str) -> None:
        """
        Construct an declare node.

        This method constructs an declaration node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self._type = _type
        self.identifier = identifier
        

    def validate(self, scope: Scope) -> bool:
        """
        Validate the node.

        This method validates the declare node, an declare node is valid if the variable has not been declared before in the current scope
        note that the variable can be declared in an outer scope and used in an inner scope.

        Args:
            None

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        
        if scope.contains(self.identifier) and not scope.get_symbol(self.identifier).is_procedure:
            raise SemanticException(f"Variable '{self.identifier}' ya esta declarada en este ambito.")
        scope.add_symbol(Symbol(self.identifier, self._type))
        return True

        
class DeclareProcedureNode(Node):
    
    """
    Class representing a procedure declaration node.

    This class represents a procedure declaration node in the abstract syntax tree.

    Attributes:
        identifier (str): The identifier to which the value is assigned.
        value (int): The value to be assigned to the identifier.

    Methods:
        validate: Validate the node.
        identifier=p[3], return_type=p[2], block=p[8], return_value=p[10]
    """
    def __init__(self, identifier: str, return_type:type, block: Node, param: Node) -> None:
        from pl0.nodes import BlockNode
        """
        Construct a subroutine declaration node.

        This method constructs a subroutine declaration node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self._type = "subroutine"
        self.identifier = identifier
        self.return_type = return_type
        self.param = param
        self.children = [param, block]

        

    def validate(self, scope: Scope) -> bool:
        """
        Validate the node.

        This method validates the procedure declaration node, a procedure declaration node is valid if the procedure has not been declared before in the current scope
        note that the procedure can be declared in an outer scope and used in an inner scope.

        Args:
            None

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        if scope.contains(self.identifier):
            raise SemanticException(f"Procedimiento '{self.identifier}' ya esta declarado en este ambito.")
        scope.add_symbol(Symbol(self.identifier, self._type, is_procedure=True))
        return True

