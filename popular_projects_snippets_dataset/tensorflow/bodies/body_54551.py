# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Configure JIT compilation.

  Note: compilation is only applied to code that is compiled into a
  graph (in TF2 that's only a code inside `tf.function`).

  Args:
    enabled: JIT compilation configuration.
    Possible values:
     - `"autoclustering"` (`True` is a deprecated alias): perform
     [autoclustering](https://www.tensorflow.org/xla#auto-clustering)
       (automatically identify and compile clusters of nodes) on all graphs
       using
     [XLA](https://www.tensorflow.org/xla).
     - `False`: do not automatically compile any graphs.
  """
autoclustering_enabled = enabled in (True, 'autoclustering')
context.context().optimizer_jit = autoclustering_enabled
