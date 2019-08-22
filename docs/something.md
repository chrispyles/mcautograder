**_class_ `notebook.Notebook`**

Multiple choice question autograder for Jupyter Notebook

**_method_ `notebook.Notebook.check(self, identifier, answer)`**

Visible wrapper for `Notebook._check_answer` to print output based on whether or not student'sanswer is correct    Args:* `identifier` (`str`): The question identifier* `answer` (`str`, `int`): The student's answerReturns:* `None`. Prints out student's result on question

**_method_ `notebook.Notebook.score(self)`**

If assignment is scored, displays student's score as fraction and percentage.

---

**_function_ `utils.repeat(x, n)`**

Returns a list of a given value repeated a given number of timesArgs:* `x` (any): The value to repeat* `n` (`int`): The number of repetitionsReturns:* `list`. List of repeated values `x`

**_function_ `utils.serialize(obj, file)`**

Serializes an object and writes its bytes to a fileArgs:* `obj` (any): Object to be serialized* `file` (file object): File to write bytes into
