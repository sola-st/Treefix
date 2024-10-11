from unittest.mock import Mock # pragma: no cover

cfg = Mock(build=Mock(return_value='graph_data')) # pragma: no cover
node = 'initial_node' # pragma: no cover
qual_names = Mock(resolve=Mock(return_value='resolved_qual_names_node')) # pragma: no cover
activity = Mock(resolve=Mock(return_value='resolved_activity_node')) # pragma: no cover
ctx = 'context_data' # pragma: no cover
reaching_definitions = Mock(resolve=Mock(return_value='resolved_reaching_definitions_node')) # pragma: no cover
reaching_fndefs = Mock(resolve=Mock(return_value='resolved_reaching_fndefs_node')) # pragma: no cover
liveness = Mock(resolve=Mock(return_value='resolved_liveness_node')) # pragma: no cover
ControlFlowTransformer = type('ControlFlowTransformer', (object,), {'visit': lambda self, x: 'transformed_node'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
from l3.Runtime import _l_
graphs = cfg.build(node)
_l_(20006)
node = qual_names.resolve(node)
_l_(20007)
node = activity.resolve(node, ctx, None)
_l_(20008)
node = reaching_definitions.resolve(node, ctx, graphs)
_l_(20009)
node = reaching_fndefs.resolve(node, ctx, graphs)
_l_(20010)
node = liveness.resolve(node, ctx, graphs)
_l_(20011)

node = ControlFlowTransformer(ctx).visit(node)
_l_(20012)
aux = node
_l_(20013)
exit(aux)
