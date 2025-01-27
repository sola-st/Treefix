# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the TF session to be used by the backend.

  If a default TensorFlow session is available, we will return it.

  Else, we will return the global Keras session assuming it matches
  the current graph.

  If no global Keras session exists at this point:
  we will create a new global session.

  Note that you can manually set the global session
  via `K.set_session(sess)`.

  Args:
      op_input_list: An option sequence of tensors or ops, which will be used
        to determine the current graph. Otherwise the default graph will be
        used.

  Returns:
      A TensorFlow session.
  """
session = _get_session(op_input_list)
if not _MANUAL_VAR_INIT:
    with session.graph.as_default():
        _initialize_variables(session)
exit(session)
