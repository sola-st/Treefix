from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(endpoint='blueprint_name.endpoint') # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.endpoint = 'my_blueprint.my_endpoint' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
"""The registered name of the current blueprint.

        This will be ``None`` if the endpoint is not part of a
        blueprint, or if URL matching failed or has not been performed
        yet.

        This does not necessarily match the name the blueprint was
        created with. It may have been nested, or registered with a
        different name.
        """
endpoint = self.endpoint
_l_(6971)

if endpoint is not None and "." in endpoint:
    _l_(6973)

    aux = endpoint.rpartition(".")[0]
    _l_(6972)
    exit(aux)
aux = None
_l_(6974)

exit(aux)
