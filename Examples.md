## 1. Input matrix
```
python matrix.py
Enter a input: matrix A is [[1,2],[3,4]];
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
## 2. Transpose Matrix
```
Enter a input: matrix_transpose A;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_transpose
        matrix_name     A
        end_statement
```

## 3. Matrix Addition
```
Enter a input: matrix B is [[5, 6], [7, 8]];
Enter a input: matrix_addition A to B;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_addition
        matrix_name     A
        matrix_name     B
        end_statement
```

## 4. Smallest Value In a Matrix
```
Enter a input: matrix_smallest_value matrix_result;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_smallest_value
        matrix_name     matrix_result
        end_statement
```

## 5. Matrix Multiplication
```
Enter a input: matrix_row_multiplication A 1 2;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_row_multiplication
        matrix_name     A
        row_number      1
        literal_value   2
        end_statement
```

## 6. Matrix Column Sum
```
Enter a input: matrix_column_sum A 2;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_column_sum
        matrix_name     A
        column_number   2
        end_statement
```
## 7. Multiplying A Matrix by its Transpose
```
Enter a input: matrix_multiplication A with matrix_result;
Parsed operation: start
  statement
    matrix_operation
      matrix_operation_multiplication
        matrix_name     A
        matrix_name     matrix_result
        end_statement
```