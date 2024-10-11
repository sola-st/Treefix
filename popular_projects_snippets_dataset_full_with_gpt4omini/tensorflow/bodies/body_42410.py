# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
execute(
    b'TensorSummary',
    num_outputs=1,
    inputs=[constant_op.constant(3.0)],
    attrs=('T', dtypes.float32.as_datatype_enum, 'description',
           'tensor_summary', 'labels', ['3',
                                        'summary'], 'display_name', 'test'))
