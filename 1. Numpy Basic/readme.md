## NumPy Introduction

This is a README file for a Jupyter Notebook exploring NumPy, a powerful library for numerical computations in Python.

### What is NumPy?

NumPy (Numerical Python) provides efficient arrays and mathematical functions for scientific computing. It excels in tasks involving large datasets compared to standard Python lists.

**Key Feature:** The `ndarray` object, a multidimensional array with a single data type for all elements.

### Getting Started with Arrays

**Importing NumPy:**

```python
import numpy as np
```

**Creating Arrays:**

* From Lists:

```python
vector = np.array([1, 2, 3, 4])

print("vector:", vector)
```

* Examining Array Properties:

  * **Shape:** Number of dimensions (rows and columns)
  * **Dimensions (ndim):** Total number of dimensions
  * **Data type (dtype):** Type of elements in the array (e.g., integer, float)

```python
print("Shape:", vector.shape)
print("Dim:", vector.ndim)
print("Data type:", vector.dtype)
```

**Reshaping Arrays:**

```python
v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
v.shape = (2, 3, 2)  # Reshape into a 2x3x2 array
print(v)
```

### Creating Specialized Arrays

* **`zeros(dim)`:** Creates an array of zeros with specified dimensions (`dim`).

```python
v = np.zeros((2, 3, 3))
print(v)
```

* **`ones(dim)`:** Creates an array filled with ones.

* **`empty(dim)`:** Creates an uninitialized array with specified dimensions. Values are undefined (garbage data).

**Note:** `zeros`, `ones`, and `empty` all take a tuple as the `dim` argument.

### `arange` Function

Similar to Python's `range` function, `arange` generates evenly spaced values within a specific range. The default data type is often `np.float64`.

```python
a = np.arange(15)
print(a)
```

**This notebook explores the basics of NumPy arrays and functions. Further exploration can delve into mathematical operations, linear algebra, and more!** 