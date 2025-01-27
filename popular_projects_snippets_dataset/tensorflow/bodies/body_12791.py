# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with ops.Graph().as_default() as g:
    with g.device("/task:0"):
        a = constant_op.constant(0, name="a")
        b = constant_op.constant(0, name="b")
    control_flow_ops.group(a.op, b.op, name="root")
gd = g.as_graph_def()
self.assertProtoEquals(
    """
      node { name: "a" op: "Const" device: "/task:0" }
      node { name: "b" op: "Const" device: "/task:0" }
      node { name: "root" op: "NoOp" input: "^a" input: "^b" device: "/task:0" }
    """, self._StripGraph(gd))
