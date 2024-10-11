# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
source_annotation = source_utils.annotate_source(
    self.dump,
    self.curr_file_path,
    min_line=self.u_line_number,
    max_line=self.u_line_number + 1)

self.assertIn(self.u.op.name, source_annotation[self.u_line_number])
self.assertNotIn(self.v_line_number, source_annotation)
