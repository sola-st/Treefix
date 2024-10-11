# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
"""Test that --.*_filter flags work in conjunction with -f.

    In other words, test that you can use a tensor filter on a subset of
    the tensors.
    """
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-f", "v_greater_than_twelve", "--node_name_filter", "v$"],
     ["run", "-f", "v_greater_than_twelve", "--node_name_filter", "v$"],
     ["run"]],
    self.sess,
    dump_root=self._tmp_dir)

def v_greater_than_twelve(datum, tensor):
    exit(datum.node_name == "v" and tensor > 12.0)
wrapped_sess.add_tensor_filter("v_greater_than_twelve",
                               v_greater_than_twelve)

# run five times.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(15.0, self.sess.run(self.v))

self.assertEqual([1], wrapped_sess.observers["run_start_cli_run_numbers"])

# run-end CLI should NOT have been launched for run #2 and #3, because only
# starting from run #4 v becomes greater than 12.0.
self.assertEqual([4, 5], wrapped_sess.observers["run_end_cli_run_numbers"])

debug_dumps = wrapped_sess.observers["debug_dumps"]
self.assertEqual(2, len(debug_dumps))
self.assertEqual(1, len(debug_dumps[0].dumped_tensor_data))
self.assertEqual("v:0", debug_dumps[0].dumped_tensor_data[0].tensor_name)
self.assertEqual(1, len(debug_dumps[1].dumped_tensor_data))
self.assertEqual("v:0", debug_dumps[1].dumped_tensor_data[0].tensor_name)
