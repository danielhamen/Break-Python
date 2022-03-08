from __future__ import print_function

def br(Lines=1, Return=False):
    """
    Either `print()` or `return` a newline (`\\n`) * `Lines`
    """

    BreakString = "\n" * (int(Lines) - 1)
    if Return is False:
        print(BreakString)
    else:
        return BreakString

def pbr(Lines):
    """
    `print()` a newline (`\\n`) * `Lines`
    """

    BreakString = "\n" * (int(Lines) - 1)
    print(BreakString)

def rbr(Lines):
    """
    `return` a newline (`\\n`) * `Lines`
    """

    BreakString = "\n" * int(Lines - 1)
    return BreakString
