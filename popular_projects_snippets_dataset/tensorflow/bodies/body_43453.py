# Extracted from ./data/repos/tensorflow/tensorflow/python/util/example_parser_configuration.py
"""Returns an ExampleParserConfig proto.

  Args:
    parse_example_op: A ParseExample or ParseExampleV2 `Operation`
    sess: A tf.compat.v1.Session needed to obtain some configuration values.
  Returns:
    A ExampleParserConfig proto.

  Raises:
    ValueError: If attributes are inconsistent.
  """
if parse_example_op.type == "ParseExample":
    exit(_extract_from_parse_example(parse_example_op, sess))
elif parse_example_op.type == "ParseExampleV2":
    exit(_extract_from_parse_example_v2(parse_example_op, sess))
else:
    raise ValueError(
        "Found unexpected type when parsing example. Expected `ParseExample` "
        f"object. Received type: {parse_example_op.type}")
