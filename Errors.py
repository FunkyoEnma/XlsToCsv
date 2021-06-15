import os
from typing import overload

##################################
# CheckPath
##################################


@overload
def checkPath(path: str) -> None: ...


@overload
def checkPath(path: list) -> None: ...


@overload
def checkPath(*paths: str) -> None: ...


def checkPath(*args):
    """
    Check if filePath is correct and Exist
    """
    for i in args:
        if type(i) is str and not os.path.isdir(os.path.split(i)[0]):
            raise ValueError(f"Element in position arg[{args[i]}]: '{args[0]}' is not pathLike or not exist.")

    if type(args[0]) is list:
        if type(args[0]) is list:
            for i in args[0]:
                if type(i) is not str:
                    raise TypeError(f"Element in position {args[0].index(i)} of the list is type {type(i)},"
                                    f" all elements of the list must be type str.")
                elif not os.path.isdir(os.path.split(i)[0]):
                    raise ValueError(f"Element in position {args[0].index(i)}: '{i}',"
                                     f" is not pathLike or not exist.")
