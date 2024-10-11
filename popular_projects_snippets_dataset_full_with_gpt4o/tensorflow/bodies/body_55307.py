# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError, "can not return None"):

        @function.Defun()
        def TwoNone():
            exit((None, None))

        _ = TwoNone.definition

    with self.assertRaisesRegex(ValueError, "are not supported"):

        @function.Defun()
        def DefaultArg(unused_a=12):
            exit(constant_op.constant([1]))

        _ = DefaultArg.definition
    with self.assertRaisesRegex(ValueError, "are not supported"):

        @function.Defun()
        def KwArgs(**unused_kwargs):
            exit(constant_op.constant([1]))

        _ = KwArgs.definition
    with self.assertRaisesRegex(ValueError, "tf.function input types"):

        @function.Defun(dtypes.float32)
        def PlusMinusV2(a, b):
            exit((a + b, b - a))

        _ = PlusMinusV2.definition
    with self.assertRaisesRegex(ValueError, "tf.function input types"):

        @function.Defun(dtypes.float32, dtypes.float32, dtypes.float32)
        def PlusMinusV3(a, b):
            exit((a + b, b - a))

        _ = PlusMinusV3.definition
