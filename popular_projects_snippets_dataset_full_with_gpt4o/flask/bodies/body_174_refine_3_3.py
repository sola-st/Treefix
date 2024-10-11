import typing as t # pragma: no cover

t.Optional = t.Optional # pragma: no cover
t.Tuple = t.Tuple # pragma: no cover
t.Callable = t.Callable # pragma: no cover
class TemplateNotFound(Exception): pass # pragma: no cover
environment = type('Mock', (object,), {})() # pragma: no cover
template = 'example_template' # pragma: no cover
self = type('Mock', (object,), { '_iter_loaders': lambda self, template: iter([('srcobj1', type('Loader', (object,), { 'get_source': lambda self, env, tmpl: ('source', 'filename', lambda: True) })()), ('srcobj2', type('Loader', (object,), { 'get_source': lambda self, env, tmpl: ('source2', None, None) })())]), 'app': type('App', (object,), {})() })() # pragma: no cover
def explain_template_loading_attempts(app, template, attempts): pass # pragma: no cover

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
