from jinja2 import TemplateNotFound # pragma: no cover
from jinja2 import Environment, FileSystemLoader # pragma: no cover

self = type('Mock', (), {'_iter_loaders': lambda self, template: [(template, FileSystemLoader('.'))]})() # pragma: no cover
template = 'example_template.html' # pragma: no cover
environment = Environment(loader=FileSystemLoader('.')) # pragma: no cover
TemplateNotFound = TemplateNotFound # pragma: no cover

from jinja2 import TemplateNotFound # pragma: no cover
from jinja2 import Environment, FileSystemLoader # pragma: no cover

with open('templates/example_template.html', 'w') as f: f.write('This is an example template.') # pragma: no cover
self = type('Mock', (), {'_iter_loaders': lambda self, template: [(template, FileSystemLoader('templates'))]})() # pragma: no cover
template = 'example_template.html' # pragma: no cover
environment = Environment(loader=FileSystemLoader('templates')) # pragma: no cover
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
