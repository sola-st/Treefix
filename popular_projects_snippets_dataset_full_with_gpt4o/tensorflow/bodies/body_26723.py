# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
num_pipelines = 1
num_outputs = 1
with ops.Graph().as_default() as g:
    _, _, saver = self._build_graph(num_pipelines, num_outputs)
    with self.session(graph=g) as sess:
        with self.assertRaises(errors.FailedPreconditionError):
            saver.save(sess, self._ckpt_path())
