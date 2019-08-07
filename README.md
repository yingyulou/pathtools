# pathtools

Utility functions for path operations.

## enter

### Description

Auto enter and exit a path.

### Usage

``` Python
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
```

### Argument

1. enterPath, str

The path you need to enter

## walk

### Description

Walk (like os.walk) and glob (like glob.glob) files under a path.

Return a list.

### Usage

``` Python
from pathtools import walk

for fileName in walk('xxxPath', '.xxx'):
    # Get all the '*.xxx' files in all folders under 'xxxPath'
```

### Argument

1. folderPath, str

The path of the folder to walk.

2. extStr = '', str

The extension of the target file.

## iwalk

### Description

Walk (like os.walk) and glob (like glob.iglob) files under a path.

Return a generator.

### Usage

``` Python
from pathtools import iwalk

for fileName in iwalk('xxxPath', '.xxx'):
    # Get all the '*.xxx' files in all folders under 'xxxPath'
```

### Argument

1. folderPath, str

The path of the folder to walk.

2. extStr = '', str

The extension of the target file.
