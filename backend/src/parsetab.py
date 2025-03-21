
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARE AT AVAILABLE BOOK BOOKINGS BOOKING_ID CANCEL COMMA CONFIRM DATE DOUBLE_QUOTE EQUAL_SIGN FOR FROM ID_STRING IN INTEGER IS LBRACKET LIST LOCATION LPAREN NAME ON PAY PERIOD QUESTION_SIGN RBRACKET RESERVATION RESOURCE RPAREN SCHEDULE SINGLE_QUOTE SPACE TO WHAT\n    statement : listing_statements\n              | booking_statements\n              | reservation_statements\n    \n    listing_statements : listing_statement\n                       | query_listing_statements\n    \n    listing_statement : LIST name_list BOOKINGS PERIOD\n    \n    query_listing_statements : query_listing_statement\n                             | query_schedule_listing_statement\n    \n    query_listing_statement : WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN\n                            | WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN\n    \n    query_schedule_listing_statement : WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN\n                                     | WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN\n    \n    booking_statements : booking_statement\n                       | schedule_booking_statement\n    \n    booking_statement : BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD\n    \n    schedule_booking_statement : BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD\n    \n    booking_list : INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE\n                 | INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE AND INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE\n                 | INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE COMMA booking_list\n    \n    location : LOCATION\n             | DOUBLE_QUOTE LOCATION DOUBLE_QUOTE TO DOUBLE_QUOTE LOCATION DOUBLE_QUOTE\n    \n    date : DATE\n         | DOUBLE_QUOTE DATE DOUBLE_QUOTE TO DOUBLE_QUOTE DATE DOUBLE_QUOTE\n    \n    name_list : LPAREN name_group RPAREN\n              | LPAREN name_group RPAREN AND LPAREN name_group RPAREN\n              | LPAREN name_group RPAREN COMMA name_list\n    \n    name_group : names\n               | names AND names\n               | names COMMA name_group\n    \n    names : NAME\n          | NAME SPACE NAME\n    \n    reservation_statements : confirm_statement\n                           | cancel_statement\n                           | pay_statement\n    \n    confirm_statement : CONFIRM RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD\n    \n    cancel_statement : CANCEL RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD\n    \n    pay_statement : PAY RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD\n    '
    
