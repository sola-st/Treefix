# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
graph = ops.Graph()
with graph.as_default(), session.Session():
    directory = self.get_temp_dir()
    prefix = os.path.join(directory, "ckpt")
    save_state = _NumpyState()
    saver = util.Checkpoint(numpy=save_state)
    save_state.a = numpy.ones([2, 2])
    save_path = saver.save(prefix)
    saver.restore(save_path)
    graph.finalize()
    saver.save(prefix)
    save_state.a = numpy.zeros([2, 2])
    saver.save(prefix)
    saver.restore(save_path)
