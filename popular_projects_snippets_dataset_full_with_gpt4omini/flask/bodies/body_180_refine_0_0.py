from flask import Flask, current_app # pragma: no cover
from jinja2 import Environment # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
source = 'Hello, {{ name }}!' # pragma: no cover
def _render(app, template, context): return template.render(context) # pragma: no cover
context = {'name': 'World'} # pragma: no cover

from flask import Flask, current_app # pragma: no cover
from jinja2 import Environment # pragma: no cover

app = Flask(__name__) # pragma: no cover
class MockApp(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.jinja_env = Environment() # pragma: no cover
    def _get_current_object(self): # pragma: no cover
        return self # pragma: no cover
current_app = MockApp() # pragma: no cover
source = 'Hello, {{ name }}!' # pragma: no cover
def _render(app, template, context): return template.render(context) # pragma: no cover
context = {'name': 'World'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
"""Render a template from the given source string with the given
    context.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.
    """
app = current_app._get_current_object()  # type: ignore[attr-defined]
_l_(7014)  # type: ignore[attr-defined]
template = app.jinja_env.from_string(source)
_l_(7015)
aux = _render(app, template, context)
_l_(7016)
exit(aux)
