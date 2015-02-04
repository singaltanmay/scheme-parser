# Parser for the Schemeling Interpreter
#
# Authors: Keyan Pishdadian and David Gomez Urquiza


def tokenize(string):
    """
    Returns a list containing each individual character of a string.

    string --> a string of Lisp code
    """
    string = string.replace("(", " ( ")
    string = string.replace(")", " ) ")
    token_list = string.split()

    return token_list


def parenthesize(tokens, array=[]):
    """
    Returns a nested array where each '(' starts a new dict and each
    character is labeled by type and value

    tokens --> an array of characters from tokenize()
    """
    try:
        current_token = tokens.pop(0)
    except IndexError:
        current_token = None

    if current_token == '(':
        array.append(parenthesize(tokens, []))
    elif current_token == ')':
        return array
    elif current_token is not None:
        array.append(categorize(current_token))
        parenthesize(tokens, array)

    return array


def categorize(token):
    """
    Returns a dict with two entries, 'type' and 'indentifier' which describe
    the input token

    token --> a single, non-parenthesis, token from the array passed to
    parenthesize()
    """
    identifiers_list = ['lambda', '+', '-', '/', '*']

    if token in identifiers_list:
        return {'type': 'identifier', 'value': token}
    else:
        return {'type': 'literal', 'value': token}


def parse(lisp_string):
    """
    Just a wrapper for tokenize() and subsequent parenthesize()
    """
    if lisp_string == '':
        return
    else:
        return parenthesize(tokenize(lisp_string)).pop()


if __name__ == "__main__":
    print parse("((lambda (x) x) 'Lisp'")
