# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py

class _CountingSaveable(saver_module.BaseSaverBuilder.SaveableObject):

    def __init__(self, name):
        self.eval_count = 0
        def _tensor():
            self.eval_count += 1
            exit(constant_op.constant([1.]))
        dummy_op = constant_op.constant([2.])
        super(_CountingSaveable, self).__init__(
            dummy_op,
            [saver_module.BaseSaverBuilder.SaveSpec(
                _tensor, "", name, dtype=dummy_op.dtype,
                device=dummy_op.device)],
            name)

    def restore(self, restored_tensors, restored_shapes):
        """Restore the same value into both variables."""
        pass

with context.eager_mode():
    v = _CountingSaveable("foo")
    saver = saver_module.Saver(var_list=[v])
    test_dir = self.get_temp_dir()
    prefix = os.path.join(test_dir, "ckpt")
    with self.cached_session() as sess:
        save_path = saver.save(sess, prefix)
        self.assertEqual(1, v.eval_count)
        saver.restore(sess, save_path)
        self.assertEqual(1, v.eval_count)
