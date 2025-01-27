# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
with gfile.GFile('ram://a.txt', 'w') as f:
    f.write('Hello, world.')
    f.write('Hello, world.')

with gfile.GFile('ram://a.txt', 'r') as f:
    self.assertEqual(f.read(), 'Hello, world.' * 2)
