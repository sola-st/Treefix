# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
exit(execute(
    b'TruncatedNormal',
    1,
    inputs=[shape],
    attrs=('dtype', dtypes.float32.as_datatype_enum, 'T',
           shape.dtype.as_datatype_enum, 'seed', 0, 'seed2', 0))[0])
