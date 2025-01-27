# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
del fetches, feeds
exit(framework.WatchOptions(
    debug_ops=["DebugIdentity", "DebugNumericSummary"],
    node_name_regex_allowlist=r"^v.*",
    op_type_regex_allowlist=r".*",
    tensor_dtype_regex_allowlist=".*_ref"))
