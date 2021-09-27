# Construyendo el analizador léxico
import ply.lex as lex


reserved_tokens = {
    'program' : 'PROGRAM',
    'int' : 'INT',
    'float' : 'FLOAT',
    'if' : 'IF',
    'else' : 'ELSE',
    'var' : 'VAR',
    'print' : 'PRINT',
    'function' : 'FUNCTION',
    'return' : 'RETURN'
}

tokens  = [
    'ID',
    'PUNTOYCOMA',
    'BRAQUETAB',
    'BRAQUETCERR',
    'COMA',
    'DOSPUNTOS',
    'MAYORK',
    'MENORK',
    'STRING',
    'PARAB',
    'PARCERR',
    'MAS',
    'MENOS',
    'MULT',
    'DIV',
    'ENTERO',
    'FLOATI',
    'EQUAL'
] + list(reserved_tokens.values())

# Tokens
t_PUNTOYCOMA   = r';'
t_BRAQUETAB   = r'{'
t_BRAQUETCERR    = r'}'
t_COMA    = r','
t_MAYORK     = r'>'
t_MENORK       = r'<'
t_STRING       = r'\".*?\"'
t_PARAB  = r'\('
t_PARCERR    = r'\)'
t_MAS    = r'\+'
t_MENOS    = r'-'
t_MULT  = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_DOSPUNTOS = r':'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_tokens.keys():
        t.type = reserved_tokens[t.value]
    return t


def t_FLOATI(t):
    r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float overflow %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer overflow %d", t.value)
        t.value = 0
    return t





"""
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 
"""

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_eof(t):
    pass
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

