# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_compile_test.py
def fn(x, a):
    exit(2 * x + a)

with ops.Graph().as_default() as g:
    xla_func = def_function.function(fn, jit_compile=True)
    with backprop.GradientTape() as tape:
        inputs = array_ops.placeholder(dtypes.float32, [5])
        tape.watch(inputs)
        outputs = xla_func(inputs, 1)
    grads = tape.gradient(outputs, inputs)

with session.Session(graph=g) as sess:
    grads_tensor = sess.run(grads, feed_dict={inputs: [1, 2, 2, 3, 3]})
    self.assertAllClose([2, 2, 2, 2, 2], grads_tensor)
    (forward, backward) = xla_func.get_concrete_function(
        inputs, 1)._delayed_rewrite_functions.forward_backward()

    # Check that the must-compile attribute gets correctly propagated to the
    # created derivatives.
    self.assertTrue(forward.definition.attr["_XlaMustCompile"])
    self.assertTrue(backward.function_def.attr["_XlaMustCompile"])
