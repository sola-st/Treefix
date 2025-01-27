# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
suffix = "/.ATTRIBUTES/VARIABLE_VALUE"
self.assertEqual(r"a.Sb.Sc" + suffix, self._get_checkpoint_name(r"a/b/c"))
self.assertEqual(r"b" + suffix, self._get_checkpoint_name(r"b"))
self.assertEqual(r"c.S" + suffix, self._get_checkpoint_name(r"c/"))
self.assertEqual(r"d.S..S" + suffix, self._get_checkpoint_name(r"d/.S"))
self.assertEqual(r"d.S..ATTRIBUTES.Sf" + suffix,
                 self._get_checkpoint_name(r"d/.ATTRIBUTES/f"))
