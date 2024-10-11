import typing as t # pragma: no cover
from flask import Flask, request, stream_with_context, signals # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {} # pragma: no cover
before_render_template = type('MockSignal', (object,), {'send': lambda self, app, template, context: None})() # pragma: no cover
template = type('MockTemplate', (object,), {'generate': lambda self, context: iter(['<html></html>'])})() # pragma: no cover
template_rendered = type('MockSignal', (object,), {'send': lambda self, app, template, context: None})() # pragma: no cover

import typing as t # pragma: no cover
from flask import Flask, request, stream_with_context # pragma: no cover
from blinker import Namespace # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {} # pragma: no cover
signals = Namespace() # pragma: no cover
before_render_template = signals.signal('before_render_template') # pragma: no cover
template_rendered = signals.signal('template_rendered') # pragma: no cover
template = type('MockTemplate', (object,), {'generate': lambda self, context: iter(['rendered template'])})() # pragma: no cover
request = type('MockRequest', (object,), {'__bool__': lambda self: True})() # pragma: no cover

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
