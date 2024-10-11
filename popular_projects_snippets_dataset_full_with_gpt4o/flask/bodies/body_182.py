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
