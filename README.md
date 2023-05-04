# Matrix Operations Parser
This repository contains a simple matrix operations parser that can parse basic matrix operations using pthon.

## Requirements
- Python 3.6+
- lark-parser 0.12.0+

## How to run
To use the matrix operations parser, run the matrix_parser.py file and enter a matrix operation when prompted. The parser will parse the operation and print the parsed output.
    
## Supported Operations To Execute
The grammar supports the following matrix operations:
- assignment: `matrix matrix_name is matrix_definition`
- addition: `matrix_addition matrix_name to matrix_name`
- subtraction: `matrix_subtraction matrix_name from matrix_name`
- multiplication: `matrix_multiplication matrix_name with matrix_name`
- transpose: `matrix_transpose matrix_name`
- largest value: `matrix_largest_value matrix_name`
- smallest value: `matrix_smallest_value matrix_name`
- row sum: `matrix_row_sum matrix_name row_number`
- column sum: `matrix_column_sum matrix_name column_number`
- row multiplication: `matrix_row_multiplication matrix_name row_number literal_value`

## Example
Here is the example showing how to assign a matrix to a variable(matrix_name).
```
python matrix_parser.py
Enter a input: matrix A is [[1, 2], [3, 4]];
Parsed operation: start
statement
  matrix_assignment
    matrix_name       A
    matrix_definition
      row
        literal_value 1
        literal_value 2
      row
        literal_value 3
        literal_value 4
    end_statement
```  

## Conclusion
This code defines a grammar for parsing matrix operations with support for basic matrix operations like addition, subtraction, multiplication, transpose, largest or smallest value in a matrix, row or column sum and row multiplications etc. 
With this code, you can perform various matrix operations using the defined grammar. 

The test_matrix_operations.txt file contains the matrix operations that can be used to test the parser.
