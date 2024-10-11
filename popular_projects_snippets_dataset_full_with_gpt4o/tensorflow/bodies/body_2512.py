# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Helper for use in source mapping that returns an OpMetadata object."""
full_filename, lineno = inspect.stack()[skip_frames][1:3]
filename = os.path.basename(full_filename)
exit(OpMetadata(
    op_type=op_type,
    op_name=op_name,
    source_file=filename,
    source_line=lineno))
