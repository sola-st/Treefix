# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
dictionary = mapping_type({(4, 5, (6, 8)): ("a", "b", ("c", "d"))})
flat = {4: "a", 5: "b", 6: "c", 8: "d"}
self.assertEqual(nest.flatten_dict_items(dictionary), flat)

with self.assertRaises(TypeError):
    nest.flatten_dict_items(4)

bad_dictionary = mapping_type({(4, 5, (4, 8)): ("a", "b", ("c", "d"))})
with self.assertRaisesRegex(ValueError, "not unique"):
    nest.flatten_dict_items(bad_dictionary)

another_bad_dictionary = mapping_type({
    (4, 5, (6, 8)): ("a", "b", ("c", ("d", "e")))
})
with self.assertRaisesRegex(
    ValueError, "Key had [0-9]* elements, but value had [0-9]* elements"):
    nest.flatten_dict_items(another_bad_dictionary)
