from flask import Flask, current_app, Response # pragma: no cover
from jinja2 import Environment # pragma: no cover

app = Flask(__name__) # pragma: no cover
source = '<h1>{{ title }}</h1>' # pragma: no cover
context = {'title': 'Hello, World!'} # pragma: no cover
def _stream(app, template, context): return iter([template.render(context)]) # pragma: no cover
current_app = type('Mock', (object,), {'_get_current_object': lambda: app})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
"""Render a template from the given source string with the given
    context as a stream. This returns an iterator of strings, which can
    be used as a streaming response from a view.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    """
app = current_app._get_current_object()  # type: ignore[attr-defined]
_l_(15710)  # type: ignore[attr-defined]
template = app.jinja_env.from_string(source)
_l_(15711)
aux = _stream(app, template, context)
_l_(15712)
exit(aux)
