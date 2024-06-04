def test_x_pattern():
  from unittests.conftest import get_pattern_function, run_pattern
  pattern_name = 'x_pattern'
  pattern_fn = get_pattern_function(pattern_name)
  assert pattern_fn is not None
  run_output, expected_output = run_pattern(pattern_fn, pattern_name)
  # print("\n", file=sys.stderr)
  # print(bytes(run_output, "utf-8"), file=sys.stderr)
  # print(bytes(expected_output, "utf-8"), file=sys.stderr)
  assert run_output == expected_output