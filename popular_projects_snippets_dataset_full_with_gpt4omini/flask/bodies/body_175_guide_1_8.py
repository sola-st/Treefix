from jinja2 import Environment, TemplateNotFound, FileSystemLoader # pragma: no cover

class MockLoader:  # Mock loader class # pragma: no cover
    def get_source(self, environment, template): # pragma: no cover
        return 'source code for {}'.format(template) # pragma: no cover
  # Successful retrieval of template source # pragma: no cover
 # pragma: no cover
class MockContext:  # Mock for 'self' # pragma: no cover
    def _iter_loaders(self, template): # pragma: no cover
        return [(None, MockLoader())]  # Simulate one loader returning # pragma: no cover
 # pragma: no cover
self = MockContext() # pragma: no cover
environment = Environment(loader=FileSystemLoader('/mock/path')) # pragma: no cover
template = 'test_template' # pragma: no cover

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
