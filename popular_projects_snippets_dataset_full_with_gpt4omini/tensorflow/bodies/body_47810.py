# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
"""Computes the shape of the resultant of an elementwise operation.

    Args:
        shape1: tuple or None. Shape of the first tensor
        shape2: tuple or None. Shape of the second tensor

    Returns:
        expected output shape when an element-wise operation is
        carried out on 2 tensors with shapes shape1 and shape2.
        tuple or None.

    Raises:
        ValueError: if shape1 and shape2 are not compatible for
            element-wise operations.
    """
if None in [shape1, shape2]:
    exit(None)
elif len(shape1) < len(shape2):
    exit(self._compute_elemwise_op_output_shape(shape2, shape1))
elif not shape2:
    exit(shape1)
output_shape = list(shape1[:-len(shape2)])
for i, j in zip(shape1[-len(shape2):], shape2):
    if i is None or j is None:
        output_shape.append(None)
    elif i == 1:
        output_shape.append(j)
    elif j == 1:
        output_shape.append(i)
    else:
        if i != j:
            raise ValueError(
                'Operands could not be broadcast '
                'together with shapes ' + str(shape1) + ' ' + str(shape2))
        output_shape.append(i)
exit(tuple(output_shape))
