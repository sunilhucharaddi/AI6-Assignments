```
This python file is a good starting point.
Activation Functions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  return((numpy.exp(x)-numpy.exp(-x))/(numpy.exp(x)+numpy.exp(-x)))
  # enter code below
  
def relu(x):
  return max(0,x)
  # entr code below
  
