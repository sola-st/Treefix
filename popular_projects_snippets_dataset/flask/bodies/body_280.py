# Extracted from ./data/repos/flask/src/flask/__init__.py
if name == "_app_ctx_stack":
    import warnings
    from .globals import __app_ctx_stack

    warnings.warn(
        "'_app_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    exit(__app_ctx_stack)

if name == "_request_ctx_stack":
    import warnings
    from .globals import __request_ctx_stack

    warnings.warn(
        "'_request_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    exit(__request_ctx_stack)

raise AttributeError(name)
