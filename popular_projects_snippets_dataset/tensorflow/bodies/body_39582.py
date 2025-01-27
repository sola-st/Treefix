# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
"""Restores after the first should not modify the graph."""
with context.graph_mode():
    graph = ops.Graph()
    with graph.as_default(), self.session(graph):
        checkpoint_directory = self.get_temp_dir()
        checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
        obj = trackable_utils.Checkpoint()
        obj.var = variable_scope.get_variable(name="v", initializer=0.)
        obj.opt = adam.AdamOptimizer(0.1)
        obj.opt.minimize(obj.var.read_value())
        self.evaluate(trackable_utils.gather_initializers(obj))
        save_path = obj.save(checkpoint_prefix)
        obj.restore(save_path)
        before_ops = graph.get_operations()
        obj.restore(save_path)
        self.assertEqual(before_ops, graph.get_operations())
