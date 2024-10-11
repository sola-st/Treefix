from enum import Enum, auto # pragma: no cover
from typing import Set # pragma: no cover

class TargetVersion(Enum): # pragma: no cover
    VERSION_1 = auto() # pragma: no cover
    VERSION_2 = auto() # pragma: no cover
    VERSION_3 = auto() # pragma: no cover
VERSION_TO_FEATURES = { # pragma: no cover
    TargetVersion.VERSION_1: {'feature_a', 'feature_b'}, # pragma: no cover
    TargetVersion.VERSION_2: {'feature_a', 'feature_b', 'feature_c'}, # pragma: no cover
    TargetVersion.VERSION_3: {'feature_a', 'feature_b', 'feature_c', 'feature_d'} # pragma: no cover
} # pragma: no cover
    return {'feature_a', 'feature_b', 'feature_c'} # pragma: no cover
node = type('Mock', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Detect the version to target based on the nodes used."""
features = get_features_used(node, future_imports=future_imports)
_l_(15424)
aux = {
    version for version in TargetVersion if features <= VERSION_TO_FEATURES[version]
}
_l_(15425)
exit(aux)
