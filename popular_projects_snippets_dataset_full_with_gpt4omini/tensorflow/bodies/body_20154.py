# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
global_step = session.run(self._global_step_tensor)

# We do write graph and saver_def at the first call of before_run.
# We cannot do this in begin, since we let other hooks to change graph and
# add variables in begin. Graph is finalized after all begin calls.
def _write_graph_fn(self):
    training_util.write_graph(
        ops.get_default_graph().as_graph_def(add_shapes=True),
        self._checkpoint_dir, "graph.pbtxt")
self._write_graph_thread = threading.Thread(target=_write_graph_fn,
                                            args=[self])
self._write_graph_thread.start()

saver_def = self._get_saver().saver_def if self._get_saver() else None
graph = ops.get_default_graph()
meta_graph_def = meta_graph.create_meta_graph_def(
    graph_def=graph.as_graph_def(add_shapes=True), saver_def=saver_def)
self._summary_writer.add_graph(graph)
self._summary_writer.add_meta_graph(meta_graph_def)
# The checkpoint saved here is the state at step "global_step".
self._save(session, global_step)
self._timer.update_last_triggered_step(global_step)
