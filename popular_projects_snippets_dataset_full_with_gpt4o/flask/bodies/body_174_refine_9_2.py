from typing import Optional, Tuple, Callable # pragma: no cover
import sys # pragma: no cover

t = type('t', (), {'Optional': Optional, 'Tuple': Tuple, 'Callable': Callable}) # pragma: no cover
TemplateNotFound = type('TemplateNotFound', (Exception,), {}) # pragma: no cover
self = type('Mock', (object,), {'_iter_loaders': lambda self, template: iter([]), 'app': None})() # pragma: no cover
template = '' # pragma: no cover
environment = type('MockEnvironment', (object,), {})() # pragma: no cover

from typing import Optional, Tuple, Callable # pragma: no cover

class MockLoader: # pragma: no cover
    def get_source(self, environment, template): # pragma: no cover
        return ('source', 'filename', lambda: True)  # Dummy values, replace them accordingly # pragma: no cover
 # pragma: no cover
class MockApp: # pragma: no cover
    def explain_template_loading_attempts(self, app, template, attempts): # pragma: no cover
        print(f'Explaining template loading attempts for {template}.') # pragma: no cover
t = type('t', (object,), { # pragma: no cover
    'Optional': Optional, # pragma: no cover
    'Tuple': Tuple, # pragma: no cover
    'Callable': Callable # pragma: no cover
}) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_iter_loaders': lambda self, template: [(MockLoader(), 'srcobj')], # pragma: no cover
    'app': MockApp() # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
template = 'dummy_template'  # Replace with an actual template name # pragma: no cover
environment = 'dummy_environment'  # Replace with an actual environment object # pragma: no cover
TemplateNotFound = type('TemplateNotFound', (Exception,), {}) # pragma: no cover
 # pragma: no cover
def explain_template_loading_attempts(app, template, attempts): # pragma: no cover
    print(f'Explain template loading for {template} with attempts: {attempts}') # pragma: no cover

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
