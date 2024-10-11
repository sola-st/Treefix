from flask import current_app # pragma: no cover
from jinja2 import Environment # pragma: no cover

current_app = type('Mock', (object,), {'_get_current_object': lambda self: self, 'jinja_env': Environment()})() # pragma: no cover
source = '<h1>Hello {{ name }}</h1>' # pragma: no cover
_stream = lambda app, template, context: (template.render(context),) # pragma: no cover
context = {'name': 'World'} # pragma: no cover

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
_l_(4150)  # type: ignore[attr-defined]
template = app.jinja_env.from_string(source)
_l_(4151)
aux = _stream(app, template, context)
_l_(4152)
exit(aux)
