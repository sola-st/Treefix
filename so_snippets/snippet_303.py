# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value
# ✅ test multiple variables against single value using tuple

from l3.Runtime import _l_
if 'a' in (a, b, c):
    _l_(1069)

    print('value is stored in at least one of the variables')
    _l_(1068)

# ---------------------------------------------------------

# ✅ test multiple variables against single value using tuple

if 'a' in {a, b, c}:
    _l_(1071)

    print('value is stored in at least one of the variables')
    _l_(1070)

# ---------------------------------------------------------


# ✅ test multiple variables against single value (OR operator chaining)
if a == 'a' or b == 'a' or c == 'a':
    _l_(1073)

    print('value is stored in at least one of the variables')
    _l_(1072)

