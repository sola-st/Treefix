from typing import List, Dict, Set, Union # pragma: no cover

node = 'node_identifier' # pragma: no cover
TargetVersion = {'v1.0', 'v2.0', 'v3.0'} # pragma: no cover
VERSION_TO_FEATURES = {'v1.0': {'feature_a'}, 'v2.0': {'feature_a', 'feature_b'}, 'v3.0': {'feature_a', 'feature_b', 'feature_c'}} # pragma: no cover

from typing import Set, Dict, Any # pragma: no cover

node = 'example_node' # pragma: no cover
TargetVersion = {'v1', 'v2', 'v3'} # pragma: no cover
VERSION_TO_FEATURES = {'v1': {'feature_a'}, 'v2': {'feature_a', 'feature_b'}, 'v3': {'feature_a', 'feature_b', 'feature_c'}} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Detect the version to target based on the nodes used."""
features = get_features_used(node, future_imports=future_imports)
_l_(3879)
aux = {
    version for version in TargetVersion if features <= VERSION_TO_FEATURES[version]
}
_l_(3880)
exit(aux)
