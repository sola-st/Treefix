# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
export_dir = os.path.join("tmp", "export", "1576013284")
tmp_export_dir = export_utils.get_temp_export_dir(export_dir)
self.assertEqual(tmp_export_dir,
                 os.path.join(b"tmp", b"export", b"temp-1576013284"))

export_dir = os.path.join(b"tmp", b"export", b"1576013284")
tmp_export_dir = export_utils.get_temp_export_dir(export_dir)
self.assertEqual(tmp_export_dir,
                 os.path.join(b"tmp", b"export", b"temp-1576013284"))
