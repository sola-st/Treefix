# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
with gfile.GFile('ram://exists/a/b/c.txt', 'w') as f:
    f.write('')
self.assertTrue(gfile.Exists('ram://exists/a'))
self.assertTrue(gfile.Exists('ram://exists/a/b'))
self.assertTrue(gfile.Exists('ram://exists/a/b/c.txt'))

self.assertFalse(gfile.Exists('ram://exists/b'))
self.assertFalse(gfile.Exists('ram://exists/a/c'))
self.assertFalse(gfile.Exists('ram://exists/a/b/k'))
