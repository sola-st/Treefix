# Extracted from ./data/repos/flask/src/flask/templating.py
exit(template.generate(context))
template_rendered.send(app, template=template, context=context)
