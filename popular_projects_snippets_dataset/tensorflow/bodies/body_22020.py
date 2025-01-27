# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Create old and new vocabs for embedding column "sc_vocab".
prev_vocab_path = self._write_vocab(["apple", "banana", "guava", "orange"],
                                    "old_vocab")
new_vocab_path = self._write_vocab(
    ["orange", "guava", "banana", "apple", "raspberry", "blueberry"],
    "new_vocab")

# Save checkpoint from which to warm-start.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        variable_scope.get_variable(
            "input_layer/sc_vocab_embedding/embedding_weights",
            initializer=[[0.5, 0.4], [1., 1.1], [2., 2.2], [3., 3.3]])
        self._write_checkpoint(sess)

def _partitioner(shape, dtype):  # pylint:disable=unused-argument
    # Partition each var into 2 equal slices.
    partitions = [1] * len(shape)
    partitions[0] = min(2, shape.dims[0].value)
    exit(partitions)

# Create feature columns.
sc_vocab = fc.categorical_column_with_vocabulary_file(
    "sc_vocab", vocabulary_file=new_vocab_path, vocabulary_size=6)
emb_vocab_column = fc.embedding_column(
    categorical_column=sc_vocab,
    dimension=2)
all_deep_cols = [emb_vocab_column]
# New graph, new session with warm-starting.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        cols_to_vars = {}
        with variable_scope.variable_scope("", partitioner=_partitioner):
            # Create the variables.
            fc.input_layer(
                features=self._create_dummy_inputs(),
                feature_columns=all_deep_cols,
                cols_to_vars=cols_to_vars)
        vocab_info = ws_util.VocabInfo(
            new_vocab=sc_vocab.vocabulary_file,
            new_vocab_size=sc_vocab.vocabulary_size,
            num_oov_buckets=sc_vocab.num_oov_buckets,
            old_vocab=prev_vocab_path,
            # Can't use constant_initializer with load_and_remap.  In practice,
            # use a truncated normal initializer.
            backup_initializer=init_ops.random_uniform_initializer(
                minval=0.42, maxval=0.42))
        ws_util.warm_start(
            self.get_temp_dir(),
            var_name_to_vocab_info={
                ws_util._infer_var_name(cols_to_vars[emb_vocab_column]):
                    vocab_info
            })
        self.evaluate(variables.global_variables_initializer())
        # Verify weights were correctly warm-started. Var corresponding to
        # emb_vocab_column should be correctly warm-started after vocab
        # remapping. Missing values are filled in with the EmbeddingColumn's
        # initializer.
        self._assert_cols_to_vars(
            cols_to_vars, {
                emb_vocab_column: [
                    np.array([[3., 3.3], [2., 2.2], [1., 1.1]]),
                    np.array([[0.5, 0.4], [0.42, 0.42], [0.42, 0.42]])
                ]
            }, sess)
