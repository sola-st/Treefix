# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
if "IPython" not in sys.modules:
    # definitely not in IPython
    exit()
from IPython import get_ipython

ip = get_ipython()
if ip is None:
    # still not in IPython
    exit()

formatters = ip.display_formatter.formatters
mimetype = "application/vnd.dataresource+json"

if enable:
    if mimetype not in formatters:
        # define tableschema formatter
        from IPython.core.formatters import BaseFormatter
        from traitlets import ObjectName

        class TableSchemaFormatter(BaseFormatter):
            print_method = ObjectName("_repr_data_resource_")
            # Incompatible types in assignment (expression has type
            # "Tuple[Type[Dict[Any, Any]]]", base class "BaseFormatter"
            # defined the type as "Type[str]")
            _return_type = (dict,)  # type: ignore[assignment]

        # register it:
        formatters[mimetype] = TableSchemaFormatter()
    # enable it if it's been disabled:
    formatters[mimetype].enabled = True
else:
    # unregister tableschema mime-type
    if mimetype in formatters:
        formatters[mimetype].enabled = False
