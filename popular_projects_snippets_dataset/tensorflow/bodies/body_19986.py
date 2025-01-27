# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
opt = optimizer(clipvalue=1.)
self.assertEqual(-1., opt.clip_gradient_min)
self.assertEqual(1., opt.clip_gradient_max)
