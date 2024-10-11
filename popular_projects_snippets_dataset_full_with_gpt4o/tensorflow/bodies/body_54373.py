# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with g.name_scope("foo"):
    op1 = g.create_op("FloatOutput", [], [dtypes.float32])
    self.has_mutated_graph.set()
    self.should_continue.wait()
    self.should_continue.clear()
    op2 = g.create_op("FloatOutput", [], [dtypes.float32])
    self.result = (op1, op2)
