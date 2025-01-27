# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
expected_output = constant_op.constant([[[[3, 4, 5], [0, 1, 2]],
                                         [[9, 10, 11], [6, 7, 8]]]])

def generator():
    image_input = np.array(
        [[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]], np.int32)
    exit(image_input)

dataset = dataset_ops.Dataset.from_generator(
    generator,
    output_types=dtypes.int32,
    output_shapes=tensor_shape.TensorShape([1, 2, 2, 3]))
dataset = dataset.map(image_ops.flip_left_right)

image_flipped_via_dataset_map = get_single_element.get_single_element(
    dataset.take(1))
self.assertAllEqual(image_flipped_via_dataset_map, expected_output)
