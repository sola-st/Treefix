# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Enable or disable the use of TensorFloat-32 on supported hardware.

  [TensorFloat-32](https://blogs.nvidia.com/blog/2020/05/14/tensorfloat-32-precision-format),
  or TF32 for short, is a math mode for NVIDIA Ampere GPUs. TensorFloat-32
  execution causes certain float32 ops, such as matrix multiplications and
  convolutions, to run much faster on Ampere GPUs but with reduced precision.
  This reduced precision should not impact convergence of deep learning models
  in practice.

  TensorFloat-32 is enabled by default. TensorFloat-32 is only supported on
  Ampere GPUs, so all other hardware will use the full float32 precision
  regardless of whether TensorFloat-32 is enabled or not. If you want to use the
  full float32 precision on Ampere, you can disable TensorFloat-32 execution
  with this function. For example:

  ```python
  x = tf.fill((2, 2), 1.0001)
  y = tf.fill((2, 2), 1.)
  # TensorFloat-32 is enabled, so matmul is run with reduced precision
  print(tf.linalg.matmul(x, y))  # [[2., 2.], [2., 2.]]
  tf.config.experimental.enable_tensor_float_32_execution(False)
  # Matmul is run with full precision
  print(tf.linalg.matmul(x, y))  # [[2.0002, 2.0002], [2.0002, 2.0002]]
  ```

  To check whether TensorFloat-32 execution is currently enabled, use
  `tf.config.experimental.tensor_float_32_execution_enabled`.

  If TensorFloat-32 is enabled, float32 inputs of supported ops, such as
  `tf.linalg.matmul`, will be rounded from 23 bits of precision to 10 bits of
  precision in most cases. This allows the ops to execute much faster by
  utilizing the GPU's tensor cores. TensorFloat-32 has the same dynamic range as
  float32, meaning it is no more likely to underflow or overflow than float32.
  Ops still use float32 accumulation when TensorFloat-32 is enabled. Enabling or
  disabling TensorFloat-32 only affects Ampere GPUs and subsequent GPUs that
  support TensorFloat-32.

  Note TensorFloat-32 is not always used in supported ops, as only inputs of
  certain shapes are supported. Support for more input shapes and more ops may
  be added in the future. As a result, precision of float32 ops may decrease in
  minor versions of TensorFlow.

  TensorFloat-32 is also used for some complex64 ops. Currently, TensorFloat-32
  is used in fewer cases for complex64 as it is for float32.

  Args:
    enabled: Bool indicating whether to enable TensorFloat-32 execution.
  """
_pywrap_tensor_float_32_execution.enable(enabled)
