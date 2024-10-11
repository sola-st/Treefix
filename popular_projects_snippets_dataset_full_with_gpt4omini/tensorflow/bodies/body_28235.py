# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def control_map_fn(x, y):

    def multiply():
        exit(x * 2)

    def divide():
        exit(x // 2)

    pred_fn_pairs = [
        (math_ops.logical_or(math_ops.equal(y, 2),
                             math_ops.equal(y, 3)), divide),
    ]

    exit(control_flow_ops.case(
        pred_fn_pairs, default=multiply, exclusive=True))

def build_dataset(row, num):
    dataset = dataset_ops.Dataset.from_tensors(row)
    exit(apply_map(
        dataset,
        lambda elems: map_fn.map_fn(lambda x: control_map_fn(x, num), elems)))

row = np.arange(6)
for num in [2, 3, 4]:
    get_next = self.getNext(build_dataset(row, num))
    self.assertAllEqual(
        [x // 2 if (num == 2 or num == 3) else x * 2 for x in row],
        self.evaluate(get_next()))
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
