from lark import Lark

# Define matrix operations grammar
matrix_grammar = """
start: statement+

statement: matrix_operation
        | matrix_assignment

matrix_operation: matrix_operation_addition
                | matrix_operation_subtraction
                | matrix_operation_multiplication
                | matrix_operation_transpose
                | matrix_operation_largest_value
                | matrix_operation_smallest_value
                | matrix_operation_row_sum
                | matrix_operation_column_sum
                | matrix_operation_row_multiplication

matrix_operation_addition: "matrix_addition" matrix_name "to" matrix_name end_statement

matrix_operation_subtraction: "matrix_subtraction" matrix_name "from" matrix_name end_statement

matrix_operation_multiplication: "matrix_multiplication" matrix_name "with" matrix_name end_statement

matrix_operation_transpose: "matrix_transpose" matrix_name end_statement

matrix_operation_largest_value: "matrix_largest_value" matrix_name end_statement

matrix_operation_smallest_value: "matrix_smallest_value" matrix_name end_statement

matrix_operation_row_sum: "matrix_row_sum" matrix_name row_number end_statement

matrix_operation_column_sum: "matrix_column_sum" matrix_name column_number end_statement

matrix_operation_row_multiplication: "matrix_row_multiplication" matrix_name row_number literal_value end_statement

matrix_assignment: "matrix" matrix_name "is" matrix_definition end_statement

matrix_definition: "[" row ("," row)* "]"

row: "[" literal_value ("," literal_value)* "]"

matrix_name: CNAME

row_number: SIGNED_INT

column_number: SIGNED_INT

literal_value: SIGNED_INT

end_statement: ";"

%import common.CNAME
%import common.SIGNED_INT
%import common.WS
%ignore WS

"""

# Create Lark parser
parser = Lark(matrix_grammar, start='start', parser='lalr', transformer=None)

# Prompt user for matrix operation
operation = input("Enter a input: ")

# Parse matrix operation
matrix_operation = parser.parse(operation)
if matrix_operation is not None:
    print("Parsed operation:", matrix_operation.pretty())
else:
    print("Error: Parsing failed")