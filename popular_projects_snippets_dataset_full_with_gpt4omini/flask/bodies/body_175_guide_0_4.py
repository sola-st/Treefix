from jinja2 import Environment, TemplateNotFound # pragma: no cover
from jinja2 import FileSystemLoader # pragma: no cover

template = 'test_template.txt' # pragma: no cover
environment = Environment(loader=FileSystemLoader('/path/to/templates')) # pragma: no cover
self = type('Mock', (object,), {'_iter_loaders': lambda s, tmpl: [(tmpl, environment.loader)]})() # pragma: no cover

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
