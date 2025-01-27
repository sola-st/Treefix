# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
self.graph = ops_lib.Graph()
with self.graph.as_default():
    self.a = constant_op.constant([1., 1.], shape=[2], name="a")
    with ops_lib.name_scope("foo"):
        self.b = constant_op.constant([2., 2.], shape=[2], name="b")
        self.c = math_ops.add(self.a, self.b, name="c")
        self.d = constant_op.constant([3., 3.], shape=[2], name="d")
        with ops_lib.name_scope("bar"):
            self.e = math_ops.add(self.c, self.d, name="e")
            self.f = math_ops.add(self.c, self.d, name="f")
            self.g = math_ops.add(self.c, self.a, name="g")
            with ops_lib.control_dependencies([self.c.op]):
                self.h = math_ops.add(self.f, self.g, name="h")
