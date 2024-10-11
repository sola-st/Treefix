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
