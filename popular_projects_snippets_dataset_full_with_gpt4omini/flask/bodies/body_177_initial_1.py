from flask import Flask, Blueprint, render_template # pragma: no cover

class MockLoader:# pragma: no cover
    def list_templates(self):# pragma: no cover
        return ["template1.html", "template2.html"]# pragma: no cover
# pragma: no cover
class MockApp:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.jinja_loader = MockLoader()# pragma: no cover
    def iter_blueprints(self):# pragma: no cover
        return [MockBlueprint()] # pragma: no cover
class MockBlueprint:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.jinja_loader = MockLoader() # pragma: no cover
self = type('Mock', (), {'app': MockApp()})() # pragma: no cover

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
