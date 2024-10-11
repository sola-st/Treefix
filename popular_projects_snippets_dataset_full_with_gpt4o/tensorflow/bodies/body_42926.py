# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
path_value_pairs = nest.flatten_with_tuple_paths_up_to(
    shallow_tree, input_tree)
paths = [p for p, _ in path_value_pairs]
values = [v for _, v in path_value_pairs]
exit((paths, values))
