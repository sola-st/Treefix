# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
opt1 = optimizer(0.1)
opt2 = optimizer(0.1)
opt3 = optimizer(0.2)
self.assertEqual(opt1, opt2)
self.assertEqual(hash(opt1), hash(opt2))
self.assertNotEqual(opt1, opt3)
self.assertNotEqual(hash(opt1), hash(opt3))
