# codegen.py

def generate_js(node):
    if node.type == 'PROGRAM':
        return f'// {node.value}\n' + generate_js(node.children[0])
    elif node.type == 'MAIN':
        return 'function main() {\n' + ''.join(generate_js(child) for child in node.children) + '\n}\nmain();'
    elif node.type == 'DISPLAY':
        return f'console.log("{node.value}");\n'
    elif node.type == 'INPUT':
        return f'let {node.value} = prompt("{node.value}: ");\n'
    elif node.type == 'ASSIGN':
        return f'let {node.value} = {generate_js(node.children[0])};\n'
    elif node.type == 'CALC':
        return f'{generate_js(node.children[0])}'
    elif node.type == 'EXPRESSION':
        operand1 = generate_js(node.children[0])
        operator = generate_js(node.children[1])
        operand2 = generate_js(node.children[2])
        return f'({operand1} {operator} {operand2})'
    elif node.type == 'OPERAND':
        return f'{node.value}'
    elif node.type == 'OPERATOR':
        return {
            '"+"': '+',
            '"-"': '-',
            '"*"': '*',
            '"/"': '/'
        }[node.value]
    else:
        raise ValueError(f'Unknown node type {node.type}')

if __name__ == "__main__":
    # Test del generador de código con un ejemplo simple
    from lexer import tokenize
    from parser import parse
    code = '''PROGRAM-ID. BasicCalculator.
MAIN:
    DISPLAY "Ingrese el primer número: "
    INPUT num1
    DISPLAY "Ingrese la operación (+, -, *, /): "
    INPUT op
    DISPLAY "Ingrese el segundo número: "
    INPUT num2
    result = CALC(num1, op, num2)
    DISPLAY "El resultado es: "
    DISPLAY result
    END'''
    tokens = list(tokenize(code))
    ast = parse(tokens)
    js_code = generate_js(ast)
    print(js_code)
