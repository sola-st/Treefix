from typing import Optional, Tuple, Callable # pragma: no cover
from jinja2 import TemplateNotFound # pragma: no cover

t = type('MockTypeHints', (object,), {'Optional': Optional, 'Tuple': Tuple, 'Callable': Callable}) # pragma: no cover
self = type('MockSelf', (object,), {'_iter_loaders': lambda self, template: [(None, type('MockLoader', (object,), {'get_source': lambda self, env, tmpl: ('source', None, None)})())]})() # pragma: no cover
template = 'mock_template' # pragma: no cover
environment = 'mock_environment' # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

from typing import Optional, Tuple, Callable # pragma: no cover
from jinja2 import TemplateNotFound # pragma: no cover

t = type('MockTypeHints', (object,), {'Optional': Optional, 'Tuple': Tuple, 'Callable': Callable}) # pragma: no cover
class MockLoader:# pragma: no cover
    def get_source(self, env, tmpl):# pragma: no cover
        return ('source_code', None, None) # pragma: no cover
self = type('MockSelf', (object,), {'_iter_loaders': lambda self, template: [(None, MockLoader())]})() # pragma: no cover
template = 'mock_template' # pragma: no cover
environment = 'mock_environment' # pragma: no cover
attempts = [] # pragma: no cover
def explain_template_loading_attempts(app, template, attempts):# pragma: no cover
    print(f'Explaining attempts for template: {template}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
attempts = []
_l_(8534)
rv: t.Optional[t.Tuple[str, t.Optional[str], t.Optional[t.Callable[[], bool]]]]
_l_(8535)
trv: t.Optional[
    t.Tuple[str, t.Optional[str], t.Optional[t.Callable[[], bool]]]
] = None
_l_(8536)

for srcobj, loader in self._iter_loaders(template):
    _l_(8544)

    try:
        _l_(8542)

        rv = loader.get_source(environment, template)
        _l_(8537)
        if trv is None:
            _l_(8539)

            trv = rv
            _l_(8538)
    except TemplateNotFound:
        _l_(8541)

        rv = None
        _l_(8540)
    attempts.append((loader, srcobj, rv))
    _l_(8543)
try:
    from .debughelpers import explain_template_loading_attempts
    _l_(8546)

except ImportError:
    pass

explain_template_loading_attempts(self.app, template, attempts)
_l_(8547)

if trv is not None:
    _l_(8549)

    aux = trv
    _l_(8548)
    exit(aux)
raise TemplateNotFound(template)
_l_(8550)
