from sniffer.api import * # import the really small API
import os, sys

# This fires runnables only if files ending with .py extension and not prefixed
# with a period.
@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

# This example simply runs nose.
@runnable
def execute_nose(*args):
    import nose

    args = args + ('--detailed-errors', '--nocapture')

    return nose.run(argv=list(args))
