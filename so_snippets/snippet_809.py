# Extracted from https://stackoverflow.com/questions/9885217/in-python-if-i-return-inside-a-with-block-will-the-file-still-close
with locked(myLock):
    # Code here executes with myLock held.  The lock is
    # guaranteed to be released when the block is left (even
    # if via return or by an uncaught exception).

