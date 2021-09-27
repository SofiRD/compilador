# Construyendo el analizador léxico

import ply.yacc as yacc
from lexico_compilador import tokens

def p_init(t) :
    'init : programa'
    t[0] = t[1]
    
def p_programa(t):
    'programa : PROGRAM ID PUNTOYCOMA progvars group_functions bloque'
    t[0] = t[1]

def p_group_functions(t):
    """group_functions : dec_funcion group_functions 
	| empty"""
    t[0] = t[1]

def p_dec_funcion(t):
    'dec_funcion : FUNCTION PARAB progvars PARCERR ID bloque RETURN expresion PUNTOYCOMA'
    t[0] = t[1]

def p_uso_funcion(t):
    'uso_funcion : FUNCTION ID PARAB progvars PARCERR PUNTOYCOMA'
    t[0] = t[1]

def p_progvars(t):
    """progvars : vars 
                | empty"""
    t[0] = t[1]
    
def p_vars(t):
    'vars : VAR ID ids DOSPUNTOS tipo PUNTOYCOMA mvars'
    t[0] = t[1]

def p_ids(t):
    """ids : COMA ID 
        | empty"""
    t[0] = t[1]

def p_mvars(t):
    """mvars : ID ids DOSPUNTOS tipo PUNTOYCOMA mvars
        | empty"""
    t[0] = t[1]
    
def p_tipo(t):
    """tipo : INT
        | FLOAT"""
    t[0] = t[1]
    
def p_bloque(t):
    'bloque : BRAQUETAB estatutos BRAQUETCERR'
    t[0] = t[1]
    
def p_estatutos(t):
    """estatutos : estatuto estatutos
        | empty"""
    t[0] = t[1]
    
def p_estatuto(t):
    """estatuto : asignacion
        | condicion
        | escritura"""
    t[0] = t[1]

def p_asignacion(t):
    'asignacion : ID EQUAL expresion PUNTOYCOMA'
    t[0] = t[1]

def p_escritura(t):
    'escritura : PRINT PARAB pescritura mescritura PARCERR PUNTOYCOMA'
    t[0] = t[1]

def p_pescritura(t):
    """pescritura : expresion
        | STRING"""
    t[0] = t[1]
    
def p_mescritura(t):
    """mescritura : COMA pescritura mescritura
        | empty"""
    t[0] = t[1]
    
def p_expresion(t):
    'expresion : exp posexp'
    t[0] = t[1]
    
def p_posexp(t):
    """posexp : symexp exp
        | empty"""
    t[0] = t[1]
    
def p_symexp(t):
    """symexp : MAYORK
        | MENORK may"""
    t[0] = t[1]
    
def p_may(t):
    """may : MAYORK
        | empty"""
    t[0] = t[1]
        
def p_exp(t):
    'exp : termino mexp'
    t[0] = t[1]
    
def p_mexp(t):
    """mexp : sumres exp
        | empty"""
    t[0] = t[1]

def p_sumres(t):
    """sumres : MAS
        | MENOS"""
    t[0] = t[1]
    
def p_termino(t):
    'termino : factor mtermino'
    t[0] = t[1]
    
def p_mtermino(t):
    """mtermino : multdiv termino
        | empty"""
    t[0] = t[1]
    
def p_multdiv(t):
    """multdiv : MULT
        | DIV"""
    t[0] = t[1]
    
def p_factor(t):
    """factor : PARAB expresion PARCERR
        | sumresvac varcte"""
    t[0] = t[1]
    
def p_sumresvac(t):
    """sumresvac : sumres
        | empty"""
    t[0] = t[1]
        
def p_condicion(t):
    'condicion : IF PARAB expresion PARCERR bloque elsee PUNTOYCOMA'
    t[0] = t[1]
    
def p_elsee(t):
    'elsee : ELSE bloque'
    t[0] = t[1]
    
def p_varcte(t):
    """varcte : ID
        | FLOATI
        | ENTERO
	| uso_funcion"""
    t[0] = t[1]
    
def p_empty(t):
    'empty :'
    pass

def p_error(p):
    print("Syntax error in input!")
    
    
parser = yacc.yacc()


f = open("proguno.txt", "r")
s = f.read()
result = parser.parse(s)
if result:
    print("Si funciona!")