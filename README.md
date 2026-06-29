# Number to Language

A Python package that converts decimal numbers represented as strings into their English-language equivalents.

## Example

```python
>>> num_to_language("0")
"zero"

>>> num_to_language("123")
"one hundred twenty-three"

>>> num_to_language("1001")
"one thousand one"

>>> num_to_language("999999999999")
"nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"
```

## Features

- Converts decimal strings to English words.
- Supports numbers from 0 through 999,999,999,999.
- Input validation.
- Unit tested.
- Modular project structure.

## Project Structure

```
num_to_language/
│
├── converter.py
├── validation.py
├── constants.py
├── type_defs.py
└── main.py
```

## Running

```bash
python -m num_to_language.main
```

## Running Tests

```bash
python -m unittest discover
```

## Future Improvements

- Support negative numbers.
- Support decimal values.
- Support numbers greater than one trillion.
- Localization for additional languages.