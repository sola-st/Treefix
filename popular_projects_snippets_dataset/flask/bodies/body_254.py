# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if not current_app:
    _l_(22901)

    app = __ctx.ensure_object(ScriptInfo).load_app()
    _l_(22899)
    __ctx.with_resource(app.app_context())
    _l_(22900)
aux = __ctx.invoke(f, *args, **kwargs)
_l_(22902)

exit(aux)
