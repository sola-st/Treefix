# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py
self.assertEqual(
    "object_path/.ATTRIBUTES/",
    restore._extract_saveable_name("object_path/.ATTRIBUTES/123"))
self.assertEqual(
    "object/path/ATTRIBUTES/.ATTRIBUTES/",
    restore._extract_saveable_name("object/path/ATTRIBUTES/.ATTRIBUTES/"))
