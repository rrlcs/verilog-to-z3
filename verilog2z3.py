import sys

import antlr4
import argparse

from verilogToZ3Py.Verilog2001Lexer import Verilog2001Lexer
from verilogToZ3Py.Verilog2001Parser import Verilog2001Parser
from verilogToZ3Py.verilogToZ3Visitor import verilogVisitor


def preparez3(verilog_spec, verilog_spec_location):
    '''
    Input: verilog file
    Output: z3py equivalent of verilog file
    Functionality: Parses the verilog file and converts it to z3py format.
                                    It does the same for the NN output as well.
    '''

    # verilog_spec = "sampleskf.v"
    # verilog_spec_location = ""
    filename = verilog_spec_location+verilog_spec
    f = open(filename, "r")
    data = f.read()
    inputStream = antlr4.InputStream(data)
    lexer = Verilog2001Lexer(inputStream)
    tokenStream = antlr4.CommonTokenStream(lexer)
    parser = Verilog2001Parser(tokenStream)
    tree = parser.module_declaration()
    visitor = verilogVisitor(
        verilog_spec, verilog_spec_location)
    z3filecontent = visitor.visit(tree)
    with open('verilogToZ3Py/templateZ3Checker.py', 'r') as file:
        filedata = file.read()
        file.close()
    filedata = filedata.replace('#*#', z3filecontent)
    with open(verilog_spec+'.py', 'w') as file:
        file.write(filedata)
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--verilog_spec", type=str)
    args = parser.parse_args()
    path = 'benchmarks/verilog/'
    preparez3(args.verilog_spec, path)
