from flask import Flask, render_template # pragma: no cover
from blinker import Signal # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {'key': 'value'} # pragma: no cover
before_render_template = Signal('before-render-template') # pragma: no cover
template_rendered = Signal('template-rendered') # pragma: no cover

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
