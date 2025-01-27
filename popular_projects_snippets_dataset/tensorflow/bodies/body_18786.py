# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Replaces the global generator with another `Generator` object.

  This function replaces the global generator with the provided `generator`
  object.
  A random number generator utilizes a `tf.Variable` object to store its state.
  The user shall be aware of caveats how `set_global_generator` interacts with
  `tf.function`:

  - tf.function puts restrictions on Variable creation thus one cannot freely
    create a new random generator instance inside `tf.function`.
    To call `set_global_generator` inside `tf.function`, the generator instance
    must have already been created eagerly.
  - tf.function captures the Variable during trace-compilation, thus a compiled
    f.function will not be affected `set_global_generator` as demonstrated by
    random_test.py/RandomTest.testResetGlobalGeneratorBadWithDefun .

  For most use cases, avoid calling `set_global_generator` after program
  initialization, and prefer to reset the state of the existing global generator
  instead, such as,

  >>> rng = tf.random.get_global_generator()
  >>> rng.reset_from_seed(30)


  Args:
    generator: the new `Generator` object.
  """
global global_generator
global_generator = generator
