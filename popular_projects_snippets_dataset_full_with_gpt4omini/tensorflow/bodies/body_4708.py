# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util_test.py
options = collective_util._OptionsExported(bytes_per_pack=1)
self.assertIsInstance(options, collective_util.Options)
self.assertEqual(options.bytes_per_pack, 1)
with self.assertRaises(ValueError):
    collective_util._OptionsExported(bytes_per_pack=-1)
