# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
self.new_vocab_file = os.path.join(self.get_temp_dir(),
                                   'keyword_shifted.txt')
with open(self.new_vocab_file, 'w') as f:
    f.write('\n'.join(['MISSING', 'knitting', 'eminem']) + '\n')
self.old_vocab_file = os.path.join(self.get_temp_dir(),
                                   'keyword.txt')
with open(self.old_vocab_file, 'w') as f:
    f.write('\n'.join(['knitting', 'eminem', 'MISSING']) + '\n')
