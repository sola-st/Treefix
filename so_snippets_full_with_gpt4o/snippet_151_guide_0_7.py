from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
from l3.Runtime import _l_
try:
    from app import (
        app, abort, make_response, redirect, render_template, request, session
    )
    _l_(11839)

except ImportError:
    pass

