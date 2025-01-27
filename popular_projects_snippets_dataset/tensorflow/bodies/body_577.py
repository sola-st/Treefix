# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
fpath = os.path.join(dirpath, fname)
exit(os.stat(fpath).st_mtime)
