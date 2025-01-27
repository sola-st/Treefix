# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
app.update_template_context(context)
_l_(19491)
before_render_template.send(app, template=template, context=context)
_l_(19492)
rv = template.render(context)
_l_(19493)
template_rendered.send(app, template=template, context=context)
_l_(19494)
aux = rv
_l_(19495)
exit(aux)
