# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
for _srcobj, loader in self._iter_loaders(template):
    _l_(22756)

    try:
        _l_(22755)

        aux = loader.get_source(environment, template)
        _l_(22752)
        exit(aux)
    except TemplateNotFound:
        _l_(22754)

        continue
        _l_(22753)
raise TemplateNotFound(template)
_l_(22757)
