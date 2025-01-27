# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    names_v1 = tf_export.get_v1_names(attr)

    for name in names_v1:
        name = "tf.%s" % name
        if name not in all_keyword_renames:
            continue
        arg_names_v1 = tf_inspect.getargspec(attr)[0]
        keyword_renames = all_keyword_renames[name]
        self.assertEqual(type(keyword_renames), dict)

        # Assert that v1 function has valid v1 argument names.
        for from_name, _ in keyword_renames.items():
            self.assertIn(
                from_name, arg_names_v1,
                "%s not found in %s arguments: %s" %
                (from_name, name, str(arg_names_v1)))
