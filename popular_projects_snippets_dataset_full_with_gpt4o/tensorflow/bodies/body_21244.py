# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
test_dir = os.path.join(self.get_temp_dir(), test_name)
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)
exit(test_dir)
