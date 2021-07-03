import os
import antlr4
import argparse
from verilogToZ3.verilogVisitor import verilogVisitor
from verilogToZ3.Verilog2001Lexer import Verilog2001Lexer
from verilogToZ3.Verilog2001Parser import Verilog2001Parser

if __name__ == "__main__":
	# Select spec file to parse
	parser = argparse.ArgumentParser()
	parser.add_argument("--spec", type=int, default=1, help="Enter values from 1 to 5")
	args = parser.parse_args()
	filename = "sample"+str(args.spec)+"_skolem.v"

	# Parse Skolem Function from Manthan and
	# Generate Z3Py Format
	f = open("sample_skf/"+filename, "r")
	data = f.read()
	inputStream = antlr4.InputStream(data)
	lexer = Verilog2001Lexer(inputStream)
	tokenStream = antlr4.CommonTokenStream(lexer)
	parser = Verilog2001Parser(tokenStream)
	tree = parser.module_declaration()
	visitor = verilogVisitor()
	z3filecontent = visitor.visit(tree)
	with open('verilogToZ3/templateZ3Checker.py', 'r') as file :
		filedata = file.read()
	filedata = filedata.replace('#*#', z3filecontent)
	with open('z3ValidityChecker.py', 'w') as file:
		file.write(filedata)
	
	# Run the Validity Checker File
	os.system("python z3ValidityChecker.py")
