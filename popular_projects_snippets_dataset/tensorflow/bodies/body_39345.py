# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
# Make sure we have a clean directory to work in.
with self.tempDir() as tempdir:

    # Jump to that directory until this test is done.
    with self.tempWorkingDir(tempdir):

        # Save training snapshots to a relative path.
        traindir = "train"
        os.mkdir(traindir)

        filename = "snapshot"
        filepath = os.path.join(traindir, filename)

        with self.cached_session() as sess:
            # Build a simple graph.
            v0 = variables.Variable(0.0)
            inc = v0.assign_add(1.0)

            save = saver_module.Saver({"v0": v0})

            # Record a short training history.
            self.evaluate(variables.global_variables_initializer())
            save.save(sess, filepath, global_step=0)
            self.evaluate(inc)
            save.save(sess, filepath, global_step=1)
            self.evaluate(inc)
            save.save(sess, filepath, global_step=2)

        with self.cached_session() as sess:
            # Build a new graph with different initialization.
            v0 = variables.Variable(-1.0)

            # Create a new saver.
            save = saver_module.Saver({"v0": v0})
            self.evaluate(variables.global_variables_initializer())

            # Get the most recent checkpoint name from the training history file.
            name = checkpoint_management.latest_checkpoint(traindir)
            self.assertIsNotNone(name)

            # Restore "v0" from that checkpoint.
            save.restore(sess, name)
            self.assertEqual(self.evaluate(v0), 2.0)
