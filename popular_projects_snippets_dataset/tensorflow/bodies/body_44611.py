# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables.py
raise UnboundLocalError("'{}' is used before assignment".format(
    self.symbol_name))
