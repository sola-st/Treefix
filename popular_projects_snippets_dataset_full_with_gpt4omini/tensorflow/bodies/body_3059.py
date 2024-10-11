# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/hash_table_asset_v1.py

vocabulary_file = write_vocabulary_file(['cat', 'is', 'on', 'the', 'mat'])
table_initializer = tf.lookup.TextFileInitializer(
    vocabulary_file, tf.string, tf.lookup.TextFileIndex.WHOLE_LINE, tf.int64,
    tf.lookup.TextFileIndex.LINE_NUMBER)
# Incur another bound_input on the asset, but with a different sym_name, i.e.,
# __tf_saved_model_asset1_tokens.txt vs. __tf_saved_model_asset0_tokens.txt.
table = tf.lookup.StaticVocabularyTable(table_initializer, num_oov_buckets=10)
vocab_file_tensor = tf.convert_to_tensor(
    vocabulary_file, tf.string, name='asset_filepath')
tf.add_to_collection(tf.GraphKeys.ASSET_FILEPATHS, vocab_file_tensor)

x = tf.placeholder(tf.string, shape=(), name='input')
r = table.lookup(x)

tensor_info_x = tf.compat.v1.saved_model.utils.build_tensor_info(x)
tensor_info_r = tf.compat.v1.saved_model.utils.build_tensor_info(r)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name='some_function'))
}, tf.tables_initializer(), tf.get_collection(tf.GraphKeys.ASSET_FILEPATHS)))
