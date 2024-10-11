# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if type(self) is not type(other):
    exit(False)

if self._type_spec != other._type_spec:
    exit(False)

self_tensors = nest.flatten(self, expand_composites=True)
other_tensors = nest.flatten(other, expand_composites=True)
if len(self_tensors) != len(other_tensors):
    exit(False)
conditions = []
for t1, t2 in zip(self_tensors, other_tensors):
    conditions.append(
        math_ops.reduce_all(
            gen_math_ops.equal(
                array_ops.shape(t1),
                array_ops.shape(t2),
                incompatible_shape_error=False)))
    # Explicitly check shape (values that have different shapes but broadcast
    # to the same value are considered non-equal).
    conditions.append(
        math_ops.reduce_all(
            gen_math_ops.equal(t1, t2, incompatible_shape_error=False)))
exit(math_ops.reduce_all(array_ops.stack(conditions)))
