from ply import yacc
from lexer import *

def p_statement(p):
    """
    statement : listing_statements
              | booking_statements
              | reservation_statements
    """
    p[0] = p[1]

def p_listing_statements(p):
    """
    listing_statements : listing_statement
                       | query_listing_statements
    """
    p[0] = p[1]

def p_listing_statement(p):
    """
    listing_statement : LIST name_list BOOKINGS PERIOD
    """
    p[0] = ("list_bookings", p[2])

def p_query_listing_statements(p):
    """
    query_listing_statements : query_listing_statement
                             | query_schedule_listing_statement
    """
    p[0] = p[1]

def p_query_listing_statement(p):
    """
    query_listing_statement : WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN
                            | WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN
    """
    if len(p) == 16:  # First rule: No specific resource
        p[0] = ("query_listing", p[3], None, p[9], p[13])
    else:  # Second rule: Specific resource
        p[0] = ("query_listing", p[3], p[9], p[13], p[17])

def p_query_schedule_listing_statement(p):
    """
    query_schedule_listing_statement : WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN
                                     | WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN
    """
    p[0] = ("query_schedule_listing", p[4], p[7], p[9], p[13])

def p_booking_statements(p):
    """
    booking_statements : booking_statement
                       | schedule_booking_statement
    """
    p[0] = p[1]

def p_booking_statement(p):
    """
    booking_statement : BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD
    """
    p[0] = ("booking", p[2], p[5], p[9], p[13], p[16])

def p_schedule_booking_statement(p):
    """
    schedule_booking_statement : BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD
    """
    p[0] = ("scheduled_booking", p[2], p[5], p[9], p[13], p[16])

def p_booking_list(p):
    """
    booking_list : INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE
                 | INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE AND INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE
                 | INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE COMMA booking_list
    """
    if len(p) == 5:
        p[0] = [(p[1], p[3])]
    elif len(p) == 9:
        p[0] = [(p[1], p[3]), (p[6], p[8])]
    else:
        p[0] = [(p[1], p[3])] + [(p[6], p[8])]

def p_location(p):
    """
    location : LOCATION
             | DOUBLE_QUOTE LOCATION DOUBLE_QUOTE TO DOUBLE_QUOTE LOCATION DOUBLE_QUOTE
    """
    if len(p) == 2:
        p[0] = p[1]  # Single location
    else:
        p[0] = (p[2], p[6])  # Travel between two locations

def p_date(p):
    """
    date : DATE
         | DOUBLE_QUOTE DATE DOUBLE_QUOTE TO DOUBLE_QUOTE DATE DOUBLE_QUOTE
    """
    if len(p) == 2:
        p[0] = p[1]  # Single date
    else:
        p[0] = (p[2], p[6])  # Date range

def p_name_list(p):
    """
    name_list : LPAREN name_group RPAREN
              | LPAREN name_group RPAREN AND LPAREN name_group RPAREN
              | LPAREN name_group RPAREN COMMA name_list
    """
    if len(p) == 4:
        p[0] = p[2]  # Just a single name group
    elif len(p) == 8:
        p[0] = ("name_list", p[2], p[6])  # Two groups
    else:
        p[0] = ("name_list", p[2], p[5])  # Group with comma-separated values

def p_name_group(p):
    """
    name_group : names
               | names AND names
               | names COMMA name_group
    """
    if len(p) == 2:
        p[0] = [p[1]]  # Single name
    elif len(p) == 4 and p[2] == "AND":
        p[0] = [p[1]] + [p[3]]  # List of two names
    else:
        p[0] = [p[1]] + [p[3]]  # List of names with comma

def p_names(p):
    """
    names : NAME
          | NAME SPACE NAME
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + " " + p[3]

def p_reservation_statements(p):
    """
    reservation_statements : confirm_statement
                           | cancel_statement
                           | pay_statement
    """
    p[0] = p[1]

def p_confirm_statement(p):
    """
    confirm_statement : CONFIRM RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD
    """
    p[0] = ("confirm_reservation", p[7])

def p_cancel_statement(p):
    """
    cancel_statement : CANCEL RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD
    """
    p[0] = ("cancel_reservation", p[7])

def p_pay_statement(p):
    """
    pay_statement : PAY RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD
    """
    p[0] = ("pay_reservation", p[7])


# Error handling rule
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at end of input")

# Build the parser
parser = yacc.yacc()

# Function to test the parser
def test_parser(input_text):
    result = parser.parse(input_text)
    if result:
        print("Parsing results...")
        print("Results:")
        print(result)
        print("Parsing successful!\n")
    else:
        print("DEBUG: Parser returned None or an empty structure.")
        print("Type of result:", type(result))
        print("Parsing failed!\n")

# Test cases
test_inputs = [
    "What '$rooms' are available for '$Sandals Resort' in [@Montego Bay] on [2025-12-05]?",
    "What '$villas' are available in [@Negril] on [\"2026-01-10\" to \"2026-01-15\"]?",
    "What is '$shuttle' schedule from [\"@Ocho Rios\" to \"@Kingston\"] on [2025-08-20]?",

    "Book 2 '$deluxe suite' and 1 '$penthouse suite' for '$Grand Hotel' at [@Kingston] on [2025-09-10] for (Alice) and (Bob and Charlie).",
    "Book 1 '$VIP pass' and 3 '$standard pass' for '$Ultra Festival' at [@Miami] on [2025-07-01] for (Eve) and (Oscar and Leo).",

    "Book 1 '$business class seat' for '$JetBlue Flight' from [\"@JFK\" to \"@LAX\"] on [2025-05-20] for (Daniel).",
    "Book 2 '$executive suite' for '$Royal Caribbean Cruise' from [\"@Florida\" to \"@Bahamas\"] on [2025-06-15] for (Sophia and Michael).",

    "Confirm reservation for bookingID = '#A12345'.",
    "Cancel reservation for bookingID = '#B67890'.",
    "Pay reservation for bookingID = '#C54321'.",
]

for test in test_inputs:
    print(f"\nTesting: {test}")
    print("Tokens:")
    try:
        lexer.input(test)

        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

    except SyntaxError as e:
        print(e)

    test_parser(test)