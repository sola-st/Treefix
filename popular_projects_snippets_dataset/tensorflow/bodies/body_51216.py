# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py

class Zoo(extension_type.ExtensionType):
    __name__ = "tf.nested_structure_coder_test.Zoo"
    zookeepers: typing.Tuple[str, ...]
    animals: typing.Mapping[str, ops.Tensor]

structure = [
    Zoo.Spec(
        zookeepers=["Zoey", "Zack"],
        animals={"tiger": tensor_spec.TensorSpec([16])})
]

self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected_pbtxt = r"""
    list_value {
      values {
        type_spec_value {
          type_spec_class: EXTENSION_TYPE_SPEC
          type_spec_class_name: "tf.nested_structure_coder_test.Zoo.Spec"
          num_flat_components: 1
          type_state {
            tuple_value {
              values {
                tuple_value {
                  values { string_value: "zookeepers" }
                  values { tuple_value {
                    values { string_value: "Zoey" }
                    values { string_value: "Zack" } } } } }
              values {
                tuple_value {
                  values { string_value: "animals" }
                  values { dict_value {
                    fields {
                      key: "tiger"
                      value { tensor_spec_value {
                        shape { dim { size: 16 } }
                        dtype: DT_FLOAT } } } } } } } } } } } }
    """
expected = struct_pb2.StructuredValue()
text_format.Parse(expected_pbtxt, expected)
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)
