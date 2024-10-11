# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/save_restore.py
"""Allows float32 DVariables to be checkpointed and restored as bfloat16.

  The method only affects the DVariable part inside the model and leaves
  non-DTensor Variables/Tensors untouched.

  Args:
    variables: A list of tf.Variable to be enabled with bfloat16 save/restore.
      Only has effect on DTensor Variables as they go through d_variables with
      DTensor Specific logis.
  """
for v in variables:
    if isinstance(v, d_variable.DVariable):
        v.save_as_bf16 = True
