# No Imports
# Read 'mbox-short.txt'
# Find time posted
# Sort by hour
# Must use a Tuple

# ---- Tuples ---- #
# Tuples are unchangable after creation...
# You can add Tuples to Tuples
# Cannot delete items in a Tuple

'''
e = 'Gouda'                                                                                 # Variables work in Tuple
cheb = 'Milk'

cheese = ('Brie', 'Parmesan', e)                                                            

cheese = cheese + ('Cheddar',)                                                             # Tuple doesn't have to be a variable to add it

cheese = cheese + (f'{cheb}',)                                                             # Formatting works with adding tuples

print(cheese)
'''

# ---------------- #

print('Scanning mbox-short.txt...')
print('Done!')
print('# ----- #')

emailstr = ''
emailtuple = ()
emaildict = {}
num = 0

# epath = 'D:/mbox-short.txt'                                                               # USB path / Home path
epath = 'I:/Testing/mbox-short.txt'                                                         # School path
emailscript = open(epath, 'r')                                                              # Opens path to mbox-short.txt for reading
emailscript = emailscript.read()                                                            # Reads lines

letterindex = emailscript.find("From")

# ----------------------------------------------------------------------------- # Main Loop 
while letterindex < len(emailscript):
    letterindex = emailscript.find("From", letterindex)                                     # Finds the spots of the word 'From' in the string
    if letterindex == -1:                                                                   # Exception for when the program reaches the end of the string to prevent errors
        break
    letterindex += 1                                                                        # Increments the index place so the program doesn't get stuck
    if (emailscript[letterindex + 3] == ' '):                                               # Checks forward a few characters after the 'From' to check for a space (Colon Clause)
        letterindex = letterindex + 4                                                       # Jumps forward a few characters to the real start of the line
        colonclause = False                                                                 # Sets up for email while loop
        
        while colonclause == False:                                                         # Parses emails character by character until there's a space
            try:                                                                            
                 int(emailscript[letterindex])                                              # Attempts to convert the letter in the index position to an integer
                 if emailscript[letterindex + 2] == ':':                                    # Checks if there is a colon two positions away from the index position
                     tens = emailscript[letterindex]                                        # Gets the tens position of the number
                     ones = emailscript[letterindex + 1]                                    # Gets the ones position of the number
                     num = (f'{tens}{ones}')                                                # Joining the tens place and ones place together manually with formatting

                     if num in emailtuple:                                                  # Checks if the number is already in the tuple
                         emailtuple = emailtuple + (num,)                                   # Adds tuple (num,) to already existing tuple emailtuple
                         if num in emaildict:                                               # Checks if the number is already in the dictionary
                             emaildict[num] += 1                                            # Updates the dictionary entry with a value of +1
                             num = ''                                                       # Clears num so that the program doesn't accidentally add them together
                         break                                                              # Breaks loop to continue checking for 'From'
                     else:
                         emailtuple = emailtuple + (num,)                                   
                         if num not in emaildict:
                             emaildict[num] = 1                                             # Adds initial value for new dictionary entries
                             num = ''
                         break
                     break                                                           

                 letterindex += 1                                                           # Runs after the if else statement to keep continuing the program
                  
            except:
                    if emailscript[letterindex] == '\n':                                    # Checks for new line if the program cannot find an integer
                        print('newline')
                        break                                                         
                    letterindex += 1                                                        

print('Hour To Post Ratio:')

for y in sorted(emaildict):                                                                 # Sorting algorithm
    a = str((y, emaildict[y]))                                                              # Format for printing the dict values without messing it up & Converts to string                                                                            # Emaildict is a tuple here for some reason so I have to convert it
    a = a.replace("'", "").replace(")", "").replace("(", "").replace(",", "")               # Removes unnesesary characters
    print(a)

dictvalues = emaildict.values()
maxvalue = max(dictvalues)
maxkey = max(emaildict, key = emaildict.get)
    
print(f'The most active hour on this website is currently {maxkey}, with {maxvalue} posts!')
print('# ----- #')

input('-Press Enter to Exit-')                                                              # Prevents program from closing
