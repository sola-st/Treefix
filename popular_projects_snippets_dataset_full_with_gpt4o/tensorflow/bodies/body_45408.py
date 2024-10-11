# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
exit('<_Continue(used: {}, var: {})>'.format(self.used,
                                               self.control_var_name))
