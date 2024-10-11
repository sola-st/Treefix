# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
exit(execute(
    b'Add',
    num_outputs=1,
    inputs=[x, y],
    attrs=('T', dtypes.int32.as_datatype_enum))[0])
