# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'Barrier',
        num_outputs=1,
        inputs=[],
        attrs=('component_types', '1', 'shapes', [[1, 2]], 'capacity', -1,
               'container', '', 'shared_name', ''))
