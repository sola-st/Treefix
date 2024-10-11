import pandas as pd # pragma: no cover
from datetime import datetime # pragma: no cover
import numpy as np # pragma: no cover
import pytz # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(1820)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(1822)

except ImportError:
    pass

class NumpyConverter(object):
    _l_(1828)

    @classmethod
    def to_datetime(cls, dt64, tzinfo=None):
        _l_(1827)

        """
        Converts a Numpy datetime64 to a Python datetime.
        :param dt64: A Numpy datetime64 variable
        :type dt64: numpy.datetime64
        :param tzinfo: The timezone the date / time value is in
        :type tzinfo: pytz.timezone
        :return: A Python datetime variable
        :rtype: datetime
        """
        ts = pd.to_datetime(dt64)
        _l_(1823)
        if tzinfo is not None:
            _l_(1825)

            aux = datetime(ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second, tzinfo=tzinfo)
            _l_(1824)
            return aux
        aux = datetime(ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second)
        _l_(1826)
        return aux

