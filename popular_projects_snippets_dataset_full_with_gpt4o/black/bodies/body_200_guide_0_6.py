from enum import Enum, auto # pragma: no cover
from typing import Set # pragma: no cover
def get_features_used(node, future_imports=None): return set() # pragma: no cover
class TargetVersion(Enum): V1 = auto(); V2 = auto(); V3 = auto() # pragma: no cover
VERSION_TO_FEATURES = {TargetVersion.V1: set(), TargetVersion.V2: set(), TargetVersion.V3: set()} # pragma: no cover

node = type('MockNode', (object,), {})() # pragma: no cover

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
