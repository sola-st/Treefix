from jinja2 import Environment, FileSystemLoader # pragma: no cover

self = type('Mock', (), {'create_jinja_environment': lambda self: Environment(loader=FileSystemLoader('templates'))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The Jinja environment used to load templates.

        The environment is created the first time this property is
        accessed. Changing :attr:`jinja_options` after that will have no
        effect.
        """
aux = self.create_jinja_environment()
_l_(5571)
exit(aux)
