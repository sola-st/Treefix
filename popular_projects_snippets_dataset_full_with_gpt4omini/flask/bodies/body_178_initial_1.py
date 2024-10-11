from unittest.mock import Mock # pragma: no cover

app = Mock() # pragma: no cover
context = {} # pragma: no cover
before_render_template = Mock() # pragma: no cover
template = Mock() # pragma: no cover
template_rendered = Mock() # pragma: no cover
app.update_template_context = Mock() # pragma: no cover
before_render_template.send = Mock() # pragma: no cover
template.render = Mock(return_value='rendered output') # pragma: no cover
template_rendered.send = Mock() # pragma: no cover

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
