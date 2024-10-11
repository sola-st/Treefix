# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
training_util.write_graph(
    ops.get_default_graph().as_graph_def(add_shapes=True),
    self._checkpoint_dir, "graph.pbtxt")
