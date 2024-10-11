# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
num_pipelines = 10
num_outputs = 10
break_point = 10
all_outputs = [[] for _ in range(num_pipelines)]
with ops.Graph().as_default() as g:
    init_ops, get_next_ops, saver = self._build_graph(num_pipelines,
                                                      num_outputs)
    with self.session(graph=g) as sess:
        self.evaluate(init_ops)
        for _ in range(break_point):
            output = self.evaluate(get_next_ops)
            for i in range(num_pipelines):
                all_outputs[i].append(output[i])
        saver.save(sess, self._ckpt_path())

with ops.Graph().as_default() as g:
    init_ops, get_next_ops, saver = self._build_graph(num_pipelines,
                                                      num_outputs)
    with self.session(graph=g) as sess:
        self.evaluate(init_ops)
        saver.restore(sess, self._ckpt_path())
        for _ in range(num_outputs - break_point):
            output = self.evaluate(get_next_ops)
            for i in range(num_pipelines):
                all_outputs[i].append(output[i])

for output in all_outputs:
    self.assertSequenceEqual(sorted(output), range(num_outputs))
