# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
source_annotation = source_utils.annotate_source(
    self.dump, self.curr_file_path, do_dumped_tensors=True)

# Note: Constant Tensors u_init and v_init may not get dumped due to
#   constant-folding.
self.assertIn(self.u.name, source_annotation[self.u_line_number])
self.assertIn(self.v.name, source_annotation[self.v_line_number])
self.assertIn(self.w.name, source_annotation[self.w_line_number])

self.assertNotIn(self.u.op.name, source_annotation[self.u_line_number])
self.assertNotIn(self.v.op.name, source_annotation[self.v_line_number])
self.assertNotIn(self.w.op.name, source_annotation[self.w_line_number])

self.assertIn(self.u.name, source_annotation[self.helper_line_number])
self.assertIn(self.v.name, source_annotation[self.helper_line_number])
self.assertIn(self.w.name, source_annotation[self.helper_line_number])