_lr_action_items = {'LIST':([0,],[12,]),'BOOK':([0,],[15,]),'CONFIRM':([0,],[16,]),'CANCEL':([0,],[17,]),'PAY':([0,],[18,]),'WHAT':([0,],[19,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,14,40,102,103,104,152,154,155,160,162,167,],[0,-1,-2,-3,-4,-5,-13,-14,-32,-33,-34,-7,-8,-6,-35,-36,-37,-9,-11,-12,-15,-16,-10,]),'LPAREN':([12,52,53,148,151,],[21,64,21,21,21,]),'INTEGER':([15,67,68,],[23,77,23,]),'RESERVATION':([16,17,18,],[24,25,26,]),'SINGLE_QUOTE':([19,23,28,33,38,46,51,57,59,60,61,77,79,80,81,83,101,106,],[27,34,39,45,50,58,63,66,69,70,71,89,90,91,92,94,112,114,]),'IS':([19,],[28,]),'BOOKINGS':([20,41,65,86,],[29,-24,-26,-25,]),'NAME':([21,42,43,44,64,],[32,32,32,56,32,]),'FOR':([22,24,25,26,58,72,78,112,140,143,],[33,35,36,37,-17,83,-19,-18,148,151,]),'RESOURCE':([27,34,39,45,89,94,],[38,46,51,57,101,106,]),'PERIOD':([29,41,65,86,90,91,92,156,158,],[40,-24,-26,-25,102,103,104,160,162,]),'RPAREN':([30,31,32,54,55,56,74,],[41,-27,-30,-28,-29,-31,86,]),'AND':([31,32,41,56,58,],[42,-30,52,-31,67,]),'COMMA':([31,32,41,56,58,],[43,-30,53,-31,68,]),'SPACE':([32,],[44,]),'BOOKING_ID':([35,36,37,],[47,48,49,]),'EQUAL_SIGN':([47,48,49,],[59,60,61,]),'ARE':([50,],[62,]),'AVAILABLE':([62,],[72,]),'SCHEDULE':([63,],[73,]),'AT':([66,73,],[75,85,]),'FROM':([66,73,],[76,84,]),'ID_STRING':([69,70,71,],[79,80,81,]),'IN':([72,114,],[82,121,]),'LBRACKET':([75,76,82,84,85,117,119,120,121,122,123,153,],[87,88,93,95,96,124,126,127,128,129,130,159,]),'LOCATION':([87,88,93,95,96,99,128,134,],[98,98,98,98,98,110,98,142,]),'DOUBLE_QUOTE':([87,88,93,95,96,110,124,125,126,127,128,129,130,141,142,157,159,164,],[99,99,99,99,99,118,133,134,133,133,99,133,133,149,150,161,133,166,]),'RBRACKET':([97,98,100,105,107,108,131,132,135,136,137,138,139,150,163,166,],[109,-20,111,113,115,116,140,-22,143,144,145,146,147,-21,165,-23,]),'ON':([109,111,113,115,116,145,],[117,119,120,122,123,153,]),'TO':([118,149,],[125,157,]),'DATE':([124,126,127,129,130,133,159,161,],[132,132,132,132,132,141,132,164,]),'QUESTION_SIGN':([144,146,147,165,],[152,154,155,167,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'listing_statements':([0,],[2,]),'booking_statements':([0,],[3,]),'reservation_statements':([0,],[4,]),'listing_statement':([0,],[5,]),'query_listing_statements':([0,],[6,]),'booking_statement':([0,],[7,]),'schedule_booking_statement':([0,],[8,]),'confirm_statement':([0,],[9,]),'cancel_statement':([0,],[10,]),'pay_statement':([0,],[11,]),'query_listing_statement':([0,],[13,]),'query_schedule_listing_statement':([0,],[14,]),'name_list':([12,53,148,151,],[20,65,156,158,]),'booking_list':([15,68,],[22,78,]),'name_group':([21,43,64,],[30,55,74,]),'names':([21,42,43,64,],[31,54,31,31,]),'location':([87,88,93,95,96,128,],[97,100,105,107,108,137,]),'date':([124,126,127,129,130,159,],[131,135,136,138,139,163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> listing_statements','statement',1,'p_statement','parser_v1.py',6),
  ('statement -> booking_statements','statement',1,'p_statement','parser_v1.py',7),
  ('statement -> reservation_statements','statement',1,'p_statement','parser_v1.py',8),
  ('listing_statements -> listing_statement','listing_statements',1,'p_listing_statements','parser_v1.py',14),
  ('listing_statements -> query_listing_statements','listing_statements',1,'p_listing_statements','parser_v1.py',15),
  ('listing_statement -> LIST name_list BOOKINGS PERIOD','listing_statement',4,'p_listing_statement','parser_v1.py',21),
  ('query_listing_statements -> query_listing_statement','query_listing_statements',1,'p_query_listing_statements','parser_v1.py',26),
  ('query_listing_statements -> query_schedule_listing_statement','query_listing_statements',1,'p_query_listing_statements','parser_v1.py',27),
  ('query_listing_statement -> WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN','query_listing_statement',15,'p_query_listing_statement','parser_v1.py',33),
  ('query_listing_statement -> WHAT SINGLE_QUOTE RESOURCE SINGLE_QUOTE ARE AVAILABLE FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE IN LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN','query_listing_statement',19,'p_query_listing_statement','parser_v1.py',34),
  ('query_schedule_listing_statement -> WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN','query_schedule_listing_statement',15,'p_query_schedule_listing_statement','parser_v1.py',39),
  ('query_schedule_listing_statement -> WHAT IS SINGLE_QUOTE RESOURCE SINGLE_QUOTE SCHEDULE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET QUESTION_SIGN','query_schedule_listing_statement',15,'p_query_schedule_listing_statement','parser_v1.py',40),
  ('booking_statements -> booking_statement','booking_statements',1,'p_booking_statements','parser_v1.py',45),
  ('booking_statements -> schedule_booking_statement','booking_statements',1,'p_booking_statements','parser_v1.py',46),
  ('booking_statement -> BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE AT LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD','booking_statement',17,'p_booking_statement','parser_v1.py',52),
  ('schedule_booking_statement -> BOOK booking_list FOR SINGLE_QUOTE RESOURCE SINGLE_QUOTE FROM LBRACKET location RBRACKET ON LBRACKET date RBRACKET FOR name_list PERIOD','schedule_booking_statement',17,'p_schedule_booking_statement','parser_v1.py',57),
  ('booking_list -> INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE','booking_list',4,'p_booking_list','parser_v1.py',62),
  ('booking_list -> INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE AND INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE','booking_list',9,'p_booking_list','parser_v1.py',63),
  ('booking_list -> INTEGER SINGLE_QUOTE RESOURCE SINGLE_QUOTE COMMA booking_list','booking_list',6,'p_booking_list','parser_v1.py',64),
  ('location -> LOCATION','location',1,'p_location','parser_v1.py',69),
  ('location -> DOUBLE_QUOTE LOCATION DOUBLE_QUOTE TO DOUBLE_QUOTE LOCATION DOUBLE_QUOTE','location',7,'p_location','parser_v1.py',70),
  ('date -> DATE','date',1,'p_date','parser_v1.py',75),
  ('date -> DOUBLE_QUOTE DATE DOUBLE_QUOTE TO DOUBLE_QUOTE DATE DOUBLE_QUOTE','date',7,'p_date','parser_v1.py',76),
  ('name_list -> LPAREN name_group RPAREN','name_list',3,'p_name_list','parser_v1.py',81),
  ('name_list -> LPAREN name_group RPAREN AND LPAREN name_group RPAREN','name_list',7,'p_name_list','parser_v1.py',82),
  ('name_list -> LPAREN name_group RPAREN COMMA name_list','name_list',5,'p_name_list','parser_v1.py',83),
  ('name_group -> names','name_group',1,'p_name_group','parser_v1.py',88),
  ('name_group -> names AND names','name_group',3,'p_name_group','parser_v1.py',89),
  ('name_group -> names COMMA name_group','name_group',3,'p_name_group','parser_v1.py',90),
  ('names -> NAME','names',1,'p_names','parser_v1.py',95),
  ('names -> NAME SPACE NAME','names',3,'p_names','parser_v1.py',96),
  ('reservation_statements -> confirm_statement','reservation_statements',1,'p_reservation_statements','parser_v1.py',101),
  ('reservation_statements -> cancel_statement','reservation_statements',1,'p_reservation_statements','parser_v1.py',102),
  ('reservation_statements -> pay_statement','reservation_statements',1,'p_reservation_statements','parser_v1.py',103),
  ('confirm_statement -> CONFIRM RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD','confirm_statement',9,'p_confirm_statement','parser_v1.py',109),
  ('cancel_statement -> CANCEL RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD','cancel_statement',9,'p_cancel_statement','parser_v1.py',114),
  ('pay_statement -> PAY RESERVATION FOR BOOKING_ID EQUAL_SIGN SINGLE_QUOTE ID_STRING SINGLE_QUOTE PERIOD','pay_statement',9,'p_pay_statement','parser_v1.py',119),
]
