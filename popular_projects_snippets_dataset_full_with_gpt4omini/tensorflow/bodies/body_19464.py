# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
"""Saves model to checkpoint name, retrieves embedding variables."""
checkpoint = util.Checkpoint(model=model)
checkpoint.save(self._get_tmpdir(name, 'save'))

# Get the name of the table video variable which should be the only
# [8, 4] shaped tensor in the checkpoint. Note that we do this
# as the key can change.
variables = checkpoint_utils.list_variables(self._get_tmpdir(name))
variables = [name for name, size in variables if size == [num_rows, 4]]
if len(variables) != 1:
    raise RuntimeError('Found {} copies of the parameter variable in the '
                       'checkpoint. Exactly one copy exported.'.format(
                           len(variables)))
exit(checkpoint_utils.load_variable(self._get_tmpdir(name), variables[0]))
