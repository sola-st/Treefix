import math # pragma: no cover
from typing import Callable # pragma: no cover

T_template_test = Callable[[int], bool] # pragma: no cover
class Mock: # pragma: no cover
    def add_template_test(self, f: T_template_test, name: str = None): # pragma: no cover
        print(f'Template test added with name: {name or f.__name__}') # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
name = 'test_name' # pragma: no cover
def example_test(n: int) -> bool: # pragma: no cover
    return n % 2 == 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""A decorator that is used to register custom template test.
        You can specify a name for the test, otherwise the function
        name will be used. Example::

          @app.template_test()
          def is_prime(n):
              if n == 2:
                  return True
              for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
                  if n % i == 0:
                      return False
              return True

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_test) -> T_template_test:
    _l_(18026)

    self.add_template_test(f, name=name)
    _l_(18024)
    aux = f
    _l_(18025)
    exit(aux)
aux = decorator
_l_(18027)

exit(aux)
