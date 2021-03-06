# Docs

This page contains the documentation for the classes and methods in the `mcautograder` package.

---

**_class_ `notebook.Notebook`**

Multiple choice question autograder for Jupyter Notebook


**_method_ `notebook.Notebook.check(self, identifier, answer)`**


Visible wrapper for `Notebook._check_answer` to print output based on whether or not student's
answer is correct

Args:

* `identifier` (`str`): The question identifier
* `answer` (`str`, `int`): The student's answer

Returns:

* `None`. Prints out student's result on question



**_method_ `notebook.Notebook.score(self)`**


If assignment is scored, displays student's score as fraction and percentage.



---

**_function_ `utils.repeat(x, n)`**


Returns a list of a given value repeated a given number of times

Args:

* `x` (any): The value to repeat
* `n` (`int`): The number of repetitions

Returns:

* `list`. List of repeated values `x`



**_function_ `utils.serialize(obj, file)`**


Serializes an object and writes its bytes to a file

Args:

* `obj` (any): Object to be serialized
* `file` (file object): File to write bytes into



