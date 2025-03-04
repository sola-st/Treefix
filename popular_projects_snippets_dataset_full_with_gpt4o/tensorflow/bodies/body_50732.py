# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/simple_save.py
"""Convenience function to build a SavedModel suitable for serving.

  In many common cases, saving models for serving will be as simple as:

      simple_save(session,
                  export_dir,
                  inputs={"x": x, "y": y},
                  outputs={"z": z})

  Although in many cases it's not necessary to understand all of the many ways
      to configure a SavedModel, this method has a few practical implications:
    - It will be treated as a graph for inference / serving (i.e. uses the tag
      `saved_model.SERVING`)
    - The SavedModel will load in TensorFlow Serving and supports the
      [Predict
      API](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/apis/predict.proto).
      To use the Classify, Regress, or MultiInference APIs, please
      use either
      [tf.Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator)
      or the lower level
      [SavedModel
      APIs](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md).
    - Some TensorFlow ops depend on information on disk or other information
      called "assets". These are generally handled automatically by adding the
      assets to the `GraphKeys.ASSET_FILEPATHS` collection. Only assets in that
      collection are exported; if you need more custom behavior, you'll need to
      use the
      [SavedModelBuilder](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/builder.py).

  More information about SavedModel and signatures can be found here:
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md.

  Args:
    session: The TensorFlow session from which to save the meta graph and
        variables.
    export_dir: The path to which the SavedModel will be stored.
    inputs: dict mapping string input names to tensors. These are added
        to the SignatureDef as the inputs.
    outputs:  dict mapping string output names to tensors. These are added
        to the SignatureDef as the outputs.
    legacy_init_op: Legacy support for op or group of ops to execute after the
        restore op upon a load.
  """
signature_def_map = {
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
        signature_def_utils.predict_signature_def(inputs, outputs)
}
b = builder.SavedModelBuilder(export_dir)
b.add_meta_graph_and_variables(
    session,
    tags=[tag_constants.SERVING],
    signature_def_map=signature_def_map,
    assets_collection=ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS),
    main_op=legacy_init_op,
    clear_devices=True)
b.save()
