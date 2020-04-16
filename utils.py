import numpy as np
from datetime import datetime
from pickle import dump, load, HIGHEST_PROTOCOL

def printnow(to_print):
    '''
    Flush output buffer and print to standard out. This will cause print to happen immediately. 
    
    Parameters
    ----------
    to_print : formatted string
    
    Example
    -------
    printnow('The value of r is %d'%r)
        
    '''
    print(to_print, flush=True)
    
    
def unsqueeze(val):
    '''
    Change the shape of single dimensional numpy array from (N,) to (N,1) 
    
    Parameters
    ----------
    val : numpy array with dimension (N,)
    
    '''
    return val.reshape(len(val), -1)  

def now(formatDate='%Y-%m-%d'):
    '''
    Returns the datime and time when executed in specified format
    
    Parameters
    ----------
    formatDate : string format for date time
    
    Example
    -------
    now()
    > '2018-06-01'

    now(formatDate='%Y-%m-%d %H:%M:%S')  
    > '2018-06-01 13:11:31'

    '''
    return datetime.now().strftime(formatDate)


def read_from_pickle(path):
    '''
    Read pickle file. 
    
    Returns a list of all variables stored in file.
    
    Parameters
    ----------
    path : path and filename

    '''

    objects = []
    with open(path, 'rb') as file:
        while True:
            try:
                objects.append(load(file))
            except EOFError:
                break
    return objects           


def save_to_pickle(path, data):
    '''
    Save variables to pickle file. Put multiple variables in a list. 
    
    Parameters
    ----------
    path : directory structure and filename to save
    data : list of variables

    Example
    -------
    save_to_picke('//nas2.valencell.com/Shared/Data/example.pkl', [variable_1, dataframe_0, dictionary_4])
    '''

    with open(path, 'wb') as handle:
        dump(data, handle, protocol=HIGHEST_PROTOCOL)


def in_list(first, second):
    '''
    Find all the elements of first list that matches any element in second list.
    
    Returns a list of booleans the same size as first list
    
    Parameters
    ----------
    path : directory structure and filename to save
    data : list of variables

    Example
    -------
    in_list(['a','b','c','d', 'c'], ['b', 'c'])    
    > [False, True, True, False, True]
    '''
    return list(np.compress(first, np.in1d(first,second)))


def has_digit(inputString):
    '''
    Boolean check if the string contains a digit in any character.
    
    Returns a boolean
    
    Parameters
    ----------
    inputString : string to interrogate
    '''
    return any(char.isdigit() for char in str(inputString))

# figure this out
np_has_digit = np.vectorize(has_digit, otypes=[np.bool])


def make_columns_unique(df_columns):
    seen = set()

    for item in df_columns:
        fudge = 1
        newitem = item

        while newitem in seen:
            fudge += 1
            newitem = "{}_{}".format(item, fudge)

        yield newitem
        seen.add(newitem)
#list(make_columns_unique(m.columns))        

def is_str_in_df(df, string):
    rows, cols = df.shape
    find = np.zeros([rows, cols])
    for col in np.arange(cols):
        find[:,col] = df.iloc[:,col].astype(str).str.lower().str.contains(string).values 
    # return boolean and indices    
    return(np.any(find), np.nonzero(find))    

def is_array_of_type(array, varType):
    '''
    Checks each member of array againts given varialbe type.
    
    Returns numpy boolean array.
    
    Parameters
    ----------
    array : numpy array to interrogate
    varType : variable type
    
    Example
    -------
    is_array_of_type(temp, np.int32)
    '''
    return np.array([isinstance(val, varType) for val in array])

def has_three_consecutive_int(val):
    val = str(val)
    isInt = [char.isdigit() for char in val]
    tupleOfThree = (list(zip(isInt,isInt[1:],isInt[2:])))
    return np.array(any([all(val) for val in tupleOfThree]))

def three_int_in_a_row(array):
    return [has_three_consecutive_int(val) for val in array]

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
    
