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
```python verilog2z3.py --verilog_spec=lut1_2_2.v```
Verilog benchmarks are in ```benchmarks/verilog``` 

## More Options
```python verilog2z3.py --help```

### Resources
Gabriele Tomassetti's [ANTLR Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/)

### Acknowledgement
Thanks to [Stanly Samuel](https://github.com/stanlysamuel) for helping me learn Visitor Design Patterns and Clarifying doubts.