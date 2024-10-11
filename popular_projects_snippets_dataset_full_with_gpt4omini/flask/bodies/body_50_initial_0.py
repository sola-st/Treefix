from flask import Blueprint # pragma: no cover
from flask import Flask # pragma: no cover

class MockApp:                           # Mock class to simulate the actual app # pragma: no cover
    class JinjaEnv:                      # Inner class to mock the Jinja environment # pragma: no cover
        tests = {}                       # Initialize tests as an empty dictionary # pragma: no cover
 # pragma: no cover
    jinja_env = JinjaEnv()               # Create an instance of the mock Jinja environment # pragma: no cover
 # pragma: no cover
class MockBlueprintSetupState:           # Mock class to represent the BlueprintSetupState # pragma: no cover
    def __init__(self):                  # Constructor to initialize the mock object # pragma: no cover
        self.app = MockApp()             # Initialize the app attribute with a mock app instance # pragma: no cover
 # pragma: no cover
self = MockBlueprintSetupState()          # Initialize the self variable # pragma: no cover
name = 'custom_test'                      # Set a name for the test # pragma: no cover
f = lambda x: x * 2                      # Define a simple function for testing # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a custom template test, available application wide.  Like
        :meth:`Flask.add_template_test` but for a blueprint.  Works exactly
        like the :meth:`app_template_test` decorator.

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """

def register_template(state: BlueprintSetupState) -> None:
    _l_(4821)

    state.app.jinja_env.tests[name or f.__name__] = f
    _l_(4820)

self.record_once(register_template)
_l_(4822)
