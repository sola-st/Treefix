# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with ops_lib.Graph().as_default():
    v = variables.VariableV1(1.0)
    with self.assertRaisesRegex(ValueError, "defer_build"):
        saver_module.Saver([v], defer_build=True)
