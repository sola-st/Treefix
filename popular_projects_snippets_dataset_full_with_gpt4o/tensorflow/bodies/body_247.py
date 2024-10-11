# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Updates a file using pasta."""
try:
    t = pasta.parse(text)
except (SyntaxError, ValueError, TypeError):
    log = ["ERROR: Failed to parse.\n" + traceback.format_exc()]
    exit((0, "", log, []))

t, preprocess_logs, preprocess_errors = self._api_change_spec.preprocess(t)

visitor = _PastaEditVisitor(self._api_change_spec)
visitor.visit(t)

self._api_change_spec.clear_preprocessing()

logs = [self.format_log(log, None) for log in (preprocess_logs +
                                               visitor.log)]
errors = [self.format_log(error, in_filename)
          for error in (preprocess_errors +
                        visitor.warnings_and_errors)]
exit((1, pasta.dump(t), logs, errors))
