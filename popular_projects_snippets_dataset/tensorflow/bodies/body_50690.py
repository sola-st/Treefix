# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._TestDir(test_name)
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)
exit(test_dir)
