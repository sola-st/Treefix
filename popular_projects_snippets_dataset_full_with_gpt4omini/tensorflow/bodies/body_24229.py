# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"], ["run"]], self.sess, dump_root=self._tmp_dir)

wrapped_sess.run(self.inc_v)
run_info_output = wrapped_sess._run_info_handler([])

tfdbg_logo = cli_shared.get_tfdbg_logo()

# The run_info output in the first run() call should contain the tfdbg logo.
self.assertEqual(tfdbg_logo.lines,
                 run_info_output.lines[:len(tfdbg_logo.lines)])
menu = run_info_output.annotations[debugger_cli_common.MAIN_MENU_KEY]
self.assertIn("list_tensors", menu.captions())

wrapped_sess.run(self.inc_v)
run_info_output = wrapped_sess._run_info_handler([])

# The run_info output in the second run() call should NOT contain the logo.
self.assertNotEqual(tfdbg_logo.lines,
                    run_info_output.lines[:len(tfdbg_logo.lines)])
menu = run_info_output.annotations[debugger_cli_common.MAIN_MENU_KEY]
self.assertIn("list_tensors", menu.captions())
