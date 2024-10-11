# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/from_list.py
if not elements:
    raise ValueError("Invalid `elements`. `elements` should not be empty.")
if not isinstance(elements, list):
    raise ValueError("Invalid `elements`. `elements` must be a list.")

elements = [structure.normalize_element(element) for element in elements]
type_specs = [
    structure.type_spec_from_value(element) for element in elements
]

# Check that elements have same nested structure.
num_elements = len(elements)
for i in range(1, num_elements):
    nest.assert_same_structure(type_specs[0], type_specs[i])

# Infer elements' supershape.
flattened_type_specs = [nest.flatten(type_spec) for type_spec in type_specs]
num_tensors_per_element = len(flattened_type_specs[0])
flattened_structure = [None] * num_tensors_per_element
for i in range(num_tensors_per_element):
    flattened_structure[i] = flattened_type_specs[0][i]
    for j in range(1, num_elements):
        flattened_structure[i] = flattened_structure[
            i].most_specific_common_supertype([flattened_type_specs[j][i]])

if not isinstance(type_specs[0], dataset_ops.DatasetSpec):
    self._tensors = list(
        itertools.chain.from_iterable(
            [nest.flatten(element) for element in elements]))
else:
    self._tensors = [x._variant_tensor for x in elements]
self._structure = nest.pack_sequence_as(type_specs[0], flattened_structure)
self._name = name
variant_tensor = gen_experimental_dataset_ops.list_dataset(
    self._tensors,
    output_types=self._flat_types,
    output_shapes=self._flat_shapes,
    metadata=self._metadata.SerializeToString())
super(_ListDataset, self).__init__(variant_tensor)
