from flask import Flask, current_app # pragma: no cover
from jinja2 import Template # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
source = 'Hello, {{ name }}!' # pragma: no cover
_render = lambda app, template, context: template.render(context) # pragma: no cover
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
