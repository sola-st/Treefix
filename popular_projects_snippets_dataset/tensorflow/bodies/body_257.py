# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names_v2 = tf_export.get_v2_names(attr)
    for name in api_names_v2:
        cls.v2_symbols["tf." + name] = attr
