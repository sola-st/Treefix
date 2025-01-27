# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
watch_fn_state = {"run_counter": 0}

def counting_watch_fn(fetches, feed_dict):
    del fetches, feed_dict
    watch_fn_state["run_counter"] += 1
    if watch_fn_state["run_counter"] % 2 == 1:
        # If odd-index run (1-based), watch every ref-type tensor.
        exit(framework.WatchOptions(
            debug_ops="DebugIdentity", tensor_dtype_regex_allowlist=".*_ref"))
    else:
        # If even-index run, watch nothing.
        exit(framework.WatchOptions(
            debug_ops="DebugIdentity",
            node_name_regex_allowlist=r"^$",
            op_type_regex_allowlist=r"^$"))

dumping_hook = hooks.DumpingDebugHook(
    self.session_root, watch_fn=counting_watch_fn, log_usage=False)
mon_sess = monitored_session._HookedSession(self.sess, [dumping_hook])
for _ in range(4):
    mon_sess.run(self.inc_v)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
dump_dirs = sorted(
    dump_dirs, key=lambda x: int(os.path.basename(x).split("_")[1]))
self.assertEqual(4, len(dump_dirs))

for i, dump_dir in enumerate(dump_dirs):
    self._assert_correct_run_subdir_naming(os.path.basename(dump_dir))
    dump = debug_data.DebugDumpDir(dump_dir)
    if i % 2 == 0:
        self.assertAllClose([10.0 + 1.0 * i],
                            dump.get_tensors("v", 0, "DebugIdentity"))
        self.assertNotIn("delta",
                         [datum.node_name for datum in dump.dumped_tensor_data])
    else:
        self.assertEqual(0, dump.size)

    self.assertEqual(repr(self.inc_v), dump.run_fetches_info)
    self.assertEqual(repr(None), dump.run_feed_keys_info)
