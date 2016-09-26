The parseLine function is designed to parse the shadow file, reading and storing
each line (both the user and hashed password) then plugging these values in as
parameters to the passwordCrack function.  Python does this using argparse imported
into the program.  If the proper requirements for parsing are not met, the program
will notify the user and exit, else it will parse the line, so basic error
checking is included.

The passwordCrack function pasrses the password specifically to discover the hash, 
salt and password assuming SHA-512 encryption is used (type 6).  This function uses the built 
in Python function crypt() to check for a match between the two hashes.  
If they do match, the password is cracked.  It uses a dictionary file I called
dictionary.txt.  If the passwords do not match, the user is notified.

The program executes off of the final line of code.  When Python
reads a file, it automatically (if running the source file as the main program)
creates a variable called __name__ and gives it the value __main__.  This line
simply checks to make sure this is the case, then beings the program logic
with the parseLine function (which recursivley calls the passwordCrack function
as described above if proper parameters are found in the shadow file).

To run the program, have open a terminal on a Linux machine.  You will also need a
dictionary file with the name used in the program, dictionary.txt.  Of course, you
need Python installed on the machine as well.  Simply navigate to the directory with
the Python script and tictionary file and type      python PWcrack.py 