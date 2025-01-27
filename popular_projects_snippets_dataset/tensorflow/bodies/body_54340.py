# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session() as sess:
    with sess.graph.name_scope("l0"):
        with variable_scope.variable_scope("l1"):
            with sess.graph.name_scope("l1") as scope:
                self.assertEqual("l0/l1/l1/", scope)
                self.assertEqual(
                    "l0/l1/l1/foo",
                    sess.graph.unique_name(
                        "foo", mark_as_used=False))
                self.assertEqual("l0/l1/l1/foo", sess.graph.unique_name("foo"))
            with sess.graph.name_scope("l2") as scope:
                self.assertEqual("l0/l1/l2/", scope)
                self.assertEqual(
                    "l0/l1/l2/foo",
                    sess.graph.unique_name(
                        "foo", mark_as_used=False))
                self.assertEqual("l0/l1/l2/foo", sess.graph.unique_name("foo"))
