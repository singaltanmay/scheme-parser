# Tester module
#
#

import unittest
import parser

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.input_string = "(+ 3 (+ 4 5))"
        self.tokenized = ['(', '+', '3', '(', '+', '4', '5', ')', ')']
        self.parenthesized = [{'type': 'identifier', 'value': '+'}, 
                              {'type': 'literal', 'value': '3'}, [ 
                              {'type': 'identifier', 'value': '+'}, 
                              {'type': 'literal', 'value': '4'},
                              {'type': 'literal', 'value': '5'}]]
                              
        self.input_token_literal = "3" 
        self.categorized_literal = {'type': 'literal', 'value': '3'}
        
        self.input_token_indentifier = "lambda"
        self.categorized_identifier = {'type': 'identifier', 'value': "lambda"}
        
        
    def test_simple_tokenize(self):
        self.assertEqual(self.tokenized, parser.tokenize(self.input_string))

    def test_simple_parenthesize(self):
        self.assertEqual(self.parenthesize, parser.parenthesized(parser.tokenize(self.input_string)))
    
    def test_literal_categorize(self):
        self.assertEquals(self.categorized_literal, parser.categorize(self.input_token_literal))

    def test_identifier_categorize(self):
        self.assertEquals(self.categorized_identifier, parser.categorize(self.input_token_identifier))
        
    def test_parse(self):
        self.assertEquals(self.parenthesized, parser.parse(self.input_string))
        
if __name__ == '__main__':
    unittest.main()

