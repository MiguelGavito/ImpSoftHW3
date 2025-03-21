Miguel Ángel Gavito González
A00839096

CSV structure:

q0  # Initial State
q1  # Sign
f2  # Interger Section
f3  # Zero Start
q4  # Decimal Dot
f5  # Fractional Section
q6  # Exponent Sign
q7  # Exponent Number Section
f8  # Final State


The function of read csv in a simplify way, read cell by cell the csv, skip any empty space and in the first row, if it
find any value in, then it adds it to the alphabet set.

The Final States are marked with a 'f' at the start.


For the test cases there is the function dfa_test_hm3(csv_path, n)
csv path is self explanatory.
n is the numbers of valid and invalid test generate 