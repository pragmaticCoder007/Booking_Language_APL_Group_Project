from ply import lex

reserved_words = {
#---------Event Listing---------#
    'What': 'WHAT',
    'events': 'EVENTS',
    'available': 'AVAILABLE',
    'schedule': 'SCHEDULE',

#---------Booking---------# 
    'Book': 'BOOK',
    'ticket': 'TICKET',
    'tickets': 'TICKETS',
    'list': 'LIST',
    'my': 'MY',
    'bookings': 'BOOKINGS',

#---------Confirm---------#
    'Confirm': 'CONFIRM',

#---------Cancel---------#
    'Cancel': 'CANCEL',

#---------Payment---------#
    'Pay': 'PAY',

    'reservation': 'RESERVATION',
    'bookingID': 'BOOKING_ID',

    'for': 'FOR',
    'is': 'IS',
    'are': 'ARE',
    'in': 'IN',
    'from': 'FROM',
    'on': 'ON',
    'to': 'TO',
    'and': 'AND', 
}

tokens = [
    'NAME',
    'RESOURCE',
    'LOCATION',
    'CATEGORY',

    'DATE',
    'INTEGER',
    'ID_STRING',

    'SPACE',
    'COMMA',
    'PERIOD',
    'EQUAL_SIGN',
    'SINGLE_QUOTE',
    'DOUBLE_QUOTE',
    'QUESTION_SIGN',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
] + list(reserved_words.values())

#Regular Expression Rules

#Symbols
t_SPACE = r'\s'
t_COMMA = r'\,'
t_PERIOD = r'\.'
t_EQUAL_SIGN = r'\='
t_SINGLE_QUOTE = r'\''
t_DOUBLE_QUOTE = r'\"'
t_QUESTION_SIGN = r'\?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Token Definitions
def t_RESOURCE(t):
    r'[$][A-Za-z]+(?:\s[A-Za-z]+)*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

def t_LOCATION(t):
    r'[@][A-Za-z]+(?:\s[A-Za-z]+)*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t


def t_CATEGORY(t):
    r'[+][A-Za-z]+(?:\s[A-Za-z]+)*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

def t_NAME(t):
    r'[A-Za-z]+'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

""" def t_LAST_NAME(t):
    r'[A-Za-z]+'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t """

def t_DATE(t):
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID_STRING(t):
    r'[#][A-Za-z0-9]+'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Handle New Line as an Error
def t_newline(t):
    r'\n+'
    raise SyntaxError(f"Error: New lines are not allowed. Found at position {t.lexpos}")

# Error Handling for Other Invalid Characters
def t_error(t):
    raise SyntaxError(f"Illegal character '{t.value[0]}' at position {t.lexpos}")

# Build the Lexer
lexer = lex.lex()

# Testing the Lexer:
""" data = '''to 123 314 () = " ' What 2 available 2025-01-01
'''

try:
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

except SyntaxError as e:
    print(e)
 """