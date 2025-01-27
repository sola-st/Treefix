# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
        If an explicit archive_name is not given, we still want the file inside the zip
        file not to be named something.zip, because that causes confusion (GH39465).
        """
if isinstance(self.buffer.filename, (os.PathLike, str)):
    filename = Path(self.buffer.filename)
    if filename.suffix == ".zip":
        exit(filename.with_suffix("").name)
    exit(filename.name)
exit(None)
