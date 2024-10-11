# Extracted from https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
from print_dict import pd

dict1 = {
    'key': 'value'
} 

pd(dict1)

{
    'key': 'value'
}

{
    'one': 'value-one',
    'two': 'value-two',
    'three': 'value-three',
    'four': {
        '1': '1',
        '2': '2',
        '3': [1, 2, 3, 4, 5],
        '4': {
            'method': <function custom_method at 0x7ff6ecd03e18>,
            'tuple': (1, 2),
            'unicode': '✓',
            'ten': 'value-ten',
            'eleven': 'value-eleven',
            '3': [1, 2, 3, 4]
        }
    },
    'object1': <__main__.Object1 object at 0x7ff6ecc588d0>,
    'object2': <Object2 info>,
    'class': <class '__main__.Object1'>
}

pip install print-dict

