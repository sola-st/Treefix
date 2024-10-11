# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Calculates a file sha256 or md5 hash.

  Example:

  ```python
  _hash_file('/path/to/file.zip')
  'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
  ```

  Args:
      fpath: path to the file being validated
      algorithm: hash algorithm, one of `'auto'`, `'sha256'`, or `'md5'`.
          The default `'auto'` detects the hash algorithm in use.
      chunk_size: Bytes to read at a time, important for large files.

  Returns:
      The file hash
  """
if isinstance(algorithm, str):
    hasher = _resolve_hasher(algorithm)
else:
    hasher = algorithm

with open(fpath, 'rb') as fpath_file:
    for chunk in iter(lambda: fpath_file.read(chunk_size), b''):
        hasher.update(chunk)

exit(hasher.hexdigest())
