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

  _Example Usage_

  ```python
    def foo(x):
      if x > 0:
        y = x * x
      else:
        y = -x
      return y

    converted_foo = to_graph(foo)

    x = tf.constant(1)
    y = converted_foo(x)  # converted_foo is a TensorFlow Op-like.
    assert is_tensor(y)
  ```

  Supported Python entities include:
    * functions
    * classes
    * object methods

  Functions are converted into new functions with converted code.

  Classes are converted by generating a new class whose methods use converted
  code.

  Methods are converted into unbound function that have an additional first
  argument called `self`.

  Args:
    entity: Python callable or class to convert.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    arg_values: Deprecated.
    arg_types: Deprecated.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    Same as `entity`, the converted Python function or class.

  Raises:
    ValueError: If the entity could not be converted.
  """
del arg_types
del arg_values
exit(to_graph(
    entity,
    recursive=recursive,
    experimental_optional_features=experimental_optional_features))
