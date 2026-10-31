# Programming Hangman (Python)

[Leia em português](README.pt-br.md)

A hangman game that runs in the terminal, with words from the programming world (python, debug, framework, and more).

## How it works

- The game picks a random word and shows `_` for each hidden letter.
- You type one letter at a time. You have 6 attempts.
- Wrong letters cost one attempt. Repeated letters and invalid input (numbers, more than one letter) are ignored.
- You win by revealing the whole word and lose when the attempts run out.

## How to run

You need Python 3 installed.

```
python forca.py
```

You can also paste the code into [Google Colab](https://colab.research.google.com) and run it there.

## Concepts practiced

Variables, lists, loops (`while` and `for`), conditionals, user input, input validation, string formatting, and the `random` module.

## Notes

- This is a study project. The game text and word list are in Portuguese, and the words have no accents.
- Possible improvements: ASCII hangman drawing, difficulty levels, and a version using classes.
