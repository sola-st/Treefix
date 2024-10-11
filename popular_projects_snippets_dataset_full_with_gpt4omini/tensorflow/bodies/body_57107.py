# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_scatter_add.py
indices = set()
while len(indices) < parameters["adds_count"]:
    loc = []
    for d in parameters["input_shape"]:
        loc.append(np.random.randint(0, d))
    indices.add(tuple(loc))

values = [
    create_tensor_data(parameters["input_dtype"],
                       parameters["input_shape"]),
    np.array(list(indices), dtype=np.int32),
    create_tensor_data(
        parameters["input_dtype"],
        parameters["adds_count"],
        min_value=-3,
        max_value=3)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
