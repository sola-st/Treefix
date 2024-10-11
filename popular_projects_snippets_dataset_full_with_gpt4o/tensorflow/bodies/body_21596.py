# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Restore does some tricky exception handling to figure out if it should
# load an object-based checkpoint. Tests that the exception handling isn't
# too broad.
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

a = resource_variable_ops.ResourceVariable(1., name="a")
b = resource_variable_ops.ResourceVariable(1., name="b")
a_saver = saver_module.Saver([a])
b_saver = saver_module.Saver([b])
with self.cached_session() as sess:
    self.evaluate(a.initializer)
    save_path = a_saver.save(sess=sess, save_path=checkpoint_prefix)
    with self.assertRaisesRegex(errors.NotFoundError,
                                "Key b not found in checkpoint"):
        b_saver.restore(sess=sess, save_path=save_path)

    with self.assertRaises(errors.NotFoundError) as cs:
        b_saver.restore(sess=sess, save_path=save_path)

    # Make sure we don't have a confusing "During handling of the above
    # exception" block in Python 3.
    self.assertNotIn("NewCheckpointReader", cs.exception.message)
