# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
# JSON objects may only have string keys, so don't bother tagging the
# key here.
from l3.Runtime import _l_
aux = {k: self.serializer.tag(v) for k, v in value.items()}
_l_(22874)
exit(aux)
