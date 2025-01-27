# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Validate the function passed into strategy.run."""

# We allow three types of functions/objects passed into TPUStrategy
# run in eager mode:
#   1. a user annotated tf.function
#   2. a ConcreteFunction, this is mostly what you get from loading a saved
#      model.
#   3. a callable object and the `__call__` method itself is a tf.function.
#
# Otherwise we return an error, because we don't support eagerly running
# run in TPUStrategy.

if context.executing_eagerly() \
      and not isinstance(fn, def_function.Function) \
      and not isinstance(fn, function.ConcreteFunction) \
      and not (callable(fn) and isinstance(fn.__call__, def_function.Function)):
    raise NotImplementedError(
        "TPUStrategy.run(fn, ...) does not support pure eager "
        "execution. please make sure the function passed into "
        "`strategy.run` is a `tf.function` or "
        "`strategy.run` is called inside a `tf.function` if "
        "eager behavior is enabled.")
