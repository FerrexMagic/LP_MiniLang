from typing import Dict



class Symbol:
    def __init__(self, name, type, value=None, is_constant=False, is_procedure=False):
        self.name = name
        self.type = type
        self.value = value
        self.is_procedure = is_procedure
        self.is_constant = is_constant
        self.is_var = (not is_constant) and (not is_procedure)

    def __str__(self):
        return f"Symbol({self.name}, {self.type}, {self.value})"

    def __repr__(self):
        return str(self)
    
class SymbolTable:
    def __init__(self, parent: "SymbolTable" = None):
        self._symbols: Dict[str, Symbol] = {}
        self.parent = parent

    def get_symbol(self, name, max_depth=float('inf')):
        sym = self._symbols.get(name)
        if max_depth > 0 and sym is None and self.parent:
            return self.parent.get_symbol(name, max_depth=max_depth - 1)
        
        return sym
        
    def add_symbol(self, symbol: Symbol):
        self._symbols[symbol.name] = symbol


class Scope:
    def __init__(self):
        self._symbols = SymbolTable()
    def stack(self):
        self._symbols = SymbolTable(self._symbols)
    def unstack(self):
        self._symbols = self._symbols.parent
    def get_symbol(self, name):
        return self._symbols.get_symbol(name)
    def add_symbol(self, symbol):
        self._symbols.add_symbol(symbol)
    def contains(self, id, max_depth=float('inf')):
        
        return self._symbols.get_symbol(id, max_depth=max_depth) is not None
