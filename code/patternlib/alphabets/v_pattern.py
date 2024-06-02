from patternlib.constants.patternlib_constants import ROWS5

MINROW = 3


def v_pattern(rows=ROWS5):
    '''
    *       *
     *     *
      *   *
       * *
        *

    This generates V - Pattern.

    To view pattern run: 'print(v_pattern.__doc__)'
    '''
    if rows < MINROW:
        print("E-Pattern generation failed, number of rows has to be greater than %d..." % MINROW)
    else:
        for i in range(rows, 0, -1):
            if i == 1:
                print(('* ' * i).center(2 * rows))
            else:
                print(('* ' + '  ' * (i - 2) + '* ').center(2 * rows))