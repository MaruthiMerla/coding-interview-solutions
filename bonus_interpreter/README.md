interpreter = MiniInterpreter()

# Arithmetic
print(interpreter.evaluate("(+ 1 2 3)"))  # 6

# Variable binding
print(interpreter.evaluate("(let x 5 y 10 (* x y))"))  # 50

# If condition
print(interpreter.evaluate("(if (== 5 5) 'yes' 'no')"))  # 'yes'