# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
with gfile.GFile('ram://c.txt', 'w') as f:
    f.write('Hello, world.')

with gfile.GFile('ram://c.txt', 'w+') as f:
    f.seek(offset=0, whence=2)
    f.write('Hello, world.')

with gfile.GFile('ram://c.txt', 'r') as f:
    self.assertEqual(f.read(), 'Hello, world.' * 2)
