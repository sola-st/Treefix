from jinja2 import Environment, TemplateNotFound, FileSystemLoader # pragma: no cover

class MockLoader:# pragma: no cover
    def get_source(self, environment, template):# pragma: no cover
        return 'mocked source' # pragma: no cover
mock_loader = MockLoader() # pragma: no cover
self = type('Mock', (object,), {'_iter_loaders': lambda self, template: [(None, mock_loader)]})() # pragma: no cover
environment = Environment(loader=FileSystemLoader('/some/path')) # pragma: no cover
template = 'template_name' # pragma: no cover

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
