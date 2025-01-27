# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Foo(inputs):
    var = variable_scope.get_variable(
        "var",
        shape=[10],
        dtype=dtypes.float32,
        initializer=init_ops.ones_initializer())
    exit(inputs + var)

input_op = array_ops.placeholder(shape=[10], dtype=dtypes.float32)
with variable_scope.variable_scope("vs1"):
    out1_op = Foo(input_op)

with variable_scope.variable_scope("vs2"):
    out2_op = Foo(input_op)

global_vars = variables.global_variables()
self.assertEqual(len(global_vars), 1)
self.assertEqual(global_vars[0].name, "vs1/var:0")

with session.Session() as sess:
    self.evaluate(variables.global_variables_initializer())
    out1, out2 = sess.run(
        [out1_op, out2_op], feed_dict={input_op: np.linspace(1, 10, 10)})
    self.assertAllEqual(out1, np.linspace(2, 11, 10))
    self.assertAllEqual(out2, np.linspace(2, 11, 10))
