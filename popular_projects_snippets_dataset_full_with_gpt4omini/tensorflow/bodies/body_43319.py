# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
with self.assertRaisesRegex(TypeError,
                            'should be a callable'):
    function_utils.has_kwargs('not a function')
