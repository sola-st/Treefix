# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
session_public_methods = [
    method_tuple[0] for method_tuple in
    tf_inspect.getmembers(session.Session, predicate=tf_inspect.ismethod)
    if _is_public_method_name(method_tuple[0])]
wrapper_public_methods = [
    method_tuple[0] for method_tuple in
    tf_inspect.getmembers(
        framework.BaseDebugWrapperSession, predicate=tf_inspect.ismethod)
    if _is_public_method_name(method_tuple[0])]
missing_public_methods = [
    method for method in session_public_methods
    if method not in wrapper_public_methods]
self.assertFalse(missing_public_methods)
