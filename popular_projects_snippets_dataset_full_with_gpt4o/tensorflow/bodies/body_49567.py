# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Validates a file against a sha256 or md5 hash.

  Args:
      fpath: path to the file being validated
      file_hash:  The expected hash string of the file.
          The sha256 and md5 hash algorithms are both supported.
      algorithm: Hash algorithm, one of 'auto', 'sha256', or 'md5'.
          The default 'auto' detects the hash algorithm in use.
      chunk_size: Bytes to read at a time, important for large files.

  Returns:
      Whether the file is valid
  """
hasher = _resolve_hasher(algorithm, file_hash)

if str(_hash_file(fpath, hasher, chunk_size)) == str(file_hash):
    exit(True)
else:
    exit(False)
