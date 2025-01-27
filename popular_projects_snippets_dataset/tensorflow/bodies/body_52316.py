# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
vocab_file = os.path.join(self.get_temp_dir(), file_name)
with open(vocab_file, 'w') as f:
    f.write('\n'.join(vocab_strings))
exit(vocab_file)
