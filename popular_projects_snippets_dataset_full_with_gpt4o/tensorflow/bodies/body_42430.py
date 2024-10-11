# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
shape = constant_op.constant([], dtype=dtypes.int32)

# x: Run the "TruncatedNormal" op CPU and copy result to GPU.
x = truncated_normal(shape).gpu()
# y: Explicitly run the "TruncatedNormal" op on GPU.
with context.device('gpu:0'):
    y = truncated_normal(shape)
# Add would fail if x and y were not on the same device.
execute(
    b'Add', 1, inputs=[x, y], attrs=('T', x.dtype.as_datatype_enum))
