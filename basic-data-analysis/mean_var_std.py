import numpy as np

def calculate(list):

    a = np.array(list)
    calculations = {}

    if len(a) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = a.reshape(3, 3)
    
    # Using a dictionary comprehension to calculate all operations and 'getattr' to dynamically call the method for each operation
    operations = ['mean', 'var', 'min', 'max', 'std', 'sum']
    calculations = {op: [getattr(a, op)(axis=0).tolist(), getattr(a, op)(axis=1).tolist(), getattr(a, op)()] for op in operations}

    # Rename
    calculations['standard deviation'] = calculations.pop('std') 
    calculations['variance'] = calculations.pop('var')   


    return calculations

