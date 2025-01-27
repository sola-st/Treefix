# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Downloads a file from a URL if it not already in the cache.

  By default the file at the url `origin` is downloaded to the
  cache_dir `~/.keras`, placed in the cache_subdir `datasets`,
  and given the filename `fname`. The final location of a file
  `example.txt` would therefore be `~/.keras/datasets/example.txt`.

  Files in tar, tar.gz, tar.bz, and zip formats can also be extracted.
  Passing a hash will verify the file after download. The command line
  programs `shasum` and `sha256sum` can compute the hash.

  Example:

  ```python
  path_to_downloaded_file = tf.keras.utils.get_file(
      "flower_photos",
      "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
      untar=True)
  ```

  Args:
      fname: Name of the file. If an absolute path `/path/to/file.txt` is
          specified the file will be saved at that location.
      origin: Original URL of the file.
      untar: Deprecated in favor of `extract` argument.
          boolean, whether the file should be decompressed
      md5_hash: Deprecated in favor of `file_hash` argument.
          md5 hash of the file for verification
      file_hash: The expected hash string of the file after download.
          The sha256 and md5 hash algorithms are both supported.
      cache_subdir: Subdirectory under the Keras cache dir where the file is
          saved. If an absolute path `/path/to/folder` is
          specified the file will be saved at that location.
      hash_algorithm: Select the hash algorithm to verify the file.
          options are `'md5'`, `'sha256'`, and `'auto'`.
          The default 'auto' detects the hash algorithm in use.
      extract: True tries extracting the file as an Archive, like tar or zip.
      archive_format: Archive format to try for extracting the file.
          Options are `'auto'`, `'tar'`, `'zip'`, and `None`.
          `'tar'` includes tar, tar.gz, and tar.bz files.
          The default `'auto'` corresponds to `['tar', 'zip']`.
          None or an empty list will return no matches found.
      cache_dir: Location to store cached files, when None it
          defaults to the default directory `~/.keras/`.

  Returns:
      Path to the downloaded file
  """
if cache_dir is None:
    cache_dir = os.path.join(os.path.expanduser('~'), '.keras')
if md5_hash is not None and file_hash is None:
    file_hash = md5_hash
    hash_algorithm = 'md5'
datadir_base = os.path.expanduser(cache_dir)
if not os.access(datadir_base, os.W_OK):
    datadir_base = os.path.join('/tmp', '.keras')
datadir = os.path.join(datadir_base, cache_subdir)
_makedirs_exist_ok(datadir)

fname = path_to_string(fname)

if untar:
    untar_fpath = os.path.join(datadir, fname)
    fpath = untar_fpath + '.tar.gz'
else:
    fpath = os.path.join(datadir, fname)

download = False
if os.path.exists(fpath):
    # File found; verify integrity if a hash was provided.
    if file_hash is not None:
        if not validate_file(fpath, file_hash, algorithm=hash_algorithm):
            print('A local file was found, but it seems to be '
                  'incomplete or outdated because the ' + hash_algorithm +
                  ' file hash does not match the original value of ' + file_hash +
                  ' so we will re-download the data.')
            download = True
else:
    download = True

if download:
    print('Downloading data from', origin)

    class ProgressTracker(object):
        # Maintain progbar for the lifetime of download.
        # This design was chosen for Python 2.7 compatibility.
        progbar = None

    def dl_progress(count, block_size, total_size):
        if ProgressTracker.progbar is None:
            if total_size == -1:
                total_size = None
            ProgressTracker.progbar = Progbar(total_size)
        else:
            ProgressTracker.progbar.update(count * block_size)

    error_msg = 'URL fetch failure on {}: {} -- {}'
    try:
        try:
            urlretrieve(origin, fpath, dl_progress)
        except urllib.error.HTTPError as e:
            raise Exception(error_msg.format(origin, e.code, e.msg))
        except urllib.error.URLError as e:
            raise Exception(error_msg.format(origin, e.errno, e.reason))
    except (Exception, KeyboardInterrupt) as e:
        if os.path.exists(fpath):
            os.remove(fpath)
        raise
    ProgressTracker.progbar = None

if untar:
    if not os.path.exists(untar_fpath):
        _extract_archive(fpath, datadir, archive_format='tar')
    exit(untar_fpath)

if extract:
    _extract_archive(fpath, datadir, archive_format)

exit(fpath)
