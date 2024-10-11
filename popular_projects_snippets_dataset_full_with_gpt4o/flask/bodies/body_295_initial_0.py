from flask import Flask, session as flask_session, got_request_exception # pragma: no cover
from blinker import Namespace # pragma: no cover

session = flask_session # pragma: no cover
category = 'info' # pragma: no cover
message = 'This is a flash message.' # pragma: no cover
message_flashed = Namespace().signal('message-flashed') # pragma: no cover
current_app = Flask(__name__) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Flashes a message to the next request.  In order to remove the
    flashed message from the session and to display it to the user,
    the template has to call :func:`get_flashed_messages`.

    .. versionchanged:: 0.3
       `category` parameter added.

    :param message: the message to be flashed.
    :param category: the category for the message.  The following values
                     are recommended: ``'message'`` for any kind of message,
                     ``'error'`` for errors, ``'info'`` for information
                     messages and ``'warning'`` for warnings.  However any
                     kind of string can be used as category.
    """
# Original implementation:
#
#     session.setdefault('_flashes', []).append((category, message))
#
# This assumed that changes made to mutable structures in the session are
# always in sync with the session object, which is not true for session
# implementations that use external storage for keeping their keys/values.
flashes = session.get("_flashes", [])
_l_(19809)
flashes.append((category, message))
_l_(19810)
session["_flashes"] = flashes
_l_(19811)
message_flashed.send(
    current_app._get_current_object(),  # type: ignore
    message=message,
    category=category,
)
_l_(19812)
