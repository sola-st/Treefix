from typing import Callable, TypeVar # pragma: no cover

T_template_test = TypeVar('T_template_test', bound=Callable) # pragma: no cover
class MockApp: # pragma: no cover
    def add_template_test(self, f: T_template_test, name=None): # pragma: no cover
        print(f'Test {name} registered.') # pragma: no cover
app = MockApp() # pragma: no cover
name = 'is_prime' # pragma: no cover
self = app # pragma: no cover
def decorator(f: T_template_test) -> T_template_test:  # Defining the decorator function # pragma: no cover
    self.add_template_test(f, name=name)  # This line should execute # pragma: no cover
    aux = f # pragma: no cover
aux = decorator # pragma: no cover

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
    _l_(6522)

    self.add_template_test(f, name=name)
    _l_(6520)
    aux = f
    _l_(6521)
    exit(aux)
aux = decorator
_l_(6523)

exit(aux)
