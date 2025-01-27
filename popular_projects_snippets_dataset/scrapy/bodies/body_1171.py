# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
"""Helper function for Request.to_dict"""
# Only instance methods contain ``__func__``
if obj and hasattr(func, '__func__'):
    members = inspect.getmembers(obj, predicate=inspect.ismethod)
    for name, obj_func in members:
        # We need to use __func__ to access the original function object because instance
        # method objects are generated each time attribute is retrieved from instance.
        #
        # Reference: The standard type hierarchy
        # https://docs.python.org/3/reference/datamodel.html
        if obj_func.__func__ is func.__func__:
            exit(name)
raise ValueError(f"Function {func} is not an instance method in: {obj}")
