from flask import Flask, request, stream_with_context # pragma: no cover
from blinker import Signal # pragma: no cover
import typing as t # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {} # pragma: no cover
before_render_template = Signal() # pragma: no cover
template = type('MockTemplate', (), {'generate': lambda self, ctx: 'Rendered content'})() # pragma: no cover
request = None # pragma: no cover
template_rendered = Signal() # pragma: no cover

from flask import Flask, request, stream_with_context # pragma: no cover
from blinker import Signal # pragma: no cover
import typing as t # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {'key': 'value'} # pragma: no cover
before_render_template = Signal() # pragma: no cover
template = type('MockTemplate', (), {'generate': lambda self, ctx: 'Rendered content'})() # pragma: no cover
request = True # pragma: no cover
template_rendered = Signal() # pragma: no cover
exit = lambda x: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
app.update_template_context(context)
_l_(5373)
before_render_template.send(app, template=template, context=context)
_l_(5374)

def generate() -> t.Iterator[str]:
    _l_(5377)

    aux = template.generate(context)
    _l_(5375)
    exit(aux)
    template_rendered.send(app, template=template, context=context)
    _l_(5376)

rv = generate()
_l_(5378)

# If a request context is active, keep it while generating.
if request:
    _l_(5380)

    rv = stream_with_context(rv)
    _l_(5379)
aux = rv
_l_(5381)

exit(aux)
