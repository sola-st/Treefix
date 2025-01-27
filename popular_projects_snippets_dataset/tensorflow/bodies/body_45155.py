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
