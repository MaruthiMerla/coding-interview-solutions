class MiniInterpreter:
    def __init__(self):
        self.variables = {}
    
    def evaluate(self, expr):
        if not expr.startswith('('):
            return self._parse_atom(expr)
        
        expr = expr[1:-1].strip()  # Remove outer parentheses
        tokens = self._tokenize(expr)
        
        if not tokens:
            raise ValueError("Empty expression")
        
        if tokens[0] == 'let':
            return self._eval_let(tokens[1:])
        elif tokens[0] == 'if':
            return self._eval_if(tokens[1:])
        else:
            return self._eval_expression(tokens)
    
    def _tokenize(self, expr):
        tokens = []
        current = []
        paren_level = 0
        
        for char in expr:
            if char == '(':
                paren_level += 1
                current.append(char)
            elif char == ')':
                paren_level -= 1
                current.append(char)
            elif char.isspace() and paren_level == 0:
                if current:
                    tokens.append(''.join(current))
                    current = []
            else:
                current.append(char)
        
        if current:
            tokens.append(''.join(current))
        
        return tokens
    
    def _parse_atom(self, atom):
        if atom in self.variables:
            return self.variables[atom]
        try:
            return int(atom)
        except ValueError:
            try:
                return float(atom)
            except ValueError:
                return atom  # Treat as string (e.g., variable name)
    
    def _eval_let(self, tokens):
        if len(tokens) % 2 != 1:
            raise ValueError("let requires odd number of tokens")
        
        for i in range(0, len(tokens)-1, 2):
            var_name = tokens[i]
            value = self.evaluate(tokens[i+1])
            self.variables[var_name] = value
        
        return self.evaluate(tokens[-1])
    
    def _eval_if(self, tokens):
        if len(tokens) != 3:
            raise ValueError("if requires 3 tokens: condition then else")
        
        condition = self.evaluate(tokens[0])
        if condition:
            return self.evaluate(tokens[1])
        else:
            return self.evaluate(tokens[2])
    
    def _eval_expression(self, tokens):
        if len(tokens) < 2:
            raise ValueError("Expression too short")
        
        operator = tokens[0]
        operands = [self.evaluate(token) for token in tokens[1:]]
        
        if operator == '+':
            return sum(operands)
        elif operator == '-':
            return operands[0] - sum(operands[1:])
        elif operator == '*':
            result = 1
            for num in operands:
                result *= num
            return result
        elif operator == '/':
            return operands[0] / operands[1]
        elif operator == '>':
            return operands[0] > operands[1]
        elif operator == '<':
            return operands[0] < operands[1]
        elif operator == '>=':
            return operands[0] >= operands[1]
        elif operator == '<=':
            return operands[0] <= operands[1]
        elif operator == '==':
            return operands[0] == operands[1]
        else:
            raise ValueError(f"Unknown operator: {operator}")