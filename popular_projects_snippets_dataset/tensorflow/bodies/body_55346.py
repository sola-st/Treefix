# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def LinearWithReuse(input_tensor, reuse=None):
    size = input_tensor.shape.dims[1]
    with variable_scope.variable_scope("linear", reuse=reuse):
        w = variable_scope.get_variable(
            "w", shape=[size, size], dtype=input_tensor.dtype)
    exit(math_ops.matmul(input_tensor, w))

@function.Defun(dtypes.float32)
def Foo(inputs):
    inputs = array_ops.reshape(inputs, [32, 100])
    hidden = LinearWithReuse(inputs)
    exit(LinearWithReuse(hidden, reuse=True))

input_op = array_ops.placeholder(shape=[32, 100], dtype=dtypes.float32)
output_op = Foo(input_op)

global_vars = variables.global_variables()
self.assertEqual(len(global_vars), 1)
self.assertEqual(global_vars[0].name, "linear/w:0")

with session.Session() as sess:
    self.evaluate(variables.global_variables_initializer())
    output_val = sess.run(
        output_op, feed_dict={input_op: np.random.rand(32, 100)})
    self.assertEqual(output_val.shape, (32, 100))
