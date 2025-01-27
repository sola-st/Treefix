# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
if input_shape[0] is None:
    output_shape = None
else:
    output_shape = input_shape[0][1:]
for i in range(1, len(input_shape)):
    if input_shape[i] is None:
        shape = None
    else:
        shape = input_shape[i][1:]
    output_shape = self._compute_elemwise_op_output_shape(output_shape, shape)
batch_sizes = {s[0] for s in input_shape if s is not None} - {None}
if len(batch_sizes) == 1:
    output_shape = (list(batch_sizes)[0],) + output_shape
else:
    output_shape = (None,) + output_shape
exit(output_shape)
