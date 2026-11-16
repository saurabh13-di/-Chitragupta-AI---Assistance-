import ast, operator, math
OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.FloorDiv:operator.floordiv,ast.Mod:operator.mod,ast.Pow:operator.pow,ast.USub:operator.neg,ast.UAdd:operator.pos}
def calculate(expression):
    expression=expression.strip().replace('^','**')
    if not expression or len(expression)>100: raise ValueError('Enter a valid arithmetic expression.')
    def visit(n):
        if isinstance(n,ast.Expression): return visit(n.body)
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)): return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in OPS:
            a,b=visit(n.left),visit(n.right)
            if isinstance(n.op,ast.Pow) and abs(b)>10: raise ValueError('Exponent is too large.')
            result=OPS[type(n.op)](a,b)
            if isinstance(result,complex) or not math.isfinite(result): raise ValueError('Result outside supported range.')
            return result
        if isinstance(n,ast.UnaryOp) and type(n.op) in OPS: return OPS[type(n.op)](visit(n.operand))
        raise ValueError('Use numbers, +, -, *, /, //, %, ** and parentheses only.')
    try: return visit(ast.parse(expression,mode='eval'))
    except ZeroDivisionError: raise ValueError('Cannot divide by zero.')
    except (SyntaxError,OverflowError): raise ValueError('Invalid calculation.')
