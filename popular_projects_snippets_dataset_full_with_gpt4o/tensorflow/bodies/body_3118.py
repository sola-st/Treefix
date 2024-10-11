# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates and saves a simple model that uses a vocab table.

    Args:
      output_path: Path to the directory to save the created model.
      tags: Set of strings that identifies the saved meta graph.
      signature_def_key: Name of the SignatureDef. Used to identify the
        SignatureDef within the meta graph.

    Returns:
      inputs: A mapping of input_key -> input_tensor (placeholder). The input
        key is "input_vocabs".
      outputs: A mapping of output_key -> output_tensor. The output keys are
        "lookup" and "output".
    """
with session.Session(graph=ops.Graph()) as sess:
    input_vocabs_placeholder, lookup_tensor, output_tensor = (
        self._create_vocab_table_lookup_model_tf1(sess)
    )

    inputs = {'input_vocabs': input_vocabs_placeholder}
    outputs = {
        'lookup': lookup_tensor,
        'output': output_tensor,
    }

    self._save_tf1_model(
        sess,
        output_path,
        signature_def_key,
        tags,
        inputs=inputs,
        outputs=outputs,
        init_op=lookup_ops.tables_initializer(),
        assets_collection=ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS),
    )

exit((inputs, outputs))
