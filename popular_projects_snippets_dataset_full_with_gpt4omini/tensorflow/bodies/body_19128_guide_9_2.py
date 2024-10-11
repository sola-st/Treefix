n = 10 # pragma: no cover
q = 3 # pragma: no cover
d = 5 # pragma: no cover
scalar = 1.0 # pragma: no cover
data = None # pragma: no cover
summarize = 3 # pragma: no cover
message = 'Shape mismatch detected!' # pragma: no cover
name = 'assert_shapes_test' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
from l3.Runtime import _l_
"""Assert tensor shapes and dimension size relationships between tensors.

  This Op checks that a collection of tensors shape relationships
  satisfies given constraints.

  Example:

  >>> n = 10
  >>> q = 3
  >>> d = 7
  >>> x = tf.zeros([n,q])
  >>> y = tf.ones([n,d])
  >>> param = tf.Variable([1.0, 2.0, 3.0])
  >>> scalar = 1.0
  >>> tf.debugging.assert_shapes([
  ...  (x, ('N', 'Q')),
  ...  (y, ('N', 'D')),
  ...  (param, ('Q',)),
  ...  (scalar, ()),
  ... ])

  >>> tf.debugging.assert_shapes([
  ...   (x, ('N', 'D')),
  ...   (y, ('N', 'D'))
  ... ])
  Traceback (most recent call last):
  ...
  ValueError: ...

  If `x`, `y`, `param` or `scalar` does not have a shape that satisfies
  all specified constraints, `message`, as well as the first `summarize` entries
  of the first encountered violating tensor are printed, and
  `InvalidArgumentError` is raised.

  Size entries in the specified shapes are checked against other entries by
  their __hash__, except:
    - a size entry is interpreted as an explicit size if it can be parsed as an
      integer primitive.
    - a size entry is interpreted as *any* size if it is None or '.'.

  If the first entry of a shape is `...` (type `Ellipsis`) or '*' that indicates
  a variable number of outer dimensions of unspecified size, i.e. the constraint
  applies to the inner-most dimensions only.

  Scalar tensors and specified shapes of length zero (excluding the 'inner-most'
  prefix) are both treated as having a single dimension of size one.

  Args:
    shapes: dictionary with (`Tensor` to shape) items, or a list of
      (`Tensor`, shape) tuples. A shape must be an iterable.
    data: The tensors to print out if the condition is False.  Defaults to error
      message and first few entries of the violating tensor.
    summarize: Print this many entries of the tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_shapes".

  Raises:
    ValueError:  If static checks determine any shape constraint is violated.
  """
assert_shapes(
    shapes, data=data, summarize=summarize, message=message, name=name)
_l_(7256)
