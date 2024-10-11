from enum import Enum # pragma: no cover
from typing import Set # pragma: no cover
import builtins # pragma: no cover

class TargetVersion(Enum): # pragma: no cover
    V1 = 1 # pragma: no cover
    V2 = 2 # pragma: no cover
    V3 = 3 # pragma: no cover
 # pragma: no cover
VERSION_TO_FEATURES = { # pragma: no cover
    TargetVersion.V1: {'f1', 'f2'}, # pragma: no cover
    TargetVersion.V2: {'f1', 'f2', 'f3'}, # pragma: no cover
    TargetVersion.V3: {'f1', 'f2', 'f3', 'f4'}, # pragma: no cover
} # pragma: no cover
 # pragma: no cover
    return {'f1', 'f2'} # pragma: no cover
 # pragma: no cover
node = builtins.object() # pragma: no cover

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
