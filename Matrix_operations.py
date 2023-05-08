from lark import Lark, Transformer, v_args

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

# Define a transformer to process the parsed data
@v_args(inline=True)
class MatrixTransformer(Transformer):
    matrices = {}

    def matrix_operation_addition(self, args):
        matrix1_name = args[0]
        matrix2_name = args[1]
        result = [[sum(x) for x in zip(row1, row2)] for row1, row2 in zip(self.matrices[matrix1_name], self.matrices[matrix2_name])]
        return result

    def matrix_operation_subtraction(self, args):
        matrix1_name = args[0]
        matrix2_name = args[1]
        result = [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(self.matrices[matrix1_name], self.matrices[matrix2_name])]
        return result

    def matrix_operation_multiplication(self, args):
        matrix1_name = args[0]
        matrix2_name = args[1]
        matrix2_transposed = list(map(list, zip(*self.matrices[matrix2_name])))
        result = [[sum(x * y for x, y in zip(row1, row2)) for row2 in matrix2_transposed] for row1 in self.matrices[matrix1_name]]
        return result

    def matrix_operation_transpose(self, args):
        matrix_name = args[0]
        matrix_transposed = list(map(list, zip(*self.matrices[matrix_name])))
        return matrix_transposed

    def matrix_operation_largest_value(self, args):
        matrix_name = args[0]
        matrix_values = [x for row in self.matrices[matrix_name] for x in row]
        return max(matrix_values)

    def matrix_operation_smallest_value(self, args):
        matrix_name = args[0]
        matrix_values = [x for row in self.matrices[matrix_name] for x in row]
        return min(matrix_values)

    def matrix_operation_row_sum(self, args):
        matrix_name = args[0]
        row_number = args[1]
        row_sum = sum(self.matrices[matrix_name][row_number])
        return row_sum

    def matrix_operation_column_sum(self, args):
        matrix_name = args[0]
        column_number = args[1]
        column_sum = sum(row[column_number] for row in self.matrices[matrix_name])
        return column_sum

    def matrix_operation_row_multiplication(self, args):
        matrix_name = args[0]
        row_number = args[1]
        literal_value = args[2]
        if literal_value == 0:
            raise ValueError("Cannot multiply row by zero.")
        result = [x * literal_value if i == row_number else x for i, x in enumerate(self.matrices[matrix_name][row_number])]
        return result

    def matrix_assignment(self, args):
        matrix_name = args[0]
        matrix_definition = args[1]
        self.matrices[matrix_name] = matrix_definition
        return None

    def matrix_definition(self, args):
        rows = args
        return rows

    def row(self, args):
        row = args[0]
        return row

    def literal_value(self, args):
        return int(args[0])

    def matrix_name(self, args):
        return str(args[0])

    def row_number(self, args):
        return int(args[0])

    def column_number(self, args):
        return int(args[0])

# Create a parser using the grammar and transformer
matrix_parser = Lark(matrix_grammar, parser='lalr', transformer=MatrixTransformer())

# Get input from the user and parse it
while True:
    try:
        text = input('> ')
        result = matrix_parser.parse(text)
        if isinstance(result, list):
            # The result is a matrix, so print it out
            print("[")
            for row in result:
                print(" [", end="")
                for value in row:
                    print(value, end=", ")
                print("]")
            print("]")
        else:
            # The result is not a matrix, so just print it out
            print(result)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
