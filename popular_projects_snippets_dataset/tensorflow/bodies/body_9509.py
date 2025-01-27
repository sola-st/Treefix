# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
steps = 200
inputs = []
outputs = []
a = constant_op.constant(2.0, dtypes.float32)
for i in range(steps):
    inputs.append(array_ops.placeholder(dtypes.float32, shape=[]))
    a = math_ops.multiply(a, inputs[i])
    outputs.append(a)

h = sess.partial_run_setup(outputs, inputs)
for i in range(steps):
    res = sess.partial_run(h, outputs[i], feed_dict={inputs[i]: 1.0})
self.assertEqual(2.0, res)

feed_dict = {}
for i in range(steps):
    feed_dict[inputs[i]] = 1.0
res = sess.run(outputs, feed_dict)
self.assertEqual(steps, len(res))
self.assertEqual(2.0, res[-1])
