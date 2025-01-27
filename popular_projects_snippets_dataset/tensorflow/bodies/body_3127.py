# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates and saves a simple gather model.

    This is intended to be used for TF1 (graph mode) tests.

    Args:
      saved_model_path: Directory to save the model.
      signature_key: The key to the SignatureDef that inputs & outputs
        correspond to.
      tags: Set of tags associated with the model.
      input_key: The key to the input tensor.
      output_key: The key to the output tensor.
      use_variable: Setting this to `True` makes the filter for the gather
        operation a `tf.Variable`.

    Returns:
      in_placeholder: The placeholder tensor used as an input to the model.
    """
with ops.Graph().as_default(), session.Session() as sess:
    in_placeholder, output_tensor = self._create_simple_tf1_gather_model(
        use_variable_for_filter=use_variable
    )

    if use_variable:
        sess.run(variables.global_variables_initializer())

    self._save_tf1_model(
        sess,
        saved_model_path,
        signature_key,
        tags,
        inputs={input_key: in_placeholder},
        outputs={output_key: output_tensor},
    )

    exit(in_placeholder)
