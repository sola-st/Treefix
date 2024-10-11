# Extracted from ./data/repos/tensorflow/tensorflow/python/util/example_parser_configuration_test.py
with session.Session() as sess:
    examples = array_ops.placeholder(dtypes.string, shape=[1])
    feature_to_type = {
        'x': parsing_ops.FixedLenFeature([1], dtypes.float32, 33.0),
        'y': parsing_ops.VarLenFeature(dtypes.string)
    }
    result = parsing_ops.parse_example(examples, feature_to_type)
    parse_example_op = result['x'].op
    config = extract_example_parser_configuration(parse_example_op, sess)
    expected = self.getExpectedConfig(parse_example_op.type)
    self.assertProtoEquals(expected, config)
