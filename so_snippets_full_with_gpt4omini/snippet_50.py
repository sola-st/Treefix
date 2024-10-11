# Extracted from https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
def is_float(value):
  if value is None:
      return False
  try:
      float(value)
      return True
  except:
      return False

val                   is_float(val) Note
--------------------  ----------   --------------------------------
""                    False        Blank string
"127"                 True         Passed string
True                  True         Pure sweet Truth
"True"                False        Vile contemptible lie
False                 True         So false it becomes true
"123.456"             True         Decimal
"      -127    "      True         Spaces trimmed
"\t\n12\r\n"          True         whitespace ignored
"NaN"                 True         Not a number
"NaNanananaBATMAN"    False        I am Batman
"-iNF"                True         Negative infinity
"123.E4"              True         Exponential notation
".1"                  True         mantissa only
"1_2_3.4"             False        Underscores not allowed
"12 34"               False        Spaces not allowed on interior
"1,234"               False        Commas gtfo
u'\x30'               True         Unicode is fine.
"NULL"                False        Null is not special
0x3fade               True         Hexadecimal
"6e7777777777777"     True         Shrunk to infinity
"1.797693e+308"       True         This is max value
"infinity"            True         Same as inf
"infinityandBEYOND"   False        Extra characters wreck it
"12.34.56"            False        Only one dot allowed
u'四'                 False        Japanese '4' is not a float.
"#56"                 False        Pound sign
"56%"                 False        Percent of what?
"0E0"                 True         Exponential, move dot 0 places
0**0                  True         0___0  Exponentiation
"-5e-5"               True         Raise to a negative number
"+1e1"                True         Plus is OK with exponent
"+1e1^5"              False        Fancy exponent not interpreted
"+1e1.3"              False        No decimals in exponent
"-+1"                 False        Make up your mind
"(1)"                 False        Parenthesis is bad

