# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper.py
"""Implementation of abstract method in superclass.

    See doc of `NonInteractiveDebugWrapperSession.prepare_run_debug_urls()`
    for details. This implementation creates a run-specific subdirectory under
    self._session_root and stores information regarding run `fetches` and
    `feed_dict.keys()` in the subdirectory.

    Args:
      fetches: Same as the `fetches` argument to `Session.run()`
      feed_dict: Same as the `feed_dict` argument to `Session.run()`

    Returns:
      debug_urls: (`str` or `list` of `str`) file:// debug URLs to be used in
        this `Session.run()` call.
    """

# Add a UUID to accommodate the possibility of concurrent run() calls.
self._run_counter_lock.acquire()
run_dir = os.path.join(self._session_root, "run_%d_%d" %
                       (int(time.time() * 1e6), self._run_counter))
self._run_counter += 1
self._run_counter_lock.release()
gfile.MkDir(run_dir)

fetches_event = event_pb2.Event()
fetches_event.log_message.message = repr(fetches)
fetches_path = os.path.join(
    run_dir,
    debug_data.METADATA_FILE_PREFIX + debug_data.FETCHES_INFO_FILE_TAG)
with gfile.Open(os.path.join(fetches_path), "wb") as f:
    f.write(fetches_event.SerializeToString())

feed_keys_event = event_pb2.Event()
feed_keys_event.log_message.message = (repr(feed_dict.keys()) if feed_dict
                                       else repr(feed_dict))

feed_keys_path = os.path.join(
    run_dir,
    debug_data.METADATA_FILE_PREFIX + debug_data.FEED_KEYS_INFO_FILE_TAG)
with gfile.Open(os.path.join(feed_keys_path), "wb") as f:
    f.write(feed_keys_event.SerializeToString())

exit(["file://" + run_dir])
