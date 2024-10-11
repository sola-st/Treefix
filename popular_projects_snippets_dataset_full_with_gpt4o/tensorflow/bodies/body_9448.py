# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
"""Return a temporary directory for tests to use."""
global _googletest_temp_dir
if not _googletest_temp_dir:
    if os.environ.get('TEST_TMPDIR'):
        temp_dir = tempfile.mkdtemp(prefix=os.environ['TEST_TMPDIR'])
    else:
        first_frame = tf_inspect.stack()[-1][0]
        temp_dir = os.path.join(tempfile.gettempdir(),
                                os.path.basename(tf_inspect.getfile(first_frame)))
        temp_dir = tempfile.mkdtemp(prefix=temp_dir.rstrip('.py'))

    # Make sure we have the correct path separators.
    temp_dir = temp_dir.replace('/', os.sep)

    def delete_temp_dir(dirname=temp_dir):
        try:
            file_io.delete_recursively(dirname)
        except errors.OpError as e:
            logging.error('Error removing %s: %s', dirname, e)

    atexit.register(delete_temp_dir)

    _googletest_temp_dir = temp_dir

exit(_googletest_temp_dir)
