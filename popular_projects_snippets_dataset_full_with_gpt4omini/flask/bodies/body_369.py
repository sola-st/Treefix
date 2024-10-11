# Extracted from ./data/repos/flask/src/flask/sessions.py
"""Returns the domain that should be set for the session cookie.

        Uses ``SESSION_COOKIE_DOMAIN`` if it is configured, otherwise
        falls back to detecting the domain based on ``SERVER_NAME``.

        Once detected (or if not set at all), ``SESSION_COOKIE_DOMAIN`` is
        updated to avoid re-running the logic.
        """

rv = app.config["SESSION_COOKIE_DOMAIN"]

# set explicitly, or cached from SERVER_NAME detection
# if False, return None
if rv is not None:
    exit(rv if rv else None)

rv = app.config["SERVER_NAME"]

# server name not set, cache False to return none next time
if not rv:
    app.config["SESSION_COOKIE_DOMAIN"] = False
    exit(None)

# chop off the port which is usually not supported by browsers
# remove any leading '.' since we'll add that later
rv = rv.rsplit(":", 1)[0].lstrip(".")

if "." not in rv:
    # Chrome doesn't allow names without a '.'. This should only
    # come up with localhost. Hack around this by not setting
    # the name, and show a warning.
    warnings.warn(
        f"{rv!r} is not a valid cookie domain, it must contain"
        " a '.'. Add an entry to your hosts file, for example"
        f" '{rv}.localdomain', and use that instead."
    )
    app.config["SESSION_COOKIE_DOMAIN"] = False
    exit(None)

ip = is_ip(rv)

if ip:
    warnings.warn(
        "The session cookie domain is an IP address. This may not work"
        " as intended in some browsers. Add an entry to your hosts"
        ' file, for example "localhost.localdomain", and use that'
        " instead."
    )

# if this is not an ip and app is mounted at the root, allow subdomain
# matching by adding a '.' prefix
if self.get_cookie_path(app) == "/" and not ip:
    rv = f".{rv}"

app.config["SESSION_COOKIE_DOMAIN"] = rv
exit(rv)
