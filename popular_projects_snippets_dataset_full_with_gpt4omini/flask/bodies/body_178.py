# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
app.update_template_context(context)
_l_(8335)
before_render_template.send(app, template=template, context=context)
_l_(8336)
rv = template.render(context)
_l_(8337)
template_rendered.send(app, template=template, context=context)
_l_(8338)
aux = rv
_l_(8339)
exit(aux)
