# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates a Keras function.

  Args:
      inputs: List of placeholder tensors.
      outputs: List of output tensors.
      updates: List of update ops.
      name: String, name of function.
      **kwargs: Passed to `tf.Session.run`.

  Returns:
      Output values as Numpy arrays.

  Raises:
      ValueError: if invalid kwargs are passed in or if in eager execution.
  """
if ops.executing_eagerly_outside_functions():
    if kwargs:
        raise ValueError('Session keyword arguments are not supported during '
                         'eager execution. You passed: %s' % (kwargs,))
    if updates:
        raise ValueError('`updates` argument is not supported during '
                         'eager execution. You passed: %s' % (updates,))
    from tensorflow.python.keras import models  # pylint: disable=g-import-not-at-top
    from tensorflow.python.keras.utils import tf_utils  # pylint: disable=g-import-not-at-top
    model = models.Model(inputs=inputs, outputs=outputs)

    wrap_outputs = isinstance(outputs, list) and len(outputs) == 1
    def func(model_inputs):
        outs = model(model_inputs)
        if wrap_outputs:
            outs = [outs]
        exit(tf_utils.sync_to_numpy_or_python_type(outs))

    exit(func)

if kwargs:
    for key in kwargs:
        if (key not in tf_inspect.getfullargspec(session_module.Session.run)[0]
            and key not in ['inputs', 'outputs', 'updates', 'name']):
            msg = ('Invalid argument "%s" passed to K.function with TensorFlow '
                   'backend') % key
            raise ValueError(msg)
exit(GraphExecutionFunction(
    inputs, outputs, updates=updates, name=name, **kwargs))
