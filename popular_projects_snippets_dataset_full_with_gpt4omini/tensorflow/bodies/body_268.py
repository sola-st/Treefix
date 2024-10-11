# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
collect = True
v1_symbols = set([])

# Converts all symbols in the v1 namespace to the v2 namespace, raising
# an error if the target of the conversion is not in the v1 namespace.
def conversion_visitor(unused_path, unused_parent, children):
    for child in children:
        _, attr = tf_decorator.unwrap(child[1])
        api_names = tf_export.get_v1_names(attr)
        for name in api_names:
            if collect:
                v1_symbols.add("tf." + name)
            else:
                _, _, _, text = self._upgrade("tf." + name)
                if (text and
                    not text.startswith("tf.compat.v1") and
                    not text.startswith("tf.compat.v2") and
                    not text.startswith("tf.estimator") and
                    text not in v1_symbols):
                    self.assertFalse(
                        True, "Symbol %s generated from %s not in v1 API" % (
                            text, name))

visitor = public_api.PublicAPIVisitor(conversion_visitor)
visitor.do_not_descend_map["tf"].append("contrib")
visitor.private_map["tf.compat"] = ["v1", "v2"]
traverse.traverse(tf.compat.v1, visitor)
collect = False
traverse.traverse(tf.compat.v1, visitor)
