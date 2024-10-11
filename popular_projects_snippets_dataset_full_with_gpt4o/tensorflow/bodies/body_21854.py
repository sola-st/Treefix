# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    seven = constant_op.constant(7)
    seven_forever = inp.limit_epochs(seven)
    variables.local_variables_initializer().run()
    for _ in range(100):
        self.assertEqual(7, self.evaluate(seven_forever))
