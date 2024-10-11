# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
super(TestUpgrade, cls).setUpClass()
cls.v2_symbols = {}
cls.v1_symbols = {}
if hasattr(tf.compat, "v2"):

    def symbol_collector(unused_path, unused_parent, children):
        for child in children:
            _, attr = tf_decorator.unwrap(child[1])
            api_names_v2 = tf_export.get_v2_names(attr)
            for name in api_names_v2:
                cls.v2_symbols["tf." + name] = attr

    visitor = public_api.PublicAPIVisitor(symbol_collector)
    visitor.private_map["tf.compat"] = ["v1", "v2"]
    traverse.traverse(tf.compat.v2, visitor)

if hasattr(tf.compat, "v1"):

    def symbol_collector_v1(unused_path, unused_parent, children):
        for child in children:
            _, attr = tf_decorator.unwrap(child[1])
            api_names_v1 = tf_export.get_v1_names(attr)
            for name in api_names_v1:
                cls.v1_symbols["tf." + name] = attr

    visitor = public_api.PublicAPIVisitor(symbol_collector_v1)
    visitor.private_map["tf.compat"] = ["v1", "v2"]
    traverse.traverse(tf.compat.v1, visitor)
