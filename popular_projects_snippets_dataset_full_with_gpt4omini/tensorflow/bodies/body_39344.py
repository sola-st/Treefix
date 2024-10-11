# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
# Make sure we have a clean directory to work in.
with self.tempDir() as tempdir:
    # Jump to that directory until this test is done.
    with self.tempWorkingDir(tempdir):
        # Save training snapshots to a relative path.
        traindir = "train"
        os.mkdir(traindir)
        # Collides with the default name of the checkpoint state file.
        filepath = os.path.join(traindir, "checkpoint")

        with self.cached_session() as sess:
            unused_a = variables.Variable(0.0)  # So that Saver saves something.
            self.evaluate(variables.global_variables_initializer())

            # Should fail.
            saver = saver_module.Saver(sharded=False)
            with self.assertRaisesRegex(ValueError, "collides with"):
                saver.save(sess, filepath)

            # Succeeds: the file will be named "checkpoint-<step>".
            saver.save(sess, filepath, global_step=1)
            self.assertIsNotNone(
                checkpoint_management.latest_checkpoint(traindir))

            # Succeeds: the file will be named "checkpoint-<i>-of-<n>".
            saver = saver_module.Saver(sharded=True)
            saver.save(sess, filepath)
            self.assertIsNotNone(
                checkpoint_management.latest_checkpoint(traindir))

            # Succeeds: the file will be named "checkpoint-<step>-<i>-of-<n>".
            saver = saver_module.Saver(sharded=True)
            saver.save(sess, filepath, global_step=1)
            self.assertIsNotNone(
                checkpoint_management.latest_checkpoint(traindir))
