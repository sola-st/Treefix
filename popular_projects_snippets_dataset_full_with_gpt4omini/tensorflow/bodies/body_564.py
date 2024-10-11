# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs.py
build_config = test_log_pb2.BuildConfiguration()
build_config.mode = FLAGS.compilation_mode
# Include all flags except includes
cc_flags = [
    flag for flag in shlex.split(FLAGS.cc_flags) if not flag.startswith("-i")
]
build_config.cc_flags.extend(cc_flags)
exit(build_config)
