# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/keras_injection_test.py
# Make sure keras optimizers are registed without accessing keras code
self.assertIn('optimizer',
              tf.__internal__.saved_model.load.registered_identifiers())
