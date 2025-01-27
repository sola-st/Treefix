# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
tags = {tag_constants.SERVING}
signature_def_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY

# Create and save a simple model that involves a hash table.
inputs, outputs = self._create_and_save_vocab_table_lookup_qat_model_tf1(
    self._input_saved_model_path, tags, signature_def_key
)

# Make sure that the desired input key and output key is present.
self.assertIn('input_vocabs', inputs.keys())
self.assertIn('lookup', outputs.keys())

# Representative dataset is composed of a set of vocabs for table lookup.
repr_ds = [
    {'input_vocabs': np.array([b'hello', b'model', b'quantization'])}
    for _ in range(4)
]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

signature_def_keys = [signature_def_key]

quantize_model.quantize(
    self._input_saved_model_path,
    signature_def_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=repr_ds,
)

# Tests table lookup to make sure the table has been initialized
# successfully.
with session.Session(graph=ops.Graph()) as sess:
    output_meta_graph_def = saved_model_loader.load(
        sess, tags=tags, export_dir=self._output_saved_model_path
    )

    # The graph should contain a quantized function call (it contains a
    # single f32 matmul node).
    self.assertTrue(
        self._contains_quantized_function_call(
            output_meta_graph_def.graph_def
        )
    )
    self.assertCountEqual(
        output_meta_graph_def.signature_def.keys(), signature_def_keys
    )

    signature_def = output_meta_graph_def.signature_def[signature_def_key]

    input_tensor_name = signature_def.inputs['input_vocabs'].name
    input_tensor = sess.graph.get_tensor_by_name(input_tensor_name)

    lookup_tensor_name = signature_def.outputs['lookup'].name
    lookup_tensor = sess.graph.get_tensor_by_name(lookup_tensor_name)

    lookup_val = sess.run(
        lookup_tensor,
        feed_dict={
            input_tensor: np.array([b'model', b'quantization', b'hello'])
        },
    )

    self.assertAllClose(lookup_val, [1.0, 2.0, 0.0])
