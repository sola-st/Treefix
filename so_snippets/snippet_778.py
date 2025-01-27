# Extracted from https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
   <hash>       <key>    <value>
     null        null    null
     null        null    null
      ...         ...    ...

[null, 0, null, null, null, null, null, null]

   <hash>       <key>    <value>
      ...         ...    ...

     hash         key    dict_0    dict_1    dict_2...
      ...         ...    ...       ...       ...

