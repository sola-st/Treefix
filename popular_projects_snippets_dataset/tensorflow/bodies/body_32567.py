# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
rank_two_shapes = [
    (1, 1),
    (1, 3),
    ("a", "b"),
    (None, None),
]
rank_three_shapes = [
    (1, 1, 1),
    ("a", "b", "c"),
    (None, None, None),
    (1, "b", None),
]

def raises_static_rank_error(shapes, x, correct_rank, actual_rank):
    for shape in shapes:
        regex = (r"Tensor .* must have rank %d.  Received rank %d" %
                 (correct_rank, actual_rank))
        self.raises_static_error(shapes=[(x, shape)], regex=regex)

raises_static_rank_error(
    rank_two_shapes, array_ops.ones([1]), correct_rank=2, actual_rank=1)
raises_static_rank_error(
    rank_three_shapes,
    array_ops.ones([1, 1]),
    correct_rank=3,
    actual_rank=2)
raises_static_rank_error(
    rank_three_shapes, array_ops.constant(1), correct_rank=3, actual_rank=0)
