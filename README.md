# Break-Python
Adds a ```br()``` function to Python (Similar to ```&lt;br>``` in HTML (Inserts a newline (```\n```)))

# Usage
## ```br()```
```python
print("Hello World!")
br(2)
print("Goodbye World!")

# Output
>>> Hello World!
>>> 
>>> 
>>> Goodbye World!
```

## ```pbr()```
```python
from Break import *

print("Hello World!")
pbr(2)
print("Goodbye World!")

# Output:
>>> Hello World!
>>> 
>>> 
>>> Goodbye World!

```

## ```rbr()```
```python
from Break import *

String = f"Hello World\n{rbr(2)}\nGoodbye World"
print(String)

# Output:
>>> Hello World  
>>> 
>>> 
>>> Goodbye World
```
