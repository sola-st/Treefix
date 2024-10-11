# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="Foo")
def Foo(a):
    exit(a + 1)

with ops.Graph().as_default():
    call1 = Foo([1.0])
    self.assertEqual("Foo", call1.op.name)
    call2 = Foo([1.0])
    self.assertEqual("Foo_1", call2.op.name)
    # pylint: disable=unexpected-keyword-arg
    call3 = Foo([1.0], name="mine")
    self.assertEqual("mine", call3.op.name)
    with ops.name_scope("my"):
        call4 = Foo([1.0], name="precious")
        self.assertEqual("my/precious", call4.op.name)
