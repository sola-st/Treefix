from flask import Flask # pragma: no cover
from flask.blueprints import BlueprintSetupState # pragma: no cover

self = type('MockBlueprint', (object,), {})() # pragma: no cover
app = Flask(__name__) # pragma: no cover
options = {} # pragma: no cover
first_registration = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Creates an instance of :meth:`~flask.blueprints.BlueprintSetupState`
        object that is later passed to the register callback functions.
        Subclasses can override this to return a subclass of the setup state.
        """
aux = BlueprintSetupState(self, app, options, first_registration)
_l_(22875)
exit(aux)
