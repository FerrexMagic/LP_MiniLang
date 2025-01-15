from typing import List

from pl0.context import Scope
from .base import Node, ExpressionNode, IdNode, NumberNode, StringNode
from .statements import AssignNode, DoNode, CallProcedureNode, IfNode, InNode, OutNode, StatementNode, WhileNode
from .declarations import DeclareNode, DeclareProcedureNode, ConstNode
from llvmlite import ir
class BlockNode(Node):

    def __init__(self, constants: List[ConstNode], variables: List[DeclareNode], procedures: List[DeclareProcedureNode], statement: StatementNode) -> None:
        super().__init__()
        self.constants = constants
        self.variables = variables
        self.procedures = procedures
        self.children = [*constants, *variables, *procedures, statement]
    def validate(self, scope: Scope) -> bool:
        scope.stack()
        return True
