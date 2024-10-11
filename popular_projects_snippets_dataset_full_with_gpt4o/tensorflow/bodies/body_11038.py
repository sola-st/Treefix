# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
self.assertEqual(len(nest.flatten(y_struct)),
                 len(nest.flatten(dy)))
exit(nest.flatten(Zeros(x_struct)))
