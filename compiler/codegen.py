# codegen.py

def generate_js(node):
    if node.type == 'PROGRAM':
        return f'// {node.value}\n' + generate_js(node.children[0])
    elif node.type == 'MAIN':
        return 'function main() {\n' + ''.join(generate_js(child) for child in node.children) + '\n}\nmain();'
    elif node.type == 'DISPLAY':
        return f'console.log("{node.value}");\n'
    else:
        raise ValueError(f'Unknown node type {node.type}')

if __name__ == "__main__":
    # Test del generador de código con un ejemplo simple
    from lexer import tokenize
    from parser import parse
    code = '''PROGRAM-ID. HelloWorld.
MAIN:
    DISPLAY "Hola Mundo"
    END'''
    tokens = list(tokenize(code))
    ast = parse(tokens)
    js_code = generate_js(ast)
    print(js_code)
