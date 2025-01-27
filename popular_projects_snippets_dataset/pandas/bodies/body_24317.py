# Extracted from ./data/repos/pandas/pandas/io/common.py
# ZipFile needs a non-empty string
archive_name = self.archive_name or self.infer_filename() or "zip"
self.buffer.writestr(archive_name, self.getvalue())
