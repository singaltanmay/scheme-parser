# Parser for the Schemeling Interpreter
#
#
#

import logging

logging.basicConfig(filename='schemeling.log', level=logging.DEBUG)

def tokenize(string):
    """
    Returns a list containing each individual character of a string.
    
    string --> a string of Lisp code
    """
    string = string.replace("(", " ( ")
    string = string.replace(")", " ) ")
    string = string.split()
    
    return string

def parenthesize(tokens, array=[]):
    """
    Returns a nested array where each '(' starts a new dict and each
    character is labeled by type and value
    
    tokens --> an array of characters from tokenize()
    """
    current_token = tokens.pop(0)

    if current_token == '(':
        array.append(parenthesize(tokens, []))
    elif current_token == ')':
        return array
    
    else:
        array.append(categorize(current_token))
        parenthesize(tokens, array)
        logging.debug("Tokens: %s\nArray> %s\nCurrent Token: %s\n----" % (tokens, array, current_token))
        
        
    return array
    
    
    
def categorize(token):
    """
    Returns a dict with two entries, 'type' and 'indentifier' which describe the input token
    
    token --> a single, non-parenthesis, token from the array passed to parenthesize()
    """
    identifiers_list = ['lambda', '+', '-', '/', '*']
    
    if token in identifiers_list:
        return {'type':'identifier', 'value':token}
    
    else:
        return {'type':'literal', 'value':token}
    
def parse(lisp_string):
    """
    Just a wrapper for tokenize() and subsequent parenthesize()
    """
    return parenthesize(tokenize(lisp_string))
    
if __name__ == "__main__":
    print parenthesize(tokenize("()"))
