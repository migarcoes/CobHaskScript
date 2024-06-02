# main.py

from lexer import tokenize
from parser import parse
from codegen import generate_js

def compile_chj_to_js(code):
    tokens = list(tokenize(code))
    ast = parse(tokens)
    js_code = generate_js(ast)
    return js_code

if __name__ == "__main__":
    # Código fuente en CobHaskScript
    code = '''PROGRAM-ID. HelloWorld.
MAIN:
    DISPLAY "Hola Mundo"
    END'''
    
    # Compilar a JavaScript
    js_code = compile_chj_to_js(code)
    print("Generated JavaScript code:")
    print(js_code)
