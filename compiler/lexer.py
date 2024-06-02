# lexer.py

import re

# Definimos los tokens básicos
tokens = [
    ('PROGRAM_ID', r'PROGRAM-ID\.'), 
    ('MAIN', r'MAIN:'),
    ('DISPLAY', r'DISPLAY'),
    ('STRING', r'"[^"]*"'),
    ('END', r'END'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.')  # Cualquier otro carácter
]

# Función para generar tokens
def tokenize(code):
    token_specification = [(kind, re.compile(pattern)) for kind, pattern in tokens]
    line_num = 1
    line_start = 0
    pos = 0
    while pos < len(code):
        match = None
        for kind, pattern in token_specification:
            match = pattern.match(code, pos)
            if match:
                text = match.group(0)
                if kind == 'NEWLINE':
                    line_start = pos
                    line_num += 1
                elif kind == 'SKIP':
                    pass
                elif kind != 'MISMATCH':
                    yield kind, text
                else:
                    raise RuntimeError(f'{text!r} unexpected on line {line_num}')
                break
        if not match:
            raise RuntimeError(f'{code[pos]!r} unexpected on line {line_num}')
        else:
            pos = match.end(0)

if __name__ == "__main__":
    # Test del lexer con un ejemplo simple
    code = '''PROGRAM-ID. HelloWorld.
MAIN:
    DISPLAY "Hola Mundo"
    END'''
    for token in tokenize(code):
        print(token)
