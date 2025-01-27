# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Saves a TF1 model.

    Args:
      sess: Current tf.Session object.
      saved_model_path: Directory to save the model.
      signature_key: The key to the SignatureDef that inputs & outputs
        correspond to.
      tags: Set of tags associated with the model.
      inputs: Input name -> input tensor mapping.
      outputs: Output name -> output tensor mapping.
      init_op: Op for initialization.
      assets_collection: Assets collection. This collection is a list of string
        tensors. Each tensor contains the asset file names.
    """
v1_builder = builder.SavedModelBuilder(saved_model_path)
sig_def = signature_def_utils_impl.predict_signature_def(
    inputs=inputs, outputs=outputs
)

v1_builder.add_meta_graph_and_variables(
    sess,
    tags,
    signature_def_map={signature_key: sig_def},
    main_op=init_op,
    assets_collection=assets_collection,
)
v1_builder.save()
