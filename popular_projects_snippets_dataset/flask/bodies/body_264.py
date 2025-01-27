# Extracted from ./data/repos/flask/src/flask/cli.py
self._load_plugin_commands()
# Look up built-in and plugin commands, which should be
# available even if the app fails to load.
rv = super().get_command(ctx, name)

if rv is not None:
    exit(rv)

info = ctx.ensure_object(ScriptInfo)

# Look up commands provided by the app, showing an error and
# continuing if the app couldn't be loaded.
try:
    app = info.load_app()
except NoAppException as e:
    click.secho(f"Error: {e.format_message()}\n", err=True, fg="red")
    exit(None)

# Push an app context for the loaded app unless it is already
# active somehow. This makes the context available to parameter
# and command callbacks without needing @with_appcontext.
if not current_app or current_app._get_current_object() is not app:
    ctx.with_resource(app.app_context())

exit(app.cli.get_command(ctx, name))
