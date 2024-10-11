# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph_test.py
"""Writes a classifier with two input features to the given path."""
with ops.Graph().as_default():
    examples = array_ops.placeholder(dtypes.string, name="input_node")
    feature_configs = {
        feature_name: parsing_ops.FixedLenFeature(shape=[],
                                                  dtype=dtypes.float32),
    }
    features = parsing_ops.parse_example(examples, feature_configs)
    feature = features[feature_name]

    variable_node = variables.VariableV1(1.0, name="variable_node")
    scores = math_ops.multiply(variable_node, feature, name="output_node")
    class_feature = array_ops.fill(array_ops.shape(feature),
                                   "class_%s" % feature_name)
    classes = array_ops.transpose(class_feature)

    with session.Session() as sess:
        sess.run(variables.global_variables_initializer())
        signature = (
            signature_def_utils.classification_signature_def(
                examples=examples,
                classes=classes,
                scores=scores,))
        builder = saved_model_builder.SavedModelBuilder(path)
        builder.add_meta_graph_and_variables(
            sess,
            tags,
            signature_def_map={
                signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                    signature,
            },
        )
        builder.save(as_text=True)
