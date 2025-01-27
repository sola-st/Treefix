# Extracted from ./data/repos/flask/src/flask/cli.py
"""Wraps a callback so that it's guaranteed to be executed with the
    script's application context.

    Custom commands (and their options) registered under ``app.cli`` or
    ``blueprint.cli`` will always have an app context available, this
    decorator is not required in that case.

    .. versionchanged:: 2.2
        The app context is active for subcommands as well as the
        decorated callback. The app context is always available to
        ``app.cli`` command and parameter callbacks.
    """

@click.pass_context
def decorator(__ctx, *args, **kwargs):
    if not current_app:
        app = __ctx.ensure_object(ScriptInfo).load_app()
        __ctx.with_resource(app.app_context())

    exit(__ctx.invoke(f, *args, **kwargs))

exit(update_wrapper(decorator, f))
