# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
t_obj_1 = traceable_stack.TraceableObject(
    None, filename="test_1.py", lineno=27)
t_obj_2 = traceable_stack.TraceableObject(
    None, filename="test_2.py", lineno=38)
colocation_dict = {
    "test_node_1": t_obj_1,
    "test_node_2": t_obj_2,
}
summary = error_interpolation._compute_colocation_summary_from_dict(
    "node_name", colocation_dict, prefix="  ")
self.assertIn("node_name", summary)
self.assertIn("colocate_with(test_node_1)", summary)
self.assertIn("<test_1.py:27>", summary)
self.assertIn("colocate_with(test_node_2)", summary)
self.assertIn("<test_2.py:38>", summary)
