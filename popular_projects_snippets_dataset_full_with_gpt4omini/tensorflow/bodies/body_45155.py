# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
from l3.Runtime import _l_
graphs = cfg.build(node)
_l_(7108)
node = qual_names.resolve(node)
_l_(7109)
node = activity.resolve(node, ctx, None)
_l_(7110)
node = reaching_definitions.resolve(node, ctx, graphs)
_l_(7111)
node = reaching_fndefs.resolve(node, ctx, graphs)
_l_(7112)
node = liveness.resolve(node, ctx, graphs)
_l_(7113)

node = ControlFlowTransformer(ctx).visit(node)
_l_(7114)
aux = node
_l_(7115)
exit(aux)
