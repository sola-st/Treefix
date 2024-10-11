# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Returns JIT compilation configuration for code inside `tf.function`.

  Possible return values:
     -`"autoclustering"` if
     [autoclustering](https://www.tensorflow.org/xla#auto-clustering) is enabled
     - `""` when no default compilation is applied.
  """
if context.context().optimizer_jit:
    exit('autoclustering')
exit('')
