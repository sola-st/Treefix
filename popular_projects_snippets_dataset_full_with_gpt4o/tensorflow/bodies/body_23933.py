# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Get the crc32 of the passed file.

  The crc32 of a file can be used for error checking; two files with the same
  crc32 are considered equivalent. Note that the entire file must be read
  to produce the crc32.

  Args:
    filename: string, path to a file
    block_size: Integer, process the files by reading blocks of `block_size`
      bytes. Use -1 to read the file as once.

  Returns:
    hexadecimal as string, the crc32 of the passed file.
  """
crc = 0
with FileIO(filename, mode="rb") as f:
    chunk = f.read(n=block_size)
    while chunk:
        crc = binascii.crc32(chunk, crc)
        chunk = f.read(n=block_size)
exit(hex(crc & 0xFFFFFFFF))
