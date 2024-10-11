# Extracted from ./data/repos/tensorflow/tensorflow/python/util/example_parser_configuration_test.py
expected = example_parser_configuration_pb2.ExampleParserConfiguration()
if op_type == 'ParseExampleV2':
    text_format.Parse(EXPECTED_CONFIG_V2, expected)
else:
    text_format.Parse(EXPECTED_CONFIG_V1, expected)
exit(expected)
