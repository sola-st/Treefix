# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt = MaskedTensorV2.from_full_tensor([1, 2, 3, 4])
self.assertAllEqual(mt.mask, [True, True, True, True])
self.assertEqual(mt.doc_link(), 'http://example.com/masked_tensor')
