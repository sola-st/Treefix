# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
for i in range(10):
    with gfile.GFile('ram://a/b/%d.txt' % i, 'w') as f:
        f.write('')
    with gfile.GFile('ram://c/b/%d.txt' % i, 'w') as f:
        f.write('')

matches = ['%d.txt' % i for i in range(10)]
self.assertEqual(gfile.ListDirectory('ram://a/b/'), matches)
