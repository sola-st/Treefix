from unittest.mock import Mock # pragma: no cover

cfg = Mock() # pragma: no cover
node = Mock() # pragma: no cover
qual_names = Mock() # pragma: no cover
activity = Mock() # pragma: no cover
ctx = Mock() # pragma: no cover
reaching_definitions = Mock() # pragma: no cover
reaching_fndefs = Mock() # pragma: no cover
liveness = Mock() # pragma: no cover
ControlFlowTransformer = Mock() # pragma: no cover

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
