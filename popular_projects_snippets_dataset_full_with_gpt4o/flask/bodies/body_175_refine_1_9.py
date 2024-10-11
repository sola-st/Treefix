from jinja2 import TemplateNotFound # pragma: no cover

self = type('MockSelf', (object,), {'_iter_loaders': lambda self, template: iter([(None, type('MockLoader', (object,), {'get_source': lambda self, env, tmpl: 'source_code'})())])})() # pragma: no cover
template = 'example_template' # pragma: no cover
environment = 'example_environment' # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

from jinja2 import TemplateNotFound # pragma: no cover

self = type('MockSelf', (object,), {'_iter_loaders': lambda self, template: iter([(None, type('MockLoader', (object,), {'get_source': lambda self, env, tmpl: ('source_code', None, None)})())])})() # pragma: no cover
template = 'example_template' # pragma: no cover
environment = 'example_environment' # pragma: no cover
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
