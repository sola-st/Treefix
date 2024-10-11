# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/hash_table_asset_v1.py
"""Write temporary vocab file for module construction."""
tmpdir = tempfile.mkdtemp()
vocabulary_file = os.path.join(tmpdir, 'tokens.txt')
with tf.io.gfile.GFile(vocabulary_file, 'w') as f:
    for entry in vocabulary:
        f.write(entry + '\n')
exit(vocabulary_file)
