import typing as t # pragma: no cover
from jinja2 import Environment, BaseLoader, TemplateNotFound # pragma: no cover

class MockLoader(BaseLoader): # pragma: no cover
    def get_source(self, environment, template): # pragma: no cover
        if template == 'exists': # pragma: no cover
            return ('<template>', None, lambda: True) # pragma: no cover
        raise TemplateNotFound(template) # pragma: no cover
class MockEnvironment(Environment): # pragma: no cover
    pass # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_iter_loaders': lambda self, template: [(None, MockLoader())], # pragma: no cover
    'app': None # pragma: no cover
})() # pragma: no cover
template = 'exists' # pragma: no cover
environment = MockEnvironment() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
attempts = []
_l_(22878)
rv: t.Optional[t.Tuple[str, t.Optional[str], t.Optional[t.Callable[[], bool]]]]
_l_(22879)
trv: t.Optional[
    t.Tuple[str, t.Optional[str], t.Optional[t.Callable[[], bool]]]
] = None
_l_(22880)

for srcobj, loader in self._iter_loaders(template):
    _l_(22888)

    try:
        _l_(22886)

        rv = loader.get_source(environment, template)
        _l_(22881)
        if trv is None:
            _l_(22883)

            trv = rv
            _l_(22882)
    except TemplateNotFound:
        _l_(22885)

        rv = None
        _l_(22884)
    attempts.append((loader, srcobj, rv))
    _l_(22887)
try:
    from .debughelpers import explain_template_loading_attempts
    _l_(22890)

except ImportError:
    pass

explain_template_loading_attempts(self.app, template, attempts)
_l_(22891)

if trv is not None:
    _l_(22893)

    aux = trv
    _l_(22892)
    exit(aux)
raise TemplateNotFound(template)
_l_(22894)
