# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Creates a new function instance."""
if self._unbound_factory is None:
    raise ValueError('call create first')

factory_code = self._unbound_factory.__code__
factory_freevars = factory_code.co_freevars
closure_map = dict(zip(self._freevars, closure))
factory_closure = tuple(
    closure_map[name] for name in factory_code.co_freevars)
if len(factory_closure) != len(closure):
    raise ValueError(
        'closure mismatch, requested {}, but source function had {}'.format(
            self._freevars, factory_freevars))

bound_factory = types.FunctionType(
    code=factory_code,
    globals=globals_,
    name=self._name,
    argdefs=(),
    closure=factory_closure)

# The lint override is a false positive.
new_fn = bound_factory(**self._extra_locals)  # pylint:disable=not-callable

if defaults:
    new_fn.__defaults__ = defaults
if kwdefaults:
    new_fn.__kwdefaults__ = kwdefaults

exit(new_fn)
