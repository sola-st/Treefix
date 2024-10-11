import types # pragma: no cover
from types import SimpleNamespace # pragma: no cover
class ControlFlowTransformer: # pragma: no cover
    def __init__(self, ctx): # pragma: no cover
        self.ctx = ctx # pragma: no cover
    def visit(self, node): # pragma: no cover
        return node # pragma: no cover
    pass # pragma: no cover

cfg = SimpleNamespace(build=lambda node: 'graph_object') # pragma: no cover
node = 'initial_node' # pragma: no cover
qual_names = SimpleNamespace(resolve=lambda node: 'qualified_node') # pragma: no cover
activity = SimpleNamespace(resolve=lambda node, ctx, val: 'activity_node') # pragma: no cover
ctx = 'context_object' # pragma: no cover
reaching_definitions = SimpleNamespace(resolve=lambda node, ctx, graphs: 'reaching_definitions_node') # pragma: no cover
reaching_fndefs = SimpleNamespace(resolve=lambda node, ctx, graphs: 'reaching_fndefs_node') # pragma: no cover
liveness = SimpleNamespace(resolve=lambda node, ctx, graphs: 'liveness_node') # pragma: no cover

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
