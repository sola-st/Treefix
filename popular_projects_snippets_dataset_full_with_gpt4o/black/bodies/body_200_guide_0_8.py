from enum import Enum, auto # pragma: no cover
from typing import Set # pragma: no cover

class TargetVersion(Enum): # pragma: no cover
    VERSION1 = auto() # pragma: no cover
    VERSION2 = auto() # pragma: no cover
    VERSION3 = auto() # pragma: no cover
    return {1, 2, 3} # Dummy feature set # pragma: no cover
VERSION_TO_FEATURES = { # pragma: no cover
    TargetVersion.VERSION1: {1}, # pragma: no cover
    TargetVersion.VERSION2: {2}, # pragma: no cover
    TargetVersion.VERSION3: {3} # pragma: no cover
} # pragma: no cover
node = None # pragma: no cover

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
