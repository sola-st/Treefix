# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
source_annotation = source_utils.annotate_source(self.dump,
                                                 self.curr_file_path)

self.assertIn(self.u_init.op.name,
              source_annotation[self.u_init_line_number])
self.assertIn(self.u.op.name, source_annotation[self.u_line_number])
self.assertIn(self.v_init.op.name,
              source_annotation[self.v_init_line_number])
self.assertIn(self.v.op.name, source_annotation[self.v_line_number])
self.assertIn(self.w.op.name, source_annotation[self.w_line_number])

# In the non-stack-top (default) mode, the helper line should be annotated
# with all the ops as well.
self.assertIn(self.u_init.op.name,
              source_annotation[self.helper_line_number])
self.assertIn(self.u.op.name, source_annotation[self.helper_line_number])
self.assertIn(self.v_init.op.name,
              source_annotation[self.helper_line_number])
self.assertIn(self.v.op.name, source_annotation[self.helper_line_number])
self.assertIn(self.w.op.name, source_annotation[self.helper_line_number])
