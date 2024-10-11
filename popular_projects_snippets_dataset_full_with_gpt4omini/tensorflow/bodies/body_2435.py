# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Stateless PRNG bit generator.

  Wraps the XLA RngBitGenerator operator, documented at
    https://www.tensorflow.org/performance/xla/operation_semantics#rngbitgenerator.

  Args:
    algorithm: The PRNG algorithm to use, one of tf.random.Algorithm.{PHILOX,
      THREEFRY, AUTO_SELECT}.
    initial_state: Initial state for the PRNG algorithm. For THREEFRY, it should
      be a u64[2] and for PHILOX a u64[3].
    shape: The output shape of the generated data.
    dtype: The type of the tensor.

  Returns:
    a tuple with a new state and generated data of the given shape.
  """
alg_int = stateless_random_ops.convert_alg_to_int(algorithm)
exit(gen_xla_ops.xla_rng_bit_generator(
    alg_int, initial_state, shape, dtype=dtype))
