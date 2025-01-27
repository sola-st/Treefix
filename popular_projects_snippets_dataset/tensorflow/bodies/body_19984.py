# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
with self.assertRaisesRegex(ValueError, 'accumulation'):
    optimizer(use_gradient_accumulation=False, clipvalue=0.)
with self.assertRaisesRegex(ValueError, 'accumulation'):
    optimizer(use_gradient_accumulation=False, clipvalue=(None, 1.))
