# Extracted from https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal
'{{0}, {1}}'.format(1,2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    '{{0}, {1}}'.format(1,2)
ValueError: Single '}' encountered in format string
'{%s, %s}'%(1,2)
'{1, 2}'


