# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
from l3.Runtime import _l_
try:
    import datetime, time
    _l_(2002)

except ImportError:
    pass
def convert_enddate_to_seconds(self, ts):
    _l_(2006)

    """Takes ISO 8601 format(string) and converts into epoch time."""
    dt = datetime.datetime.strptime(ts[:-7],'%Y-%m-%dT%H:%M:%S.%f')+\
                datetime.timedelta(hours=int(ts[-5:-3]),
                minutes=int(ts[-2:]))*int(ts[-6:-5]+'1')
    _l_(2003)
    seconds = time.mktime(dt.timetuple()) + dt.microsecond/1000000.0
    _l_(2004)
    aux = seconds
    _l_(2005)
    return aux
try:
    import datetime, time
    _l_(2008)

except ImportError:
    pass
ts = '2012-09-30T15:31:50.262-08:00'
_l_(2009)
dt = datetime.datetime.strptime(ts[:-7],'%Y-%m-%dT%H:%M:%S.%f')+ datetime.timedelta(hours=int(ts[-5:-3]), minutes=int(ts[-2:]))*int(ts[-6:-5]+'1')
_l_(2010)
seconds = time.mktime(dt.timetuple()) + dt.microsecond/1000000.0
_l_(2011)
seconds
_l_(2012)
1348990310.26
_l_(2013)

