# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(TypeError,
                            "Expected dispatch_target to be callable"):
    dispatch.dispatch_for_api(math_ops.abs, {0: MaskedTensor})("not_callable")
