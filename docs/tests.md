# Tests

The autograder relies on a tests file to get the answers for the questions. In this repo, the file is `tests.py` and it is public; in practice, I usually distribute the answers as a hidden file, `.tests.py`. It is unhidden here so that you can peruse its structure and contents.

The `Notebook` constructor by default assumes that your tests are in the file `.tests.py`. If you have a different preferred location, you can pass the path to the file by setting the `tests` argument of the constructor:

```python
grader = Notebook(tests=SOME_OTHER_PATH)
```

In the file, we define a variable `answers` which is a list containing dictionaries, each of which represents a single question. Each dictionary should contain 3 keys: `"identifier"`, `"answer"`, and, optionally, `"points"`. If your assignment is unscored, you can leave off the `"points"` key. A description of the keys' values is given below:

| Key | Value Type | Value Description |
|-----|-----|-----|
| `"identifier"` | `str` | a unique question identifier |
| `"answer"` | `str`, `int` | the answer to the question; specifications below |
| `"points"` | `int` | optional; the number of points assigned to that question |

Answers **must** be of length 1 (i.e. a single-character string or a single-digit integer). The autograder is currently set up to throw an `AssertionError` if an answer of length > 1 is submitted, although we do intend to add this functionality later.

An example of a file is given below.

```python
answers = [
	{
		"identifier": "q1",
		"answer": 3,
		"points": 1,
	}, {
		"identifier": "q2",
		"answer": 2,
		"points": 2,
	}, {
		"identifier": "q3",
		"answer": "D",
		"points": 3,
	}
]
```

The identifiers have no set format. This is because the identifier is passed to `Notebook.check()` when you call it in the notebook.