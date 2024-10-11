def some_function(value): # pragma: no cover
    return value # pragma: no cover
def eval_expression(expression): # pragma: no cover
    return eval(expression.replace('-', '+')) # pragma: no cover
a = some_function(eval_expression('1' + '2' + '3' + '-' + '4')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python
from l3.Runtime import _l_
a = some_function(
    '1' + '2' + '3' - '4')
_l_(13265)

a = '1'   \
    + '2' \
    + '3' \
    - '4'
_l_(13266)

