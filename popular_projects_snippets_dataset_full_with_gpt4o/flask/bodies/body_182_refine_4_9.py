from typing import Iterator # pragma: no cover
from flask import Flask, stream_with_context, Request # pragma: no cover
from flask.signals import Namespace # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {'key': 'value'} # pragma: no cover
before_render_template = Namespace().signal('before_render_template') # pragma: no cover
template = type('MockTemplate', (object,), {'generate': lambda self, context: iter(['rendered content'])})() # pragma: no cover
t = type('MockT', (object,), { 'Iterator': Iterator }) # pragma: no cover
stream_with_context = stream_with_context # pragma: no cover
template_rendered = Namespace().signal('template_rendered') # pragma: no cover

import typing as t # pragma: no cover
from flask import Flask, stream_with_context, Request # pragma: no cover
from blinker import Namespace # pragma: no cover
import sys # pragma: no cover

app = Flask(__name__) # pragma: no cover
context = {'key': 'value'} # pragma: no cover
before_render_template = Namespace().signal('before_render_template') # pragma: no cover
template = type('MockTemplate', (object,), {'generate': lambda self, context: iter(['rendered content'])})() # pragma: no cover
t = t # pragma: no cover
stream_with_context = stream_with_context # pragma: no cover
template_rendered = Namespace().signal('template_rendered') # pragma: no cover
sys.exit = lambda x: print(x) # pragma: no cover

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
