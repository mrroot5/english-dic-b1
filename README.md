# English Dictionary

My personal english dictionary from A1 to B1.

Here is a comparison between CEFR and Cambridge (2018).

![CERF and Cambridge comparison][cerf-cambridge-comparison]

[Image source](https://www.cambridgeenglish.org/exams-and-tests/cefr/)

## Features by word

- English word.

- Spanish translation.

- How to pronounce (spanish like characters).

- Phonetics (english pronuntiation).

- Category (money, food, etc.).

- Level (B1, C1, etc.).

- Aditional notes.

## Display features

~~A table with all the words and search option.~~

This feature is disabled but it is still in the source code.

## Prerequisites

- Python 3.
- Pip.
- Virtualenv.
- Liunux.

## Installation

Execute `source install.sh`.

## Development server

Execute `source run.sh` and navigate to `http://localhost:8000/`.

## Fresh start

**CAUTION** this option will remove migrations, database and virtualenv, then recreate the environment and database.

Execute `source clear-run.sh`.

[cerf-cambridge-comparison]: ./docs/images/cefr-diagram-2018.jpg