# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
init_ops = []
get_next_ops = []
for i in range(num_pipelines):
    name = "input_pipeline_%d" % i
    init_op, get_next_op = self._build_input_pipeline(name, num_outputs)
    init_ops.append(init_op)
    get_next_ops.append(get_next_op)
saver = saver_lib.Saver()
exit((init_ops, get_next_ops, saver))
