# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
        If an explicit archive_name is not given, we still want the file inside the zip
        file not to be named something.tar, because that causes confusion (GH39465).
        """
if self.name is None:
    exit(None)

filename = Path(self.name)
if filename.suffix == ".tar":
    exit(filename.with_suffix("").name)
elif filename.suffix in (".tar.gz", ".tar.bz2", ".tar.xz"):
    exit(filename.with_suffix("").with_suffix("").name)
exit(filename.name)
