from typing import Any # pragma: no cover

class Mock:# pragma: no cover
    def some_function(self, arg: Any):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
mock_instance = Mock()# pragma: no cover
some_function = mock_instance.some_function # pragma: no cover

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

