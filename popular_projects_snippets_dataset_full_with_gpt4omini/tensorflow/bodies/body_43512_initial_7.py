from inspect import getfullargspec # pragma: no cover
from types import MethodType # pragma: no cover

def mock_function(param1, param2='default', *args, **kwargs): pass # pragma: no cover
func_and_positional = (mock_function, 1, 2) # pragma: no cover
named = {'param2': 'overridden'} # pragma: no cover
ismethod = lambda obj: isinstance(obj, MethodType) # pragma: no cover

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
_l_(5395)
positional = func_and_positional[1:]
_l_(5396)
argspec = getfullargspec(func)
_l_(5397)
call_args = named.copy()
_l_(5398)
this = getattr(func, 'im_self', None) or getattr(func, '__self__', None)
_l_(5399)
if ismethod(func) and this:
    _l_(5401)

    positional = (this,) + positional
    _l_(5400)
remaining_positionals = [arg for arg in argspec.args if arg not in call_args]
_l_(5402)
call_args.update(dict(zip(remaining_positionals, positional)))
_l_(5403)
default_count = 0 if not argspec.defaults else len(argspec.defaults)
_l_(5404)
if default_count:
    _l_(5408)

    for arg, value in zip(argspec.args[-default_count:], argspec.defaults):
        _l_(5407)

        if arg not in call_args:
            _l_(5406)

            call_args[arg] = value
            _l_(5405)
if argspec.kwonlydefaults is not None:
    _l_(5412)

    for k, v in argspec.kwonlydefaults.items():
        _l_(5411)

        if k not in call_args:
            _l_(5410)

            call_args[k] = v
            _l_(5409)
aux = call_args
_l_(5413)
exit(aux)
