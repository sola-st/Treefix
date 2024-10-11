from jinja2 import Environment, TemplateNotFound # pragma: no cover

self = type('Mock', (object,), {'_iter_loaders': lambda self, tmpl: [(None, loader) for loader in [type('Loader', (object,), {'get_source': lambda self, env, tmpl: 'source'})()] ] })() # pragma: no cover
template = 'example_template' # pragma: no cover
environment = Environment() # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

from jinja2 import Environment, TemplateNotFound # pragma: no cover

class MockLoader:# pragma: no cover
    def get_source(self, environment, template):# pragma: no cover
        if template == 'example_template':# pragma: no cover
            return 'valid_template_source', None, None# pragma: no cover
        else:# pragma: no cover
            raise TemplateNotFound(template) # pragma: no cover
def mock_iter_loaders(template):# pragma: no cover
    return iter([(None, MockLoader())]) # pragma: no cover
self = type('Mock', (object,), {'_iter_loaders': mock_iter_loaders})() # pragma: no cover
template = 'example_template' # pragma: no cover
environment = Environment() # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
for _srcobj, loader in self._iter_loaders(template):
    _l_(22756)

    try:
        _l_(22755)

        aux = loader.get_source(environment, template)
        _l_(22752)
        exit(aux)
    except TemplateNotFound:
        _l_(22754)

        continue
        _l_(22753)
raise TemplateNotFound(template)
_l_(22757)
