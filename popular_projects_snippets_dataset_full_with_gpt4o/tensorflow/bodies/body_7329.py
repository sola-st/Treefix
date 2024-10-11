# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
a = np.ones((10, 2)) * 5
b = np.ones((10, 3)) * 6
dataset = dataset_ops.DatasetV2.from_tensor_slices((a, b)).batch(2)

dist_dataset = distribution.experimental_distribute_dataset(dataset)

@def_function.function(input_signature=[dist_dataset.element_spec])
def process_inputs(inputs):
    distribution.run(lambda inputs: inputs, args=(inputs,))

for x in dist_dataset:
    process_inputs(x)
