# 📘 Assignment: Python Testing with pytest

## 🎯 Objective

Learn how to write and run tests in Python using pytest so you can verify that functions behave correctly and catch errors early.

## 📝 Tasks

### 🛠️ Write Basic Function Tests

#### Description
Create tests for a few simple Python functions that perform math or string operations.

#### Requirements
Completed program should:

- Write test functions using `assert` statements.
- Test at least three behaviors, such as addition, subtraction, or string formatting.
- Use meaningful test names that describe the behavior being checked.
- Run the tests with `pytest` and confirm they pass.
- Example:
  ```python
  def add(a, b):
      return a + b

  def test_add():
      assert add(2, 3) == 5
  ```

### 🛠️ Test Edge Cases

#### Description
Check that your functions still work correctly with values that might cause unusual behavior.

#### Requirements
Completed program should:

- Test at least one edge case such as zero, an empty string, or negative numbers.
- Confirm the function returns the expected result in each scenario.
- Write tests that cover both valid and edge-case inputs.
- Example:
  ```python
  def test_add_zero():
      assert add(0, 5) == 5
  ```

### 🛠️ Debug a Broken Function

#### Description
Fix a function that has a logic error and verify the fix using tests.

#### Requirements
Completed program should:

- Identify the bug in a provided function.
- Write tests that expose the bug before fixing it.
- Update the function so the tests pass.
- Explain briefly what was wrong with the original logic.
- Example:
  ```python
  def is_even(number):
      return number % 2 == 0
  ```
