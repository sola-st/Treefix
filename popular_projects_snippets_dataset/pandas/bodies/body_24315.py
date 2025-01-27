# Extracted from ./data/repos/pandas/pandas/io/common.py
super().__init__()
mode = mode.replace("b", "")
self.archive_name = archive_name

kwargs.setdefault("compression", zipfile.ZIP_DEFLATED)
# error: Argument 1 to "ZipFile" has incompatible type "Union[
# Union[str, PathLike[str]], ReadBuffer[bytes], WriteBuffer[bytes]]";
# expected "Union[Union[str, PathLike[str]], IO[bytes]]"
self.buffer = zipfile.ZipFile(file, mode, **kwargs)  # type: ignore[arg-type]
