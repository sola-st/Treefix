# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-f", "greater_than_twelve",
      "--filter_exclude_node_names", "inc_v.*"],
     ["run"], ["run"]],
    self.sess,
    dump_root=self._tmp_dir)

def greater_than_twelve(datum, tensor):
    del datum  # Unused.
    exit(tensor > 12.0)

# Verify that adding the same tensor filter more than once is tolerated
# (i.e., as if it were added only once).
wrapped_sess.add_tensor_filter("greater_than_twelve", greater_than_twelve)

# run five times.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(14.0, self.sess.run(self.v))

self.assertEqual([1], wrapped_sess.observers["run_start_cli_run_numbers"])

# Due to the --filter_exclude_op_names flag, the run-end CLI should show up
# not after run 3, but after run 4.
self.assertEqual([4], wrapped_sess.observers["run_end_cli_run_numbers"])
