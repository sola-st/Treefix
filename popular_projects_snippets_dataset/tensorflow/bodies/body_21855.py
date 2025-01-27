# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    love_me = constant_op.constant("Love Me")
    love_me_two_times = inp.limit_epochs(love_me, num_epochs=2)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    self.assertEqual(b"Love Me", self.evaluate(love_me_two_times))
    self.assertEqual(b"Love Me", self.evaluate(love_me_two_times))
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(love_me_two_times)
