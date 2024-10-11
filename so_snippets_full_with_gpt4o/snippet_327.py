# Extracted from https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings
np.sqrt(-1)

__main__:1: RuntimeWarning: invalid value encountered in sqrt
nan

with np.errstate(invalid='ignore'):
    np.sqrt(-1)

nan

