# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Expecting a Dimension for attr shape, got object'):
    execute(
        b'VarHandleOp',
        num_outputs=1,
        inputs=[],
        attrs=('shape', [object()], 'dtype', dtypes.int32.as_datatype_enum,
               'container', '', 'shared_name', ''))
