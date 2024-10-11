from jinja2 import TemplateNotFound # pragma: no cover
from jinja2 import Environment # pragma: no cover

self = type('Mock', (), {'_iter_loaders': lambda template: [(None, type('MockLoader', (), {'get_source': lambda env, tmpl: 'source_code'})())]})() # pragma: no cover
template = 'my_template.html' # pragma: no cover
environment = Environment() # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

from jinja2 import TemplateNotFound # pragma: no cover
from jinja2 import Environment # pragma: no cover

class MockLoader:# pragma: no cover
    def get_source(self, environment, template):# pragma: no cover
        return 'source code' # pragma: no cover
self = type('Mock', (), {'_iter_loaders': lambda self, template: [(None, MockLoader())]})() # pragma: no cover
template = 'my_template.html' # pragma: no cover
environment = Environment() # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
for _srcobj, loader in self._iter_loaders(template):
    _l_(6968)

    try:
        _l_(6967)

        aux = loader.get_source(environment, template)
        _l_(6964)
        exit(aux)
    except TemplateNotFound:
        _l_(6966)

        continue
        _l_(6965)
raise TemplateNotFound(template)
_l_(6969)
