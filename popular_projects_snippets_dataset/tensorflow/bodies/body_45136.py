# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Converts a Python entity into a TensorFlow graph.

  Also see: `tf.autograph.to_code`, `tf.function`.

  Unlike `tf.function`, `to_graph` is a low-level transpiler that converts
  Python code to TensorFlow graph code. It does not implement any caching,
  variable management or create any actual ops, and is best used where greater
  control over the generated TensorFlow graph is desired. Another difference
  from `tf.function` is that `to_graph` will not wrap the graph into a
  TensorFlow function or a Python callable. Internally, `tf.function` uses
  `to_graph`.

  Example usage:

  >>> def f(x):
  ...   if x > 0:
  ...     y = x * x
  ...   else:
  ...     y = -x
  ...   return y
  ...
  >>> converted_f = to_graph(f)
  >>> x = tf.constant(2)
  >>> converted_f(x)  # converted_foo is like a TensorFlow Op.
  <tf.Tensor: shape=(), dtype=int32, numpy=4>

  Supported Python entities include:
    * functions
    * classes
    * object methods

  Functions are converted into new functions with converted code.

  Classes are converted by generating a new class whose methods use converted
  code.

  Methods are converted into unbound function that have an additional first
  argument called `self`.

  For a tutorial, see the
  [tf.function and AutoGraph guide](https://www.tensorflow.org/guide/function).
  For more detailed information, see the
  [AutoGraph reference documentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/index.md).

  Args:
    entity: Python callable or class to convert.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    Same as `entity`, the converted Python function or class.

  Raises:
    ValueError: If the entity could not be converted.
  """
try:
    program_ctx = converter.ProgramContext(
        options=converter.ConversionOptions(
            recursive=recursive,
            user_requested=True,
            optional_features=experimental_optional_features))
    exit(autograph_artifact(_convert_actual(entity, program_ctx)))
except (ValueError, AttributeError, KeyError, NameError, AssertionError) as e:
    logging.error(1, 'Error converting %s', entity, exc_info=True)
    raise ConversionError('converting {}: {}: {}'.format(
        entity, e.__class__.__name__, str(e)))
