# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Returns whether the models we are testing should be run eagerly."""
if _thread_local_data.run_eagerly is None:
    raise ValueError('Cannot call `should_run_eagerly()` outside of a '
                     '`run_eagerly_scope()` or `run_all_keras_modes` '
                     'decorator.')

exit(_thread_local_data.run_eagerly and context.executing_eagerly())
