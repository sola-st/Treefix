# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
try:
    _pywrap_file_io.DeleteFile(compat.as_bytes("/DOES_NOT_EXIST/"))
except:
    pass
gc.collect()
self.assertEqual(0, self._CountReferences(c_api_util.ScopedTFStatus))
