# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Decorator that registers the given dispatch target."""
if not callable(dispatch_target):
    raise TypeError("Expected dispatch_target to be callable; "
                    f"got {dispatch_target!r}")
dispatch_target = _add_name_scope_wrapper(dispatch_target, api_signature)
_check_signature(api_signature, dispatch_target)

for signature_checker in signature_checkers:
    dispatcher.Register(signature_checker, dispatch_target)
_TYPE_BASED_DISPATCH_SIGNATURES[api][dispatch_target].extend(signatures)

if not signature_checkers:
    signature = _signature_from_annotations(dispatch_target)
    checker = _make_signature_checker(api_signature, signature)
    dispatcher.Register(checker, dispatch_target)
    _TYPE_BASED_DISPATCH_SIGNATURES[api][dispatch_target].append(signature)

exit(dispatch_target)
