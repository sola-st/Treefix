# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Marks the function as unsaveable if not inside save context."""
if ops.inside_function() and not save_context.in_save_context():
    ops.get_default_graph().mark_as_unsaveable("""
ConcreteFunction that uses distributed variables in certain way cannot be saved.
If you're saving with

tf.saved_model.save(..., signatures=f.get_concrete_function())

do

@tf.function(input_signature=...)
def f_with_input_signature():
  ...

tf.saved_model.save(..., signatures=f_with_input_signature)`

instead.""")
