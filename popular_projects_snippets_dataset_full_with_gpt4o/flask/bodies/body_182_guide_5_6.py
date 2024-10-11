import typing as t # pragma: no cover
from flask import Flask, request, stream_with_context # pragma: no cover
from blinker import Signal # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {} # pragma: no cover
before_render_template = Signal('before_render_template') # pragma: no cover
template_rendered = Signal('template_rendered') # pragma: no cover
template = type('MockTemplate', (object,), {'generate': lambda self, ctx: iter(['generated content'])})() # pragma: no cover
app.update_template_context = lambda ctx: None # pragma: no cover
app.test_request_context('/').push() # pragma: no cover
request.method = 'GET' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
app.update_template_context(context)
_l_(22610)
before_render_template.send(app, template=template, context=context)
_l_(22611)

def generate() -> t.Iterator[str]:
    _l_(22614)

    aux = template.generate(context)
    _l_(22612)
    exit(aux)
    template_rendered.send(app, template=template, context=context)
    _l_(22613)

rv = generate()
_l_(22615)

# If a request context is active, keep it while generating.
if request:
    _l_(22617)

    rv = stream_with_context(rv)
    _l_(22616)
aux = rv
_l_(22618)

exit(aux)
