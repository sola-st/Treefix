# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
exit({
    trackable.VARIABLE_VALUE_KEY:
        functools.partial(_DVariableSaveable, self)
})
