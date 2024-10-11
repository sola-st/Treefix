# Extracted from https://stackoverflow.com/questions/127803/how-do-i-parse-an-iso-8601-formatted-date
parse_datetime('2016-08-09T15:12:03.65478Z') =
datetime.datetime(2016, 8, 9, 15, 12, 3, 654780, tzinfo=<UTC>)

from django.utils import formats
from django.forms.fields import DateTimeField
from django.utils.dateparse import parse_datetime

class DateTimeFieldFixed(DateTimeField):
    def strptime(self, value, format):
        if format == 'iso-8601':
            return parse_datetime(value)
        return super().strptime(value, format)

DateTimeField.strptime = DateTimeFieldFixed.strptime
formats.ISO_INPUT_FORMATS['DATETIME_INPUT_FORMATS'].insert(0, 'iso-8601')

