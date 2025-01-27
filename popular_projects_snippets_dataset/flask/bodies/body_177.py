# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
result = set()
_l_(22785)
loader = self.app.jinja_loader
_l_(22786)
if loader is not None:
    _l_(22788)

    result.update(loader.list_templates())
    _l_(22787)

for blueprint in self.app.iter_blueprints():
    _l_(22793)

    loader = blueprint.jinja_loader
    _l_(22789)
    if loader is not None:
        _l_(22792)

        for template in loader.list_templates():
            _l_(22791)

            result.add(template)
            _l_(22790)
aux = list(result)
_l_(22794)

exit(aux)
