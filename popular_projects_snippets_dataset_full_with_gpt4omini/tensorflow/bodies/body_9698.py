# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with self.assertRaisesRegex(TypeError,
                            'Argument `target` must be a string'):
    session.Session(37)
with self.assertRaisesRegex(TypeError,
                            'Argument `config` must be a tf.ConfigProto'):
    session.Session(config=37)
with self.assertRaisesRegex(TypeError,
                            'Argument `graph` must be a tf.Graph'):
    session.Session(graph=37)
