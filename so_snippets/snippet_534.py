# Extracted from https://stackoverflow.com/questions/33945261/how-to-specify-multiple-return-types-using-type-hints
from typing import Union


def foo(client_id: str) -> Union[list,bool]

def foo(a:str) -> list:
foo(1)
'Works'

foo.__annotations__ 
{'return': <class 'list'>, 'a': <class 'str'>}

def foo(client_id: str) -> list | bool:

