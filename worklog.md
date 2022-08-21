# worklog

## PROBLEMS
## QUESTIONS
### What is @property decorator ?
@property allows a class method to be accessed like an attribute. It's the
equivalent of a getter. Then, we can add @obj.setter and @obj.deleter.

An example :

```python
class User:
    def __init__(self):
        self.__name__ = ""
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
        
    @name.deleter
    def name(self):
        del self.__name
        
user = User()

user.name = "Alice"

print(user.name) # Alice

del user.name

print(user.name) # Error
```

### How to use pdb (debugger) ?

We can insert `breakpoint()`, which will `import pdb` and insert
`pdf.set_trace()`.

Or we can launch the script like this : ```python -m pdf app.py arg1 arg2```
