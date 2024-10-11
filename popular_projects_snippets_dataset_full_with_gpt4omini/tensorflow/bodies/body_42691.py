# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
# Test case for GitHub issue 26879.
with ops.Graph().as_default():
    a_2_by_2 = constant_op.constant(1.0, shape=[2, 2])
    m = resource_variable_ops.ResourceVariable(a_2_by_2)
    with self.assertRaisesRegex(TypeError,
                                "Expected list for 'values' argument"):
        _ = array_ops.stack(m, axis=1)
