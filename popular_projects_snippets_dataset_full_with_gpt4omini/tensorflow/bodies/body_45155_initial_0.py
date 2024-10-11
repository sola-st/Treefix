from typing import Any, Dict # pragma: no cover
class Mock(object): pass # pragma: no cover

cfg = Mock() # pragma: no cover
cfg.build = lambda node: node # pragma: no cover
node = 'initial_node' # pragma: no cover
qual_names = Mock() # pragma: no cover
qual_names.resolve = lambda node: node # pragma: no cover
activity = Mock() # pragma: no cover
activity.resolve = lambda node, ctx, arg: node # pragma: no cover
ctx = {'example_context_key': 'example_context_value'} # pragma: no cover
reaching_definitions = Mock() # pragma: no cover
reaching_definitions.resolve = lambda node, ctx, graphs: node # pragma: no cover
reaching_fndefs = Mock() # pragma: no cover
reaching_fndefs.resolve = lambda node, ctx, graphs: node # pragma: no cover
liveness = Mock() # pragma: no cover
liveness.resolve = lambda node, ctx, graphs: node # pragma: no cover

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
