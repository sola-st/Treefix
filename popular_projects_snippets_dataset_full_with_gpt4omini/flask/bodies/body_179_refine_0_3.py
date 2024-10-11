from flask import Flask # pragma: no cover
from jinja2 import Environment, FileSystemLoader # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
template_name_or_list = 'example_template.html' # pragma: no cover
def _render(app, template, context): return template.render(context) # pragma: no cover
context = {'key': 'value'} # pragma: no cover

from flask import Flask, current_app # pragma: no cover
from jinja2 import Template # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
template_name_or_list = 'example_template.html' # pragma: no cover
def _render(app, template, context): return template.render(context) # pragma: no cover
template = Template('<h1>{{ key }}</h1>') # pragma: no cover
context = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
"""Render a template by name with the given context.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.
    """
app = current_app._get_current_object()  # type: ignore[attr-defined]
_l_(6883)  # type: ignore[attr-defined]
template = app.jinja_env.get_or_select_template(template_name_or_list)
_l_(6884)
aux = _render(app, template, context)
_l_(6885)
exit(aux)
