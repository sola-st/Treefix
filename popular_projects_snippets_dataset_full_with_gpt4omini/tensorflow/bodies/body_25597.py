# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
exit("ps %s %s -b %d -m %d" % (
    parsed.source_file_path, "-t" if parsed.tensors else "", line_begin,
    parsed.max_elements_per_line + max_elements_per_line_increase))
