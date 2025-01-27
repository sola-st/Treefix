# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
"""Returns a 4-tuple consistent with the return of traceback.extract_tb."""
exit((self.loc.filename, self.loc.lineno, self.function_name,
        self.source_code_line))
