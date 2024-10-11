# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
slice_info = variables_lib.Variable.SaveSliceInfo()
v._set_save_slice_info(slice_info)
self.assertIs(v._get_save_slice_info(), slice_info)
# Some code accesses _save_slice_info directly without using the getter.
self.assertIs(v._save_slice_info, slice_info)
