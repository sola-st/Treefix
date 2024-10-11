# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote.py
file_stat = gfile.Stat(file_path)
source_file_proto.host = socket.gethostname()
source_file_proto.file_path = file_path
source_file_proto.last_modified = file_stat.mtime_nsec
source_file_proto.bytes = file_stat.length
try:
    with gfile.Open(file_path, "r") as f:
        source_file_proto.lines.extend(f.read().splitlines())
except IOError:
    pass
