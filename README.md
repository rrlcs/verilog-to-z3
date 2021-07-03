# Verilog To Z3 Converter
It Converts a subset of Boolean Formulae written in Verilog format to Z3Py acceptable format. Uses an [ANTLR4](/https://github.com/antlr/antlr4) to create Parsers and Visitors.

## Requirements
- ANTLR4
Read Instructions on /https://github.com/antlr/antlr4 or follow Tomassetti's tutorial https://tomassetti.me/antlr-mega-tutorial/
- z3Py
```pip install z3-solver```
- Argparse
```pip install argparse```
- Python 3

## Test
```python main.py --spec=4```

## More Options
```python main.py --help```

### Resources
Gabriele Tomassetti's [ANTLR Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/)

### Acknowledgement
Thanks to [Stanly Samuel](https://github.com/stanlysamuel) for teaching me Visitor Design Patterns and Clarifying doubts.