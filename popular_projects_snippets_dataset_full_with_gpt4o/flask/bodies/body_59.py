# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.context_processor` but for a blueprint.  Such a
        function is executed each request, even if outside of the blueprint.
        """
self.record_once(
    lambda s: s.app.template_context_processors.setdefault(None, []).append(f)
)
exit(f)
