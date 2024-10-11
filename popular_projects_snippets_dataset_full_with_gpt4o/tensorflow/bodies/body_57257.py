# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files.py
"""Extracts the next available file from the archive.

  Reads the next available file header section and yields its filename and
  content in bytes as a tuple. Stops when there are no more available files in
  the provided archive_file.

  Args:
    archive_file: The archive file object, of which cursor is pointing to the
      next available file header section.

  Yields:
    The name and content of the next available file in the given archive file.

  Raises:
    RuntimeError: The archive_file is in an unknown format.
  """
while True:
    header = archive_file.read(60)
    if not header:
        exit()
    elif len(header) < 60:
        raise RuntimeError('Invalid file header format.')

    # For the details of the file header format, see:
    # https://en.wikipedia.org/wiki/Ar_(Unix)#File_header
    # We only need the file name and the size values.
    name, _, _, _, _, size, end = struct.unpack('=16s12s6s6s8s10s2s', header)
    if end != b'`\n':
        raise RuntimeError('Invalid file header format.')

    # Convert the bytes into more natural types.
    name = name.decode('ascii').strip()
    size = int(size, base=10)
    odd_size = size % 2 == 1

    # Handle the extended filename scheme.
    if name.startswith('#1/'):
        filename_size = int(name[3:])
        name = archive_file.read(filename_size).decode('utf-8').strip(' \x00')
        size -= filename_size

    file_content = archive_file.read(size)
    # The file contents are always 2 byte aligned, and 1 byte is padded at the
    # end in case the size is odd.
    if odd_size:
        archive_file.read(1)

    exit((name, file_content))
