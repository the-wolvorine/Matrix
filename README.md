# Matrix Operations Parser
This repository contains a matrix operations parser that can parse basic matrix operations.

## Requirements
- Python 3.6+
- lark-parser 0.12.0+

## How to run
To use the matrix operations parser, run the matrix_parser.py file and enter a matrix operation when prompted. The parser will parse the operation and print the parsed output.

## Example
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
## Supported Operations To Execute
The grammar supports the following matrix operations:
- addition: `matrix add matrix`
- subtraction: `matrix subtract matrix`
- multiplication: `matrix multiply matrix`
- transpose: `matrix transpose matrix`
- largest value: `matrix largest matrix`
- smallest value: `matrix smallest matrix`
- row sum: `matrix rowsum matrix`
- column sum: `matrix columnsum matrix`
- row multiplication: `matrix rowmultiply matrix`

## Conclusion
This code defines a grammar for parsing matrix operations with support for basic matrix operations like addition, subtraction, multiplication, transpose, largest or smallest value in a matrix, row or column sum and row multiplications etc. 
With this code, you can perform various matrix operations using the defined grammar. 

The test_matrix_operations.txt file contains the matrix operations that can be used to test the parser.
