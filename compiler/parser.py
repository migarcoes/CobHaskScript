# parser.py

class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

def parse(tokens):
    tokens = iter(tokens)
    current_token = next(tokens, None)

    def eat(expected_type):
        nonlocal current_token
        if current_token and current_token[0] == expected_type:
            current_token = next(tokens, None)
        else:
            raise SyntaxError(f'Expected {expected_type} but got {current_token}')

    def parse_program():
        node = Node('PROGRAM')
        eat('PROGRAM_ID')
        node.value = current_token[1].strip()
        eat('STRING')
        node.children.append(parse_main())
        return node

    def parse_main():
        node = Node('MAIN')
        eat('MAIN')
        while current_token and current_token[0] != 'END':
            node.children.append(parse_statement())
        eat('END')
        return node

    def parse_statement():
        if current_token[0] == 'DISPLAY':
            node = Node('DISPLAY')
            eat('DISPLAY')
            node.value = current_token[1].strip('"')
            eat('STRING')
            return node
        else:
            raise SyntaxError(f'Unexpected token {current_token}')

    return parse_program()

if __name__ == "__main__":
    # Test del parser con un ejemplo simple
    from lexer import tokenize
    code = '''PROGRAM-ID. HelloWorld.
MAIN:
    DISPLAY "Hola Mundo"
    END'''
    tokens = list(tokenize(code))
    ast = parse(tokens)
    print(ast)
