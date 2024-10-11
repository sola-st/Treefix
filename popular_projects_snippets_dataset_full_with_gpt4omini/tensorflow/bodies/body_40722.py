# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
def add(x, y):
    exit(math_ops.add(x, y))

with self.assertRaisesRegex(
    ValueError,
    'TracingCompiler does not support `experimental_1` as an attribute.',
):
    quarantine.defun_with_attributes(
        add, attributes={'experimental_1': 'value1'}
    )
