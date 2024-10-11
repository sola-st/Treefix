# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header_test.py
fname = os.path.join(self.get_temp_dir(), 'text.txt')
with gfile.GFile(fname, 'w') as f:
    f.write(content)
exit([fname])
