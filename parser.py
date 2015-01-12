# Parser for the lis.py Interpreter
#
#
#

def tokenize(string):
    """
    Returns a list containing each individual character of a string.
    
    string --> a string of Lisp code
    """
    pass

def parenthesize(tokens):
    """
    Returns a nested array where each '(' starts a new dict and each
    character is labeled by type and value
    
    tokens --> an array of characters from tokenize()
    """
    #Use a stack to go through the input array and make the output array of lists and dicts
    pass
    
def categorize(token):
    """
    Returns a dict with two entries, 'type' and 'indentifier' which describe the input token
    
    token --> a single, non-parenthesis, token from the array passed to parenthesize()
    """
    pass
    
def parse(lisp_string):
    """
    Just a wrapper for tokenize() and subsequent parenthesize()
    """
    return parenthesize(tokenize(lisp_string))
    
