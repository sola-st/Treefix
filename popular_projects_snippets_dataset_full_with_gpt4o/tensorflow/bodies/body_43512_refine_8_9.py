from inspect import getfullargspec # pragma: no cover

func_and_positional = [lambda x, y: x + y, 1, 2] # pragma: no cover
named = {'z': 3} # pragma: no cover
ismethod = lambda x: False # pragma: no cover

from inspect import getfullargspec # pragma: no cover
from types import MethodType # pragma: no cover

func_and_positional = [lambda x, y, z=3: (x, y, z), 1, 2] # pragma: no cover
named = {} # pragma: no cover
ismethod = lambda func: isinstance(func, MethodType) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
from l3.Runtime import _l_
"""TFDecorator-aware replacement for inspect.getcallargs.

  Args:
    *func_and_positional: A callable, possibly decorated, followed by any
      positional arguments that would be passed to `func`.
    **named: The named argument dictionary that would be passed to `func`.

  Returns:
    A dictionary mapping `func`'s named arguments to the values they would
    receive if `func(*positional, **named)` were called.

  `getcallargs` will use the argspec from the outermost decorator that provides
  it. If no attached decorators modify argspec, the final unwrapped target's
  argspec will be used.
  """
func = func_and_positional[0]
_l_(17141)
positional = func_and_positional[1:]
_l_(17142)
argspec = getfullargspec(func)
_l_(17143)
call_args = named.copy()
_l_(17144)
this = getattr(func, 'im_self', None) or getattr(func, '__self__', None)
_l_(17145)
if ismethod(func) and this:
    _l_(17147)

    positional = (this,) + positional
    _l_(17146)
remaining_positionals = [arg for arg in argspec.args if arg not in call_args]
_l_(17148)
call_args.update(dict(zip(remaining_positionals, positional)))
_l_(17149)
default_count = 0 if not argspec.defaults else len(argspec.defaults)
_l_(17150)
if default_count:
    _l_(17154)

    for arg, value in zip(argspec.args[-default_count:], argspec.defaults):
        _l_(17153)

        if arg not in call_args:
            _l_(17152)

            call_args[arg] = value
            _l_(17151)
if argspec.kwonlydefaults is not None:
    _l_(17158)

    for k, v in argspec.kwonlydefaults.items():
        _l_(17157)

        if k not in call_args:
            _l_(17156)

            call_args[k] = v
            _l_(17155)
aux = call_args
_l_(17159)
exit(aux)
