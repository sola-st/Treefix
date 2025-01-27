# Extracted from https://stackoverflow.com/questions/23177439/how-to-check-if-a-dictionary-is-empty
test_dict = {}

if not test_dict:
    print "Dict is Empty"


if not bool(test_dict):
    print "Dict is Empty"


if len(test_dict) == 0:
    print "Dict is Empty"

