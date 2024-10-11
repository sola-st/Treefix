# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'Barrier',
        num_outputs=1,
        inputs=[],
        attrs=('component_types', dtypes.float64.as_datatype_enum, 'shapes',
               [[1, 2]], 'capacity', -1, 'container', '', 'shared_name', ''))
