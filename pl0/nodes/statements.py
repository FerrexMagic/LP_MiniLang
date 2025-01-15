from typing import List, Optional
from pl0.nodes.base import ExpressionNode, Node
from pl0.context import Scope
from pl0.nodes.declarations import ConstNode
from pl0.exceptions import SemanticException

class StatementNode(Node):
    ... 
class DoNode(StatementNode):
    def __init__(self, statements: List[StatementNode]) -> None:
        super().__init__()
        self.statements = statements
        self.children = statements

class IfNode(StatementNode):
    """
    Class representing an if node.
    Attributes:
        condition (Node): The condition node to be evaluated.
        body (List[Node]): The list of nodes to be executed in the loop body.
        else_body (List[Node]): The list of nodes to be executed in the else body.

        Methods:
            validate: Validate the node.
    """
    def __init__(self, condition: Node, body: StatementNode, else_body: Optional[StatementNode]=None) -> None:
        """
        Construct an if node.

        This method constructs an if node with the given condition, body, and else body.

        Args:
            condition (Node): The condition node to be evaluated.
            body (List[Node]): The list of nodes to be executed in the if body.
            else_body (List[Node]): The list of nodes to be executed in the else body.

        Returns:
            None
        """
        super().__init__()
        self.condition = condition
        self.body = body
        self.else_body = else_body
        if else_body:
            self.children = [condition, body, else_body]
        else:
            self.children = [condition, body]
class WhileNode(StatementNode):
    """
    Class representing a while node.
    Attributes:
        condition (Node): The condition node to be evaluated.
        body (List[Node]): The list of nodes to be executed in the loop body.

    Methods:
        validate: Validate the node.
    """
    def __init__(self, condition: Node, body: StatementNode) -> None:
        """
        Construct a while node.

        This method constructs a while node with the given condition and body.

        Args:
            condition (Node): The condition node to be evaluated.
            body (List[Node]): The list of nodes to be executed in the loop body.

        Returns:
            None
        """
        super().__init__()
        self.condition = condition
        self.body = body
        self.children = [condition, body]


class AssignNode(StatementNode):
    """
    Class representing an assignment node.

    This class represents an assignment node in the abstract syntax tree.

    Attributes:
        identifier (str): The identifier to which the value is assigned.
        value (int): The value to be assigned to the identifier.

    Methods:
        validate: Validate the node.
    """
    def __init__(self, identifier: str, value: int) -> None:
        """
        Construct an assignment node.

        This method constructs an assignment node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self.identifier = identifier
        self.value = value
        self.children = [value]
    
    def __init__(self, identifier: str, value: str) -> None:
        """
        Construct an assignment node.

        This method constructs an assignment node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self.identifier = identifier
        self.value = value
        self.children = [value]

    def __init__(self, identifier: str, value: str) -> None:
        """
        Construct an assignment node.

        This method constructs an assignment node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self.identifier = identifier
        self.value = value
        self.children = [value]

    def validate(self, scope: Scope) -> bool:
        """
        Validate the node.

        This method validates the assignment node, an assignment node is valid if the variable has been declared before in the current scope
        or in an outer scope.

        Args:
            None

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        if scope.contains(self.identifier):
            if scope._symbols.get_symbol(self.identifier).is_constant:
                raise SemanticException(f"Variable '{self.identifier}' is a constant and cannot be assigned a new value")
            return True
        else:
            raise SemanticException(f"Variable or procedure '{self.identifier}' not found in the current scope")  

class ReturnNode(StatementNode):
    def __init__(self, value: StatementNode) -> None:
        super().__init__()
        self.value = value
        self.children = [value]

    def validate(self, scope: Scope) -> bool:
        if not self.value:
            return False 
        return self.value.validate(scope)

class PrintNode(StatementNode):
    def __init__(self, value: StatementNode) -> None:
        super().__init__()
        self.value = value
        self.children = [value]
    
    def validate(self, scope: Scope) -> bool:
        if not self.value:
            return False 
        return self.value.validate(scope)

class CallProcedureNode(StatementNode):
    """
    Class representing a procedure call node.

    This class represents a procedure call node in the abstract syntax tree.

    Attributes:
        identifier (str): The identifier to which the value is assigned.
        value (int): The value to be assigned to the identifier.

    Methods:
        validate: Validate the node.
    """
    def __init__(self, identifier: str) -> None:
        """
        Construct a procedure call node.

        This method constructs a procedure call node with the given identifier 
        and value.

        Args:
            identifier (str): The identifier to which the value is assigned.
            value (int): The value to be assigned to the identifier.

        Returns:
            None
        """
        super().__init__()
        self.identifier = identifier

    def validate(self, scope: Scope) -> bool:
        """
        Validate the node.

        This method validates the procedure call node, a procedure call node is valid if the procedure has been declared before in the current scope
        or in an outer scope.

        Args:
            None

        Returns:
            bool: True if the node is valid, False otherwise.
        """
        if scope.contains(self.identifier):
            return True
        else:
            raise SemanticException(f"Procedure '{self.identifier}' not found in the current scope")

class InNode(StatementNode):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.identifier = identifier

        raise NotImplementedError("InNode validate method not implemented")
    
class OutNode(StatementNode):
    def __init__(self, value: ExpressionNode) -> None:
        super().__init__()
        self.value = value
        self.children = [value]
    
class PrintNode(StatementNode):
    def __init__(self, value: ExpressionNode) -> None:
        super().__init__()
        self.value = value
        self.children = [value]

class InputNode(StatementNode):
    def __init__(self, value: ExpressionNode) -> None:
        super().__init__()
        self.value = value
        self.children = [value]
    def validate(self, scope: Scope) -> bool:
        return True

