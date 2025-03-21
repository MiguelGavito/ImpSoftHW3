import csv
# Miguel Angel Gavito Gonzalez
# A00839096
class DFA:
  # definition of the important information for a Determinist Finite Automaton (DFA)
  def __init__(self, states, alphabet, transition, initial_state, final_states):
    self.states = states  # set of states
    self.alphabet = alphabet  #t   he alphhabet
    self.transition = transition #  Delta transtion
    self.initial_state = initial_state #  initial state q0
    self.final_states = final_states #  final state 

  def process_string(self, w): #self = DFA transition table, w = process word
    current_state = self.initial_state

    # check all the symbols in the word w
    for symbol in w:
      # check if the symbol is not in the alphabet
      if symbol not in self.alphabet:
        raise ValueError(f"Symbol '{symbol}' do not belong to the alphabet")
      
      # check if the current state is not in the transition
      # or if the symbol is not in the transition of the current state
      if current_state not in self.transition or symbol not in self.transition[current_state]:
        return False
      
      # if there is no problem
      # it update the current state
      current_state = self.transition[current_state][symbol]

    # Return true if the current state is in  the final states set
    return current_state in self.final_states
  
  # function in charge of transforms the csv file into a transitions table compatible with DFA
  def dfa_read(csv_path):
    # we initializad all the value we are extract from the csv
    transition_table = {}
    alphabet = set()
    states = set()
    initial_state = None
    final_states = set()

    # We open the csv_path as a csvfile
    # Used newfile='' to avoid surprise error for the line jumps
    # 'with' is used to close the file at the end
    with open(csv_path, newline='') as csvfile: 
      reader = csv.reader(csvfile) # create the csv reader
      # cut the first and last value in the list to get rid of the extra space
      # at start
      headers = next(reader)[1:] 

      # We add the alphabet represented as headers
      for symbol in headers:
        # Check if the symbols is not empty
        if symbol != "":
          alphabet.add(symbol)


      for row in reader:
        # identify the current state of the row (first value in the row)
        state = row[0]
        # create our dict for the transitions
        transitions = {}

        # if the state starts with f, its added to final states set
        if row[0][0] == "f":
          final_states.add(state)

        # If there is no initial state, the first state is added as the new.
        if not initial_state:
          initial_state = state

        # loop into the row to get all the transitions
        for i in range(len(headers)):
          symbol = headers[i]     # input to transite
          target_state = row[i+1] # destination state
          if target_state != '':  # targe check
            # we add the transition into the transitions set
            transitions[symbol] = target_state

        # at the end of each for loop, we add the transitions to the transitions table
        transition_table[state] = transitions

    return DFA(states, alphabet, transition_table,initial_state,final_states)
          





