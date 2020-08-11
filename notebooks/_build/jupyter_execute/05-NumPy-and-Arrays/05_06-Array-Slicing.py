## Array Slicing

Multiple values stored within an array can be accessed simultaneously with array _slicing_. To pull out a section or slice of an array, the colon operator ```:``` is used when calling the index. The general form is:

```python
<slice> = <array>[start:stop]
```

Where ```<slice>``` is the slice or section of the array object ```<array>```. The index of the slice is specified in ```[start:stop]```. Remember Python counting starts at ```0``` and ends at ```n-1```. The index ```[0:2]``` pulls the first two values out of an array. The index ```[1:3]``` pulls the second and third values out of an array.

An example of slicing the first two elements out of an array is below.

import numpy as np

a = np.array([2, 4, 6])
b = a[0:2]
print(b)

On either sides of the colon, a blank stands for "default". 

 * ```[:2]``` corresponds to ```[start=default:stop=2]``` 
 * ```[1:]``` corresponds to ```[start=1:stop=default]```
 
Therefore, the slicing operation ```[:2]``` pulls out the first and second values in an array. The slicing operation ```[1:]``` pull out the second through the last values in an array.
 
 The example below illustrates the default ```stop``` value is the last value in the array.

import numpy as np

a = np.array([2, 4, 6, 8])
print(a)
b = a[1:]
print(b)

The next examples shows the default ```start``` value is the first value in the array.

import numpy as np

a = np.array([2, 4, 6, 8])
print(a)
b = a[:3]
print(b)

The following indexing operations output the same array.

import numpy as np

a = np.array([2, 4, 6, 8])
b = a[0:4]
print(b)
c = a[:4]
print(c)
d = a[0:]
print(d)
e = a[:]
print(e)

### Slicing 2D Arrays

2D NumPy arrays can be sliced with the general form:

```Python
<slice> = <array>[start_row:end_row, start_col:end_col]
```

The code section below creates a two row by four column array and indexes out the first two rows and the first three columns.

import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
print(a)
b = a[0:2, 0:3]
print(b)

The code section below slices out the first two rows and all columns from array ```a```.

import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
b = a[:2, :]  #[first two rows, all columns]
print(b)

Again, a blank represents defaults the first index or the last index. The colon operator all by itself also represents "all" (default start: default stop).

import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
b = a[:,:]  #[all rows, all columns]
print(b)

