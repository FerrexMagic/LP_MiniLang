from typing import Dict, List, Tuple

SymbolTable = Dict[Tuple[str, str], Tuple[str, int, bool]]  # (scope, identifier) -> (type, value, is_var)
Scope = List[str]