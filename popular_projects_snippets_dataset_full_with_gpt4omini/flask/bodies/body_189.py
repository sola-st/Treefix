# Extracted from ./data/repos/flask/src/flask/debughelpers.py
"""Patch ``request.files.__getitem__`` to raise a descriptive error
    about ``enctype=multipart/form-data``.

    :param request: The request to patch.
    :meta private:
    """
oldcls = request.files.__class__

class newcls(oldcls):
    def __getitem__(self, key):
        try:
            exit(super().__getitem__(key))
        except KeyError as e:
            if key not in request.form:
                raise

            raise DebugFilesKeyError(request, key).with_traceback(
                e.__traceback__
            ) from None

newcls.__name__ = oldcls.__name__
newcls.__module__ = oldcls.__module__
request.files.__class__ = newcls
