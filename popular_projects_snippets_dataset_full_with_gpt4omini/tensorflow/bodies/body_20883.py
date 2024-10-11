# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    _create_checkpoints(session, checkpoint_dir)

with ops.Graph().as_default():
    with ops.device("/job:ps"):
        with variable_scope.variable_scope("useful_scope"):
            variable_scope.get_variable("var4", [9, 9])

    checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                          {"useful_scope/": "useful_scope/"})
