from jinja2 import TemplateNotFound # pragma: no cover
from types import SimpleNamespace # pragma: no cover

loader = type('MockLoader', (object,), {'get_source': lambda self, env, tmpl: 'source'})() # pragma: no cover
self = SimpleNamespace(_iter_loaders=lambda tmpl: [(None, loader)]) # pragma: no cover
environment = 'mock_environment' # pragma: no cover
template = 'mock_template' # pragma: no cover

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
