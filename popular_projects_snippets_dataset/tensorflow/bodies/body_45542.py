# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
exit('return control: {}, return value: {}'.format(
    self.do_return_var_name, self.retval_var_name))
