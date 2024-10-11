# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates a simple QAT model that initializes and lookups a vocab table.

    This model creates an asset file at "vocab_file.txt" containing
    comma-separated vocabularies.  It also initializes a `StaticVocabularyTable`
    and performs a lookup with the input vocabs, which is a 1D tensor of
    strings.

    Args:
      sess: Tensorflow Session to create the model in.

    Returns:
      (input_vocabs_placeholder, lookup_vals, output_tensor), where
      * input_vocabs_placeholder is a placeholder tensor of 1D strings
      * lookup_vals is an output tensor that is a direct result of table lookup
      * output_tensor is a float 2x2 matrix
    """
# Creates and populates an asset file.
asset_dir = self.create_tempdir('assets').full_path
asset_file = os.path.join(asset_dir, 'vocab_file.txt')
file_io.write_string_to_file(
    filename=asset_file, file_content='hello,model,quantization\n'
)

vocab_file = asset.Asset(asset_file)

raw_vocab = io_ops.read_file(vocab_file)
vocabs = ragged_string_ops.string_split_v2(
    string_ops.string_strip(raw_vocab), sep=','
)

# Initialize the vocab table. Each comma-separated word in vocab_file.txt
# corresponds to the numeric identifiers in `values`.
kv_init = lookup_ops.KeyValueTensorInitializer(
    keys=vocabs, values=np.array([0, 1, 2]), value_dtype=dtypes.int64
)
table = lookup_ops.StaticVocabularyTable(kv_init, num_oov_buckets=5)

input_vocabs_placeholder = array_ops.placeholder(
    dtypes.string, shape=(None,), name='input_vocabs'
)

# Introduce a matmul op that takes the lookup values to observe the
# effects of quantization.
lookup_vals = math_ops.cast(
    table.lookup(input_vocabs_placeholder), dtypes.float32
)

# shape: (2, ?)
matmul_input = array_ops.stack([lookup_vals, lookup_vals])
# Insert fake quant to simulate a QAT model.
matmul_input = array_ops.fake_quant_with_min_max_args(
    matmul_input, min=-0.3, max=0.3, num_bits=8, narrow_range=False
)

# Create a dummy weight matrix filled with ones.
weight_row = array_ops.ones(
    shape=array_ops.shape(input_vocabs_placeholder), dtype=dtypes.float32
)

# shape: (?, 2)
weight = array_ops.transpose_v2(array_ops.stack([weight_row, weight_row]))
# Insert fake quant to simulate a QAT model.
weight = array_ops.fake_quant_with_min_max_args(
    weight, min=-0.1, max=0.2, num_bits=8, narrow_range=False
)

# shape: (2, 2)
output_tensor = math_ops.matmul(matmul_input, weight)
# Insert fake quant to simulate a QAT model.
output_tensor = array_ops.fake_quant_with_min_max_args(
    output_tensor, min=-0.2, max=0.2, num_bits=8, narrow_range=False
)

exit((input_vocabs_placeholder, lookup_vals, output_tensor))
