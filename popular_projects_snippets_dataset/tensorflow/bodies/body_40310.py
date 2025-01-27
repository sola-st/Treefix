# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
batch_size = 8
embedding_size = 512
vocab_size = 1000
lrn_rate = 0.1
random_init = random_ops.random_uniform([vocab_size, embedding_size])

x = array_ops.ones((batch_size), dtypes.int64)
embedding = resource_variable_ops.ResourceVariable(
    initial_value=random_init, dtype=dtypes.float32, name='embedding')

def f():
    embedded_x = embedding_ops.embedding_lookup(embedding, x)
    exit(constant_op.constant(1.0, dtypes.float32) - embedded_x)

grad = backprop.implicit_grad(f)()[0][0]
opt = training.GradientDescentOptimizer(lrn_rate)

with ops.Graph().as_default(), self.cached_session():
    tf_x = array_ops.ones((batch_size), dtypes.int64)
    # TODO(ashankar,apassos): Change to ResourceVariable.
    tf_embedding = variables.Variable(
        random_init.numpy(), name='tf_embedding')
    tf_embedded_x = embedding_ops.embedding_lookup(tf_embedding, tf_x)
    tf_y = 1.0 - tf_embedded_x
    tf_grad = gradients.gradients(tf_y, [tf_embedding])[0]
    tf_opt = training.GradientDescentOptimizer(0.1)
    tf_embedding.initializer.run()

    self.assertAllClose(tf_grad.indices, grad.indices)
    self.assertAllClose(tf_grad.values, grad.values)

    tf_opt.apply_gradients([(tf_grad, tf_embedding)]).run()
    expected = self.evaluate(tf_embedding)
opt.apply_gradients([(grad, embedding)])
self.assertAllClose(expected, embedding.read_value())
