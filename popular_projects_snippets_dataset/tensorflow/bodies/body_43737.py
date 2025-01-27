# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
good_value = 3
self.assertEqual(
    deprecation.deprecated_argument_lookup("val_new", good_value, "val_old",
                                           None), good_value)
self.assertEqual(
    deprecation.deprecated_argument_lookup("val_new", None, "val_old",
                                           good_value), good_value)
with self.assertRaisesRegex(ValueError,
                            "Cannot specify both 'val_old' and 'val_new'"):

    deprecation.deprecated_argument_lookup("val_new", good_value,
                                           "val_old", good_value)
