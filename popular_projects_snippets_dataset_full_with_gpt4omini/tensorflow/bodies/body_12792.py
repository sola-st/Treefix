# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with ops.Graph().as_default() as g:
    with g.device("/task:0"):
        a = constant_op.constant(0, name="a")
        b = constant_op.constant(0, name="b")
    with g.device("/task:1"):
        c = constant_op.constant(0, name="c")
        d = constant_op.constant(0, name="d")
    with g.device("/task:2"):
        control_flow_ops.group(a.op, b.op, c.op, d.op, name="root")
gd = g.as_graph_def()
self.assertProtoEquals(
    """
      node { name: "a" op: "Const" device: "/task:0"}
      node { name: "b" op: "Const" device: "/task:0"}
      node { name: "c" op: "Const" device: "/task:1"}
      node { name: "d" op: "Const" device: "/task:1"}
      node { name: "root/NoOp" op: "NoOp" input: "^a" input: "^b"
             device: "/task:0" }
      node { name: "root/NoOp_1" op: "NoOp" input: "^c" input: "^d"
             device: "/task:1" }
      node { name: "root" op: "NoOp" input: "^root/NoOp" input: "^root/NoOp_1"
             device: "/task:2" }
    """, self._StripGraph(gd))
