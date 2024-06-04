import io
import sys
import os
import patternlib

def get_pattern_function(pattern):
  fn = getattr(patternlib, pattern)
  if fn and hasattr(fn, '__call__'):
    return fn
  return None


def run_pattern(pattern_fn, pattern_name):
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  pattern_fn()
  sys.stdout = sys.__stdout__ 
  run_output = capturedOutput.getvalue()
  expected_output = None
  basedir = os.path.dirname(os.path.abspath(__file__))
  fname = '%s/../outputs/%s' % (basedir, pattern_name)
  with open(fname, 'rb') as f:
    o_bytes = f.read()
    expected_output = o_bytes.decode('utf-8')
  return run_output, expected_output

