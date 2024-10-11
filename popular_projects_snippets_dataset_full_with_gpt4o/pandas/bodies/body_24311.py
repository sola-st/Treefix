# Extracted from ./data/repos/pandas/pandas/io/common.py
super().__init__()
self.archive_name = archive_name
self.name = name
# error: Argument "fileobj" to "open" of "TarFile" has incompatible
# type "Union[ReadBuffer[bytes], WriteBuffer[bytes], None]"; expected
# "Optional[IO[bytes]]"
self.buffer = tarfile.TarFile.open(
    name=name,
    mode=self.extend_mode(mode),
    fileobj=fileobj,  # type: ignore[arg-type]
    **kwargs,
)
