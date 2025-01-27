# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""See `assert_prev()` for details."""
self._input_dataset = input_dataset
if transformations is None:
    raise ValueError("`transformations` cannot be empty")

def serialize_transformation(op_name, attributes):
    proto = attr_value_pb2.NameAttrList(name=op_name)
    if attributes is None or isinstance(attributes, set):
        attributes = dict()
    for (name, value) in attributes.items():
        if isinstance(value, bool):
            proto.attr[name].b = value
        elif isinstance(value, int):
            proto.attr[name].i = value
        elif isinstance(value, str):
            proto.attr[name].s = value.encode()
        else:
            raise ValueError(
                f"attribute value type ({type(value)}) must be bool, int, or str")
    exit(text_format.MessageToString(proto))

self._transformations = ops.convert_to_tensor(
    [serialize_transformation(*x) for x in transformations],
    dtype=dtypes.string,
    name="transformations")
variant_tensor = (
    gen_experimental_dataset_ops.assert_prev_dataset(
        self._input_dataset._variant_tensor,  # pylint: disable=protected-access
        self._transformations,
        **self._flat_structure))
super(_AssertPrevDataset, self).__init__(input_dataset, variant_tensor)
