# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session() as sess:
    a1 = self._get_test_attrs()
    with sess.graph._attr_scope({
        "_A": attr_value_pb2.AttrValue(s=compat.as_bytes("foo"))
    }):
        a2 = self._get_test_attrs()
        with sess.graph._attr_scope({
            "_A": None,
            "_B": attr_value_pb2.AttrValue(s=compat.as_bytes("bar"))
        }):
            a3 = self._get_test_attrs()
            with sess.graph._attr_scope({
                "_A": attr_value_pb2.AttrValue(s=compat.as_bytes("baz"))
            }):
                a4 = self._get_test_attrs()
            a5 = self._get_test_attrs()
        a6 = self._get_test_attrs()
    a7 = self._get_test_attrs()

    self.assertAllEqual((None, None), a1)
    self.assertAllEqual(("foo", None), a2)
    self.assertAllEqual((None, "bar"), a3)
    self.assertAllEqual(("baz", "bar"), a4)
    self.assertAllEqual((None, "bar"), a5)
    self.assertAllEqual(("foo", None), a6)
    self.assertAllEqual((None, None), a7)
