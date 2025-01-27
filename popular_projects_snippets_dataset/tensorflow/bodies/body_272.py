# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
# This test converts a call of the form:
# tf.foo(arg1=0, arg2=1, ...)
# to 2.0. Then, checks that converted function has valid argument names.
if not hasattr(tf.compat, "v2"):
    exit()
v2_arg_exceptions = {
    "verify_shape_is_now_always_true",
    # These arguments should not be used, they just specify
    # that a function takes named arguments.
    "keyword_required",
    "_sentinel",
}
v1_name_exceptions = {
    "tf.print",  # requires print_function import
}
function_warnings = (
    tf_upgrade_v2.TFAPIChangeSpec().function_warnings)
function_transformers = (
    tf_upgrade_v2.TFAPIChangeSpec().function_transformers)
keyword_renames = (
    tf_upgrade_v2.TFAPIChangeSpec().function_keyword_renames)

# Visitor that converts to V2 and checks V2 argument names.
def conversion_visitor(unused_path, unused_parent, children):
    for child in children:
        _, attr = tf_decorator.unwrap(child[1])
        if not tf_inspect.isfunction(attr):
            continue
        names_v1 = tf_export.get_v1_names(attr)
        arg_names_v1 = get_args(attr)

        for name in names_v1:
            tf_name = "tf.%s" % name
            if tf_name in function_warnings or tf_name in function_transformers:
                continue  # These require manual change
            if tf_name in v1_name_exceptions:
                continue
            # Assert that arg names after converting to v2 are present in
            # v2 function.
            # 1. First, create an input of the form:
            #    tf.foo(arg1=val1, arg2=val2, ...)
            args = ",".join(
                ["%s=%d" % (from_name, from_index)
                 for from_index, from_name in enumerate(arg_names_v1)])
            text_input = "%s(%s)" % (tf_name, args)
            # 2. Convert the input to V2.
            _, _, _, text = self._upgrade(text_input)
            new_function_name, new_args = get_func_and_args_from_str(text)
            if "__internal__" in new_function_name:
                # Skip the tf.__internal__ and tf.keras.__internal__ API.
                continue
            if new_function_name == "tf.compat.v1.%s" % name:
                if tf_name in keyword_renames:
                    # If we rename arguments, new function must be available in 2.0.
                    # We should not be using compat.v1 in this case.
                    self.fail(
                        "Function '%s' is not in 2.0 when converting\n%s\nto\n%s" %
                        (new_function_name, text_input, text))
                continue
            if new_function_name.startswith("tf.compat.v2"):
                self.assertIn(new_function_name.replace("tf.compat.v2.", "tf."),
                              self.v2_symbols)
                continue
            # 3. Verify V2 function and arguments.
            args_v2 = get_args(self.v2_symbols[new_function_name])
            args_v2.extend(v2_arg_exceptions)
            for new_arg in new_args:
                self.assertIn(
                    new_arg, args_v2,
                    "Invalid argument '%s' in 2.0 when converting\n%s\nto\n%s.\n"
                    "Supported arguments: %s" % (
                        new_arg, text_input, text, str(args_v2)))
            # 4. Verify that the argument exists in v1 as well.
            if new_function_name in set(["tf.nn.ctc_loss",
                                         "tf.saved_model.save"]):
                continue
            args_v1 = get_args(self.v1_symbols[new_function_name])
            args_v1.extend(v2_arg_exceptions)
            for new_arg in new_args:
                self.assertIn(
                    new_arg, args_v1,
                    "Invalid argument '%s' in 1.0 when converting\n%s\nto\n%s.\n"
                    "Supported arguments: %s" % (
                        new_arg, text_input, text, str(args_v1)))

visitor = public_api.PublicAPIVisitor(conversion_visitor)
visitor.do_not_descend_map["tf"].append("contrib")
visitor.private_map["tf.compat"] = ["v1", "v2"]
traverse.traverse(tf.compat.v1, visitor)
