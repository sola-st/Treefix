# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
"""Use Keras-style variable management.

  All tf.layers and tf RNN cells created after keras style ha been enabled
  use Keras-style variable management.  Creating such layers with a
  scope= argument is disallowed, and reuse=True is disallowed.

  The purpose of this function is to allow users of existing layers to
  slowly transition to Keras layers API without breaking existing
  functionality.

  For more details, see the documentation for `keras_style_scope`.

  Note, once keras style has been set, it is set globally for the entire
  program and cannot be unset.

  Example:

  ```python
  set_keras_style()

  model_1 = RNNModel(name="model_1")
  model_2 = RNNModel(name="model_2")

  # model_1 and model_2 are guaranteed to create their own variables.
  output_1, next_state_1 = model_1(input, state)
  output_2, next_state_2 = model_2(input, state)

  assert len(model_1.weights) > 0
  assert len(model_2.weights) > 0
  assert(model_1.weights != model_2.weights)
  ```
  """
global _KERAS_STYLE_SCOPE
_KERAS_STYLE_SCOPE = True
