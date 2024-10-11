class Mock: # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        # Custom subtract method suitable for strings # pragma: no cover
        try: # pragma: no cover
            # Attempt numeric subtraction if possible # pragma: no cover
            return int(self) - int(other) # pragma: no cover
        except ValueError: # pragma: no cover
            # Fallback to string operation: remove occurrences of 'other' in 'self' # pragma: no cover
            return self.replace(other, '') # pragma: no cover
mock_instance = Mock() # pragma: no cover
some_function = lambda x: x # pragma: no cover

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

