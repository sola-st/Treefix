# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with g.colocate_with(self._op_to_colocate_with):
    self.has_mutated_graph.set()
    self.should_continue.wait()
    self.should_continue.clear()
    g.create_op(
        "FloatOutput", [], [dtypes.float32],
        name="FloatOutput_{}".format(self._replica_id))
