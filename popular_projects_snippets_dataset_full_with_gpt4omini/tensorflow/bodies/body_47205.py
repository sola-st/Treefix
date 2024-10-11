# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Reset state trackers for model.

  Note that we do not actually zero out attributes such as optimizer,
  but instead rely on the expectation that all of the attrs will be
  over-written on calling build/compile/etc. This is somewhat fragile,
  insofar as we check elsewhere for the presence of these attributes as
  evidence of having been built/compiled/etc. Pending a better way to do this,
  we reset key attributes here to allow building and compiling.

  Args:
    model: the model that is being reset
  """
# Reset build state
model.built = False
model.inputs = None
model.outputs = None
# Reset compile state
model._is_compiled = False  # pylint:disable=protected-access
if not ops.executing_eagerly_outside_functions():
    model._v1_compile_was_called = False
model.optimizer = None
