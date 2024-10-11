from flask import Flask, current_app # pragma: no cover
import jinja2 # pragma: no cover

current_app = type("Mock", (object,), {"_get_current_object": lambda self: self})() # pragma: no cover
current_app.jinja_env = jinja2.Environment() # pragma: no cover
source = '{{ variable }} template source' # pragma: no cover
_render = lambda app, template, context: template.render(context) # pragma: no cover
context = {'variable': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
"""Render a template from the given source string with the given
    context.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.
    """
app = current_app._get_current_object()  # type: ignore[attr-defined]
_l_(18214)  # type: ignore[attr-defined]
template = app.jinja_env.from_string(source)
_l_(18215)
aux = _render(app, template, context)
_l_(18216)
exit(aux)
