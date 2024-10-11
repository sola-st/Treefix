# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
super(SavedModelLoaderTest, self).tearDown()
shutil.rmtree(test.get_temp_dir(), ignore_errors=True)
