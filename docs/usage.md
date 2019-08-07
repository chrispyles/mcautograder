# Usage

[Home](index) | [Usage](usage) | [Tests](tests) | [Docs](docs) | [License](license) | [Help](help)

To use the autograder, import the `mcautograder` package and make sure to your [tests file](#tests) with your notebook. When you load the notebook dependencies, import the file and initialize the grader by creating an instance of the `Notebook` class (the argument to pass is the path to your tests file):

```python
import mcautograder
grader = mcautograder.Notebook("tests.py")
```

If you want the autograder to score the questions, make sure to set `scored=True` in your `Notebook` call. **The default behavior of the autograder is to allow students to submit answers until they get the correct one.** If you want to change this behavior, you must set the `max_attempts` argument to an integer, the maximum number of retakes allowed. If this is the case, when students hit that ceiling, the check cells will throw an `AssertionError` because they've hit the retake ceiling.

An example call for a scored notebook with a retake ceiling of 5 is given below.

```python
grader = Notebook("tests.py", scored=True, max_attempts=5)
```

To use the autograder to check answers, have students assign their answers to variables in the notebook; these answers can strings of length 1 or single-digit integers. Then call the `Notebook.check()` function; the first argument should be the question identifier in your tests file and the second should be the variable the student created.

```python
my_answer = "A"
grader.check("q1", my_answer)
```

If the student's response matches the test file, then `Correct.` will be printed; otherwise, `Try again.` will be printed. If the student enters an invalid response (e.g. `float`, answer of > 1 character, hit retake ceiling), the grader will throw an `AssertionError` with a descriptive message.

To get the score on a scored autograder, simply call `Notebook.score()`:

```python
grader.score()
```

The output will contain the fraction of earned points out of possible points and the percentage.

For a more descriptive introduction to the autograder, launch our [Binder](https://mybinder.org/v2/gh/chrispyles/mcautograder/master?filepath=demo/mcautograder-demo.ipynb).