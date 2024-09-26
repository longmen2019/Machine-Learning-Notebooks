## NumPy: Creating and Manipulating Arrays

This README explains how to create and manipulate NumPy arrays, a fundamental data structure in Python for scientific computing.

### What is NumPy?

NumPy (Numerical Python) is a Python library that provides powerful tools for working with arrays. NumPy arrays are efficient and offer significant performance advantages over traditional Python lists when dealing with numerical data. 

### Key Features of NumPy Arrays

* **Homogeneous Data Type:** All elements in a NumPy array must have the same data type (e.g., integers, floats, strings). This allows for optimized operations.
* **Multidimensional:** NumPy arrays can have multiple dimensions, enabling you to represent complex data structures like matrices and images.

### Creating NumPy Arrays

There are several ways to create NumPy arrays:

1. **From a Python List:**

   ```python
   import numpy as np

   vector = np.array([1, 2, 3, 4])
   print(vector)
   ```

   This code creates a one-dimensional (1D) array named `vector` from a Python list.

2. **Zeros and Ones:**

   * `np.zeros(shape)`: Creates an array filled with zeros of the specified `shape` (tuple representing dimensions).
   * `np.ones(shape)`: Creates an array filled with ones of the specified `shape`.

   ```python
   v = np.zeros((2, 3))  # 2x3 array of zeros
   print(v)
   ```

3. **Empty Arrays:**

   * `np.empty(shape)`: Creates an uninitialized array of the specified `shape`. The values in an empty array are arbitrary and may contain garbage data.

4. **arange:** Similar to Python's `range` function, but returns a NumPy array.

   ```python
   a = np.arange(15)
   print(a)  # Prints [0 1 2 3 ...]
   ```

5. **`zeros_like` and `ones_like`:**

   These functions create arrays with the same shape and data type as an existing array, but initialized with zeros or ones, respectively.

6. **`empty_like`:**

   Creates an empty array with the same shape and data type as an existing array.

### Accessing and Modifying Array Elements

You can access and modify elements in a NumPy array using indexing and slicing, similar to Python lists. However, unlike lists, modifying a slice of a NumPy array modifies the original array itself.

**Slicing:**

```python
a = np.arange(20)
print(a[10:15])  # Prints elements from index 10 (inclusive) to 14 (exclusive)

# To avoid modifying the original array, use `.copy()`
b = a[10:15].copy()
b[:] = 5  # Modifies the copy, not the original array
```

### Data Type Conversion

Use `astype` to convert the data type of a NumPy array:

```python
a = np.array([1, 2, 3, 4.5, 6.7])
print(a.dtype)  # Output: float64

b = a.astype(int)  # Converts to integer, truncating decimals
print(b.dtype)  # Output: int32
```

### Vectorization and Operations

NumPy excels at performing element-wise operations on arrays. This is often more efficient than using Python loops.

* **Operations on Arrays with the Same Shape:**

   ```python
   a = np.array([[1, 2, 3], [4, 5, 6]])
   b = np.array([[4, 5, 6], [1, 2, 3]])

   # Element-wise addition
   c = a + b
   print(c)

   # Element-wise multiplication
   c = a * b
   print(c)
   ```

* **Operations with Scalars:**

   ```python
   a = 3
   b = np.array([[1, 2, 3], [4, 5, 6]])

   # Element-wise addition of scalar and array
   c = a + b
   print(c)
   ```

### Boolean Indexing

Use boolean arrays to filter or select elements based on conditions:

```python
a = np.array(["Mayur", "is", "an", "awesome", "coder"])
print(a == "Mayur")  # Boolean array indicating elements equal to "Mayur"

# Selecting elements where the value is not