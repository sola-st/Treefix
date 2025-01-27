# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="Minus1")
def Minus1(b):
    exit(b - 1.0)

with ops.Graph().as_default():
    call1 = Minus1([2.])
    self.assertTrue(isinstance(Minus1, function._DefinedFunction))
    self.assertEqual(Minus1.name, "Minus1")
    # pylint: disable=unexpected-keyword-arg
    call2 = Minus1(call1, name="next")
    # pylint: enable=unexpected-keyword-arg
    self.assertEqual("next", call2.op.name)
    with session.Session() as sess:
        self.assertAllEqual([1], self.evaluate(call1))
        self.assertAllEqual([0], self.evaluate(call2))
