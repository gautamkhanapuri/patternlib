def test_narrow_diamond():
  from unittests.conftest import get_pattern_function, run_pattern
  pattern_name = 'narrow_diamond'
  pattern_fn = get_pattern_function(pattern_name)
  assert pattern_fn is not None
  run_output, expected_output = run_pattern(pattern_fn, pattern_name)
  assert run_output == expected_output