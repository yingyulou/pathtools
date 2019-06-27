# pathtools
Utility functions for path operations.

* enter

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

    * enterPath, str
        The path you need to enter.


* walk

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


* iwalk

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