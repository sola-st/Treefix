# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names_v1 = tf_export.get_v1_names(attr)
    for name in api_names_v1:
        cls.v1_symbols["tf." + name] = attr
