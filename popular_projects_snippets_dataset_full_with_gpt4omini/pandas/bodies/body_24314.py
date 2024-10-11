# Extracted from ./data/repos/pandas/pandas/io/common.py
# TarFile needs a non-empty string
archive_name = self.archive_name or self.infer_filename() or "tar"
tarinfo = tarfile.TarInfo(name=archive_name)
tarinfo.size = len(self.getvalue())
self.buffer.addfile(tarinfo, self)
