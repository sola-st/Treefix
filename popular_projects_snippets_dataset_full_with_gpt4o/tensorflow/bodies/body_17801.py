# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
pfor_jacobian, while_gradients = create_dynamic_lstm_batch_jacobian(8, 4, 3)
with session.Session() as sess:
    init = variables.global_variables_initializer()
    self.evaluate(init)
    pfor = self.evaluate(pfor_jacobian)
    for i in range(4):
        while_i = sess.run(while_gradients[i])
        self.assertAllClose(while_i, pfor[:, i, ...])
