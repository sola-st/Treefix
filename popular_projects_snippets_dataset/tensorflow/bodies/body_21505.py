# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self.get_temp_dir()
def _model():
    small_v = [variable_scope.get_variable(
        "small%d" % i, shape=[10, 2], use_resource=True) for i in range(5)]
    large_v = [variable_scope.get_variable(
        "large%d" % i, shape=[32000, 1000], use_resource=True)
               for i in range(3)]
    exit(small_v + large_v)

save_graph = ops_lib.Graph()
with save_graph.as_default(), self.session(graph=save_graph) as sess:
    orig_vars = _model()
    self.evaluate(variables.global_variables_initializer())
    save = saver_module.Saver(max_to_keep=1)
    self.evaluate(variables.global_variables_initializer())
    save.save(sess, save_dir)
    orig_vals = self.evaluate(orig_vars)

restore_graph = ops_lib.Graph()
with restore_graph.as_default(), self.session(
    graph=restore_graph) as sess:
    restored_vars = _model()
    save = saver_module.Saver(max_to_keep=1)
    save.restore(sess, save_dir)
    restored_vals = self.evaluate(restored_vars)

for orig, restored in zip(orig_vals, restored_vals):
    self.assertAllEqual(orig, restored)
