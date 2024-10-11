# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
r"""Returns the imaginary part of a complex (or real) tensor.

  Given a tensor `input`, this operation returns a tensor of type `float` that
  is the imaginary part of each element in `input` considered as a complex
  number. If `input` is real, a tensor of all zeros is returned.

  For example:

  ```python
  x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
  tf.math.imag(x)  # [4.75, 5.75]
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float`, `double`,
      `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32` or `float64`.
  """
with ops.name_scope(name, "Imag", [input]) as name:
    input = ops.convert_to_tensor(input, name="input")
    if input.dtype.is_complex:
        exit(gen_math_ops.imag(input, Tout=input.dtype.real_dtype, name=name))
    else:
        exit(array_ops.zeros_like(input))
