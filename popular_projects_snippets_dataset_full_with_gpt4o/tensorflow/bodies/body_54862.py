# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertEqual(unbatched._batch(batch_size), batched)
self.assertEqual(batched._unbatch(), unbatched)
