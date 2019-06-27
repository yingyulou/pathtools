#!/bin/env python
# coding=UTF-8

'''
DESCRIPTION

    pathtools

    Utility functions for path operations.

VERSION

    1.4.0

LATEST UPDATE

    2019.6.10

'''

# Import Python Lib.
import os
from os import getcwd, chdir
from os.path import join
from functools import wraps

################################################################################
# Auto Enter And Exit A Path
################################################################################

class enter(object):

    '''
        DESCRIPTION

            Auto enter and exit a path.

        USAGE

            from pathtools import enter

            # Now we in the outside path

            with enter('xxxPath'):
                # Now we in the xxxPath
                ...

            # Now we return to the outside path

            # Or use it as a decorator

            # Now we in the outside path

            @enter('xxxPath')
            def xxx():
                # Now we in the xxxPath
                ...

            # Now we return to the outside path

        ARGUMENT

            * __enterPath, str
                The path you need to enter.
    '''

    __slots__ = ('__enterPath', '__cwdPath')

    def __init__(self, __enterPath):

        self.__cwdPath = getcwd()
        self.__enterPath = __enterPath


    def __enter__(self):

        chdir(self.__enterPath)


    def __exit__(self, *exc_info):

        chdir(self.__cwdPath)


    def __call__(self, funcObj):

        @wraps(funcObj)
        def innerFunc(*args, **kwargs):

            chdir(self.__enterPath)
            returnTuple = funcObj(*args, **kwargs)
            chdir(self.__cwdPath)

            return returnTuple

        return innerFunc


################################################################################
# Walk And Glob
################################################################################

def walk(folderPath, extStr = ''):

    '''
        DESCRIPTION

            Walk (like os.walk) and glob (like glob.glob) files under a path.

            Return a list.

        USAGE

            from pathtools import walk

            for fileName in walk('xxxPath', '.xxx'):
                # Get all the '*.xxx' files in all folders under 'xxxPath'

        ARGUMENT

            * folderPath, str
                The path of the folder to walk.

            * extStr = '', str
                The extension of the target file.
    '''

    return [join(nowPath, fileName) for nowPath, _, fileNameList in os.walk(folderPath)
        for fileName in fileNameList if fileName.endswith(extStr)]


################################################################################
# Walk And Glob (Iter)
################################################################################

def iwalk(folderPath, extStr = ''):

    '''
        DESCRIPTION

            Walk (like os.walk) and glob (like glob.iglob) files under a path.

            Return a generator.

        USAGE

            from pathtools import iwalk

            for fileName in iwalk('xxxPath', '.xxx'):
                # Get all the '*.xxx' files in all folders under 'xxxPath'

        ARGUMENT

            * folderPath, str
                The path of the folder to walk.

            * extStr = '', str
                The extension of the target file.
    '''

    for nowPath, _, fileNameList in os.walk(folderPath):
        for fileName in fileNameList:
            if fileName.endswith(extStr):
                yield join(nowPath, fileName)