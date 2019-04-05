import os
from subprocess import call

_EDITOR = os.environ.get('EDITOR', 'vim')
#: _SET_BACKUP needed for consistent behaviour on mac & linux
_SET_BACKUP = "+set backupcopy=yes"


def open(file, vim_args=None):
    """ Open the file object in vim.

    :param file: File-like object.
    :param vim_args: string of additional vim arguments.
    """
    file.flush()
    name = file.name

    cmd = [_EDITOR, _SET_BACKUP, name]
    if vim_args:
        cmd = [_EDITOR, "-c", vim_args, _SET_BACKUP, name]

    call(cmd)
    file.seek(0)
