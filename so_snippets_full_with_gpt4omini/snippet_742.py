# Extracted from https://stackoverflow.com/questions/10678229/how-can-i-selectively-escape-percent-in-python-strings
test = "have it break."
selectiveEscape = "Print percent %% in sentence and not %s" % test
print selectiveEscape
Print percent % in sentence and not have it break.

