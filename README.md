# Multiple Choice Autograder

This repository contains a small Python-based multiple-choice question autograder inteded for use in Jupyter Notebooks. It is meant to be packaged with each assignment so that they are easier for use on third-party servers, e.g. MyBinder.

## Usage

To use the autograder, just include the `mcautograder.py` file in the directory containing your notebook, along with your [tests file](#tests). When you load the notebook dependencies, import the file and initialize the grader by creating an instance of the `Notebook` class (the argument to pass is the path to your tests file):

```python
import mcautograder
grader = mcautograder.Notebook("tests.txt")
```

To use the autograder to check answers, have students assign their answers to variables in the notebook; these answers can strings of length 1 or single-digit integers. Then call the `Notebook.check()` function; the first argument should be the question identifier in your tests file and the second should be the variable the student created.

```python
my_answer = "A"
grader.check("q1", my_answer)
```

If the student's response matches the test file, then `Correct.` will be printed; otherwise, `Try again.` will be printed. If the student enters an invalid response (e.g. `float`, answer of > 1 character), the grader will throw an `AssertionError` with a descriptive message.

For a more descriptive introduction to the autograder, launch our [Binder]().

<div id="tests"></div>

## Tests

The autograder relies on a tests file to get the answers for the questions. In this repo, the file is `tests.txt` and it is public; in practice, I usually distribute the answers as a hidden file, `.tests.txt`. It is unhidden here so that you can peruse its structure and contents.

The file has a specific format: each line represents a single question, with an identifier and an answer. The structure should be `identifier answer` (note the space). Answers **must** be of length 1 (i.e. a single-character string or a single-digit integer).

An example of a file is given below.

```
q1 1
q2_1 3
q2_2 2
q3 A
q4 E
q5 C
question6 7
```

The identifiers have no set format, other than that they cannot contain a space. This is because the identifier is passed to `Notebook.check()` when you call it in the notebook.