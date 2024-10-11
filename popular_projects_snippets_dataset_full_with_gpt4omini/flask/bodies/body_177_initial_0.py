from flask import Flask, Blueprint # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'app': app})() # pragma: no cover
app.jinja_loader = type('Mock', (object,), {'list_templates': lambda self: ['template1.html', 'template2.html']})() # pragma: no cover
blueprint = Blueprint('mock_blueprint', __name__) # pragma: no cover
blueprint.jinja_loader = type('Mock', (object,), {'list_templates': lambda self: ['template3.html']})() # pragma: no cover
app.blueprints = {'mock_blueprint': blueprint} # pragma: no cover
app.iter_blueprints = lambda self: iter(self.blueprints.values()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
result = set()
_l_(7481)
loader = self.app.jinja_loader
_l_(7482)
if loader is not None:
    _l_(7484)

    result.update(loader.list_templates())
    _l_(7483)

for blueprint in self.app.iter_blueprints():
    _l_(7489)

    loader = blueprint.jinja_loader
    _l_(7485)
    if loader is not None:
        _l_(7488)

        for template in loader.list_templates():
            _l_(7487)

            result.add(template)
            _l_(7486)
aux = list(result)
_l_(7490)

exit(aux)
