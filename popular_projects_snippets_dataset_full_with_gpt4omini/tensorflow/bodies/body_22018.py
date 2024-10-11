# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create old and new vocabs for sparse column "sc_vocab".
prev_vocab_path = self._write_vocab(["apple", "banana", "guava", "orange"],
                                    "old_vocab")
new_vocab_path = self._write_vocab(
    ["orange", "guava", "banana", "apple", "raspberry",
     "blueberry"], "new_vocab")
# Create feature columns.
sc_hash = fc.categorical_column_with_hash_bucket(
    "sc_hash", hash_bucket_size=15)
sc_keys = fc.categorical_column_with_vocabulary_list(
    "sc_keys", vocabulary_list=["a", "b", "c", "e"])
sc_vocab = fc.categorical_column_with_vocabulary_file(
    "sc_vocab", vocabulary_file=new_vocab_path, vocabulary_size=6)
all_linear_cols = [sc_hash, sc_keys, sc_vocab]

# Save checkpoint from which to warm-start.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        variable_scope.get_variable(
            "linear_model/sc_hash/weights", shape=[15, 1], initializer=norms())
        variable_scope.get_variable(
            "some_other_name", shape=[4, 1], initializer=rand())
        variable_scope.get_variable(
            "linear_model/sc_vocab/weights",
            initializer=[[0.5], [1.], [2.], [3.]])
        self._write_checkpoint(sess)

def _partitioner(shape, dtype):  # pylint:disable=unused-argument
    # Partition each var into 2 equal slices.
    partitions = [1] * len(shape)
    partitions[0] = min(2, shape.dims[0].value)
    exit(partitions)

# New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = self._create_linear_model(all_linear_cols, _partitioner)
        vocab_info = ws_util.VocabInfo(
            new_vocab=sc_vocab.vocabulary_file,
            new_vocab_size=sc_vocab.vocabulary_size,
            num_oov_buckets=sc_vocab.num_oov_buckets,
            old_vocab=prev_vocab_path)
        ws_util.warm_start(
            self.get_temp_dir(),
            # The special value of None here will ensure that only the variable
            # specified in var_name_to_vocab_info (sc_vocab embedding) is
            # warm-started.
            vars_to_warm_start=None,
            var_name_to_vocab_info={
                ws_util._infer_var_name(cols_to_vars[sc_vocab]): vocab_info
            },
            # Even though this is provided, the None value for
            # vars_to_warm_start overrides the logic, and this will not be
            # warm-started.
            var_name_to_prev_var_name={
                ws_util._infer_var_name(cols_to_vars[sc_keys]):
                    "some_other_name"
            })
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started.  Var corresponding to
        # sc_vocab should be correctly warm-started after vocab remapping,
        # and neither of the other two should be warm-started..
        self._assert_cols_to_vars(cols_to_vars, {
            sc_keys: [np.zeros([2, 1]), np.zeros([2, 1])],
            sc_hash: [np.zeros([8, 1]), np.zeros([7, 1])],
            sc_vocab: [
                np.array([[3.], [2.], [1.]]),
                np.array([[0.5], [0.], [0.]])
            ]
        }, sess)
