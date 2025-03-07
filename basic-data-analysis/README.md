# Task: Calculate Mean, Variance, Standard Deviation, Max, Min, and Sum of a 3x3 Matrix

Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3x3 matrix.

## Input
The input of the function should be a list containing 9 digits.

## Function Behavior
The function should convert the list into a 3x3 Numpy array, and then return a dictionary containing the following values:

- **mean**
- **variance**
- **standard deviation**
- **max**
- **min**
- **sum**

These values should be calculated along both axes (rows and columns) and for the flattened matrix.

## Output Format
The returned dictionary should follow this format:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

---
**mean_var_std.py** file has the answers of this exercise written by me. 
