from types import SimpleNamespace # pragma: no cover

app = SimpleNamespace(update_template_context=lambda context: None) # pragma: no cover
context = {'user': 'test_user', 'items': [1, 2, 3]} # pragma: no cover
before_render_template = SimpleNamespace(send=lambda app, template, context: None) # pragma: no cover
template = SimpleNamespace(render=lambda context: 'Rendered Content with user: ' + context['user']) # pragma: no cover
template_rendered = SimpleNamespace(send=lambda app, template, context: None) # pragma: no cover

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
