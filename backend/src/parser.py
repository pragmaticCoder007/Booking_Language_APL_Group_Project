from ply import yacc
from lexer import *

def p_statement(p):
    """
    statement : event_listing
              | commute_listing
              | booking_listing
              | event_booking
              | commute_booking
              | confirm_statement
              | cancel_statement
              | pay_statement
    """

def p_event_listing(p):
    """
    event_listing : WHAT EVENTS ARE AVAILABLE IN LBRACKET LOCATION RBRACKET ON DOUBLE_QUOTE DATE DOUBLE_QUOTE QUESTION_SIGN
                  | WHAT DOUBLE_QUOTE RESOURCE DOUBLE_QUOTE EVENTS ARE AVAILABLE IN LBRACKET LOCATION RBRACKET ON DOUBLE_QUOTE DATE DOUBLE_QUOTE QUESTION_SIGN
    """

def p_commute_listing(p):
    """
    commute_listing : WHAT IS DOUBLE_QUOTE RESOURCE DOUBLE_QUOTE SCHEDULE FROM LBRACKET destination RBRACKET ON DOUBLE_QUOTE DATE DOUBLE_QUOTE QUESTION_SIGN
    """

def p_booking_listing(p):
    """
    booking_listing : LIST MY BOOKINGS PERIOD
    """

def p_event_booking(p):
    """
    event_booking : BOOK category_for_booking TICKET FOR DOUBLE_QUOTE RESOURCE DOUBLE_QUOTE ON DOUBLE_QUOTE DATE DOUBLE_QUOTE FOR booking_for PERIOD
    """

def p_commute_booking(p):
    """
    commute_booking : BOOK category_for_booking TICKET FOR DOUBLE_QUOTE RESOURCE DOUBLE_QUOTE FROM LBRACKET destination RBRACKET ON DOUBLE_QUOTE DATE DOUBLE_QUOTE FOR booking_for PERIOD
    """

def p_confirm_statement(p):
    """
    confirm_statement : CONFIRM RESERVATION FOR BOOKING_ID EQUAL_SIGN DOUBLE_QUOTE ID_STRING DOUBLE_QUOTE PERIOD
    """

def p_cancel_statement(p):
    """
    cancel_statement : CANCEL RESERVATION FOR BOOKING_ID EQUAL_SIGN DOUBLE_QUOTE ID_STRING DOUBLE_QUOTE PERIOD
    """


def p_pay_statement(p):
    """
    pay_statement : PAY RESERVATION FOR BOOKING_ID EQUAL_SIGN DOUBLE_QUOTE ID_STRING DOUBLE_QUOTE PERIOD
    """

def p_destination(p):
    """
    destination : LOCATION
                | DOUBLE_QUOTE LOCATION DOUBLE_QUOTE TO DOUBLE_QUOTE LOCATION DOUBLE_QUOTE
    """

def p_category_for_booking(p):
    """
    category_for_booking : INTEGER SINGLE_QUOTE CATEGORY SINGLE_QUOTE
                         | INTEGER SINGLE_QUOTE CATEGORY SINGLE_QUOTE AND INTEGER SINGLE_QUOTE CATEGORY SINGLE_QUOTE
                         | INTEGER SINGLE_QUOTE CATEGORY SINGLE_QUOTE COMMA category_for_booking
    """

def p_booking_for(p):
    """
    booking_for : LPAREN names_for_booking RPAREN
                | LPAREN names_for_booking RPAREN AND LPAREN names_for_booking RPAREN
                | LPAREN names_for_booking RPAREN COMMA booking_for
    """

def p_names_for_booking(p):
    """
    names_for_booking : names
                      | names AND names
                      | names COMMA names_for_booking
    """

def p_names(p):
    """
    names : NAME
          | NAME SPACE NAME
    """

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
    if result is None:
        print("Parsing successful!\n")
    else:
        print("Parsing failed!\n")

# Test cases
test_inputs = [
    # ✅ 1. Complex Event Listings
    'What "$football" events are available in [@New York] on "2025-07-21"?',
    'What events are available in [@Los Angeles] on "2025-12-31"?',

    # ✅ 2. Complex Commute Listings
    'What is "$Knutsford Express" schedule from ["@Kingston" to "@Montego Bay"] on "2025-06-10"?',
    'What is "$Delta Airlines" schedule from ["@JFK" to "@LAX"] on "2025-06-15"?',

    # ✅ 3. Complex Event Bookings
    'Book 2 \'+bleachers\' and 1 \'+vip\' ticket for "$Reggae Sumfest" on "2025-07-18" for (Alice, Bob) and (Charlie).',
    'Book 3 \'+vip\' ticket for "$Champions League Final" on "2025-05-25" for (John Doe, Jane Doe, Alex Smith).',

    # ✅ 4. Complex Commute Bookings
    'Book 1 \'+economy\' and 2 \'+first class\' ticket for "$Jet Blue" from ["@JFK" to "@Miami"] on "2025-09-05" for (Mike) and (Sarah, James).',
    'Book 2 \'+standard\' and 3 \'+vip\' ticket for "$Knutsford Express" from ["@Montego Bay" to "@Ocho Rios"] on "2025-11-20" for (Chris, Emma) and (Daniel, Olivia, Sophia).',

    # ✅ 5. Complex Confirmations
    'Confirm reservation for bookingID = "#ABC123".',
    'Confirm reservation for bookingID = "#XYZ789".',

    # ✅ 6. Complex Cancellations
    'Cancel reservation for bookingID = "#12345A".',
    'Cancel reservation for bookingID = "#ZZ9900".',

    # ✅ 7. Complex Payments
    'Pay reservation for bookingID = "#P00123".',
    'Pay reservation for bookingID = "#X99999".',

    # ❌ 8. Invalid Inputs (Expected to fail)
    'What events are available on "2025-07-21" in [New York]?',  # Incorrect word order
    'Book 3 vip tickets for "Reggae Sumfest" on 2025-07-18 for (Alice, Bob, Charlie).',  # Missing quotes around 'vip'
    'Confirm reservation for booking ID = "5904".',  # Incorrect token (space between BOOKING and ID)
    'Book 2 \'bleachers\' ticket "Reggae Sumfest" on "2025-07-18" for (Alice).',  # Missing "for" keyword
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