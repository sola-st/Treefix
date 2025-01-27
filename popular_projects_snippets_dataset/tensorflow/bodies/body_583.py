# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
"""Find benchmark files, process them, and upload their data to the datastore.

  Locate benchmark files in the data directory, process them, and upload their
  data to the datastore.  After processing each file, move it to the archive
  directory for safe-keeping.  Each file is locked for processing, which allows
  multiple uploader instances to run concurrently if needed, each one handling
  different benchmark files, skipping those already locked by another.

  Args:
    opts: command line options object

  Note: To use locking, the file is first opened, then its descriptor is used to
  lock and read it.  The lock is released when the file is closed.  Do not open
  that same file a 2nd time while the lock is already held, because when that
  2nd file descriptor is closed, the lock will be released prematurely.
  """
client = datastore.Client()

for fname in list_files_by_mtime(opts.datadir):
    fpath = os.path.join(opts.datadir, fname)
    try:
        with open(fpath, "r") as fd:
            if trylock(fd):
                upload_benchmark_data(client, fd.read())
                shutil.move(fpath, os.path.join(opts.archivedir, fname))
                # unlock(fd) -- When "with open()" closes fd, the lock is released.
    except Exception as e:  # pylint: disable=broad-except
        print("Cannot process '%s', skipping. Error: %s" % (fpath, e))
