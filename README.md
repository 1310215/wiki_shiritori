# Wiki Shiritori

This is a simple "Shiritori" game using Wikipedia links. The program finds links on Wikipedia pages that start with the last character of the previous link, creating a chain of links.

## How to Play

1. Run the program using Python.
2. Enter a starting word.
3. The program will find Wikipedia links that start with the last character of the previous link and display the sequence.

## Requirements

- Python 3.x
- `requests` and `beautifulsoup4` packages

## Installation

Install the required packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the program:

```bash
python wiki_shiritori.py
```

## Example

```bash
Enter a starting word: Apple
Next word: Elephant
Next word: Tomato
...
```
