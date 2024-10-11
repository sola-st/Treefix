# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/generator_test.py
with self.assertRaisesRegex(NotImplementedError, 'generators'):
    tf.function(basic_generator)()
