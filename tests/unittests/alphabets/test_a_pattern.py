# from patternlib import a_pattern
# import io
# import sys
# import os

# def test_a_pattern_old():
#   capturedOutput = io.StringIO()
#   sys.stdout = capturedOutput
#   a_pattern()
#   sys.stdout = sys.__stdout__
#   a = capturedOutput.getvalue()
#   basedir = os.path.dirname(os.path.abspath(__file__))
#   fname = '%s/../../outputs/a_pattern' % basedir
#   # f = open('tests/outputs/a_pattern', 'rb')
#   f = open(fname, 'rb')
#   b = f.read()
#   c = b.decode('utf-8')
#   assert a == c

def test_a_pattern():
  from unittests.conftest import get_pattern_function, run_pattern
  pattern_name = 'a_pattern'
  pattern_fn = get_pattern_function(pattern_name)
  assert pattern_fn is not None
  run_output, expected_output = run_pattern(pattern_fn, pattern_name)
  assert run_output == expected_output
