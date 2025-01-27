# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
export_dir_base = tempfile.mkdtemp() + "export/"
export_dir_1 = export_utils.get_timestamped_export_dir(
    export_dir_base)
time.sleep(2)
export_dir_2 = export_utils.get_timestamped_export_dir(
    export_dir_base)
time.sleep(2)
export_dir_3 = export_utils.get_timestamped_export_dir(
    export_dir_base)

# Export directories should be named using a timestamp that is seconds
# since epoch.  Such a timestamp is 10 digits long.
time_1 = os.path.basename(export_dir_1)
self.assertEqual(10, len(time_1))
time_2 = os.path.basename(export_dir_2)
self.assertEqual(10, len(time_2))
time_3 = os.path.basename(export_dir_3)
self.assertEqual(10, len(time_3))

self.assertLess(int(time_1), int(time_2))
self.assertLess(int(time_2), int(time_3))
