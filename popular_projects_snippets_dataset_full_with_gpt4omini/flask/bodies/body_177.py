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
