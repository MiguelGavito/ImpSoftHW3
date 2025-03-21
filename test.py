from dfa import DFA
import string
import random
import re

#functions to generalte random testcases
def generate_valid_integer():
  return str(random.randint(-2**32, 2**32))

def generate_valid_float():
  integer_part = random.randint(-2**32, 2**32)
  fractional_part = random.randint(1, 9999)
  return f"{integer_part}.{fractional_part}"

def generate_valid_scientific_notation():
  base = random.randint(-2**32, 2**32)
  exponent = random.randint(1, 10)
  return f"{base}E{exponent}"

def generate_invalid_string():
  # Generate a random string with letters (invalid for a number)
  length = random.randint(3, 8)
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


# Test for the hm2 with the process_string function
def dfa_test_hm2():
  #test 1
  #the word end with 'a'
  states = {'q0','q1'}
  alphabet = {'a','b'}
  transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q0'}
  }
  initial_state = 'q0'
  final_states = {'q1'}

  dfa1 = DFA(states, alphabet, transition, initial_state, final_states)
  print("\nTest 1 end with 'a'")
  print(dfa1.process_string("a")) #true
  print(dfa1.process_string("ab")) #false
  print(dfa1.process_string("bab")) #false
  print(dfa1.process_string("aaa")) #true
  print(dfa1.process_string("abab")) #false

  states = {'q0','q1'}
  alphabet = {'a','b'}
  transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q0', 'b': 'q1'}
  }
  initial_state = 'q0'
  final_states = {'q0'}

  dfa2 = DFA(states, alphabet, transition, initial_state, final_states)

  print("\nTest 2 have a even number of 'a'")
  print(dfa2.process_string("a")) #false
  print(dfa2.process_string("ab")) #false
  print(dfa2.process_string("bab")) #false
  print(dfa2.process_string("aaa")) #false
  print(dfa2.process_string("abab")) #true

  states = {'q0','q1','q2'}
  alphabet = {'a','b'}
  transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q2', 'b': 'q2'}
  }
  initial_state = 'q0'
  final_states = {'q2'}

  dfa3 = DFA(states, alphabet, transition, initial_state, final_states)

  print("\nTest 3 any word with an 'ab' substring")
  print(dfa3.process_string("a")) #False
  print(dfa3.process_string("ab")) #True
  print(dfa3.process_string("bab")) #True
  print(dfa3.process_string("aaa")) #False
  print(dfa3.process_string("abab")) #True

# Other version of the Test for the HM3
def test_dfa_v2(csv_path):
  #test 
  dfa = DFA.dfa_read(csv_path)

  # Casos de prueba (puedes agregar más pruebas aquí)
  test_cases = [
    ("10.5E+3", True),    # Cadena válida
    ("1234", True),       # Cadena válida
    ("abc", False),       # Cadena inválida
    ("0.1", True),        # Cadena válida
    ("1E+10", True),      # Cadena válida
    ("-100", True),       # Cadena válida
    ("-100.5E-2", True),  # Cadena válida
    ("0.0", True),        # Cadena válida
    ("+0", True)          # Cadena válida
  ]
  # Probar todas las cadenas
  for string, expected in test_cases:
    try:
      result = dfa.process_string(string)
      assert result == expected, f"Failed for '{string}': expected {expected}, got {result}"
      print(f"Test passed for: '{string}'")
    except ValueError as e:
      print(f"ValueError: {e} for '{string}'")
    except AssertionError as e:
      print(e)



# hm3 test with the path to the csv and the numbers of test
def dfa_test_hm3(csv_path, n):
    
    # Read the CSV, it needs to be in the same folder
    dfa = DFA.dfa_read(csv_path)

    # Generates intergers, floats and scientist notation to test
    valid_strings = []
    for _ in range(n):
      valid_strings.append(random.choice([
         generate_valid_float(),
         generate_valid_integer(),
         generate_valid_scientific_notation()
      ]))
      
    #invalid string
    invalid_strings = [generate_invalid_string() for _ in range(n)]

    # Connect all the test cases
    test_cases = [(valid_string, True) for valid_string in valid_strings] + \
                 [(invalid_string, False) for invalid_string in invalid_strings]

    failing_inputs = []

    # Try all the string of words
    for string, expected in test_cases:
        try:
            result = dfa.process_string(string)
            assert result == expected, f"Failed for '{string}': expected {expected}, got {result}"
            print(f"Test passed for: '{string}'")
        except ValueError as e:
            print(f"ValueError: {e} for '{string}'")
        except AssertionError as e:
            print(e)
            failing_inputs.append(string)

    # Return in failures cases
    if failing_inputs:
        print("\nFalling inputs:", failing_inputs)
        return False
    else:
        return True

def prof_test_hm3(csv_path):
  A = DFA.dfa_read(csv_path)
  w = '0-247'

  R = A.process_string(w)

  print(f"\n{w} is {R}\n")

  W = ['0','01','.','.0','1.0e1']
  results = [True, False, False, True, True]
  errors = []
  for i in range(len(W)):
    if not A.process_string(W[i]) == results[i]:
      errors.append(W[i])
    print(f"{W[i]} is {A.process_string(W[i])}\n")
  if (len(errors) == 0):
    print("No hubo errores\n")
  else:
    print(errors)


if __name__ == '__main__':
  # other test to check certain cases
  #test_dfa_v2("NumericRecognizer.csv")
  
  n = 5  # number of tests.
  csv_path = "NumericRecognizer.csv" #path of the csv

  print(f"\nFirst tests with {n} valid strings and {n} invalid strings\n")
  if dfa_test_hm3(csv_path, n):
      print("All tests passed!")
  else:
      print("Some tests failed.")
  
  print("\nSecond test: Profesor examples\n")

  prof_test_hm3(csv_path)
  