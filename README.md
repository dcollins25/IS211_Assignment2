# DAN COLLINS - IS211_Assignment2

	- git version 2.30.1.windows.1

	- Python 3.6.5 :: Anaconda, Inc.

# Repo forked from https://github.com/cubanquant/IS211_Assignment2 

# Cloned from https://github.com/dcollins25/IS211_Assignment2

# Professor, 

If you can, please run this program from a Windows command-line. It creates files in the directory it is run in (but not sure if it would work in unix/linux). I imported an additional module [OS] to do this.

Also, I ran the script from Windows and captured the results to the Assignment2-Results.docx Word file. It shows the following:
	- It shows what happens if you don't supply a URL
	- It shows what happens if you don't provide a URL with good data.
	- It shows what happens if you put in something <= 0 (closes the program)
	- It shows what happens if you put in a good ID # (prints out “Person with ID # is <name> with a birthday of<date>”) - no time
	- iT shows what happens if you put in a bad ID # - like 999. (prints an error and logs a message to 'errors.log')

# Part V Putting it all Together
We now need to piece all these functions together. Lets write a main() function that is called when our script runs.

1. First, your program should use the argparse module to allow the user to send a url parameter to the script. This parameter is a string and # is required by the program. If no url is given, the program should exit.

>>> I WAS ABLE TO DO THIS. YOU CAN SEE THIS IN THE FILE AND IF YOU DO NOT PROVIDE A URL A STANDARD MESSAGE WILL SAY IT IS REQUIRED.

2. Then we need to call the downloadData() function and save the results to a variable. Lets call this
variable csvData. The URL to pass to downloadData() is the URL given as a parameter to the script via argparse. Also, we need to also ensure # that if any exception is thrown by this function, that we catch it, print out an appropriate error message, and exit the program.
	
>>> I WAS ABLE TO DO BOTH OF THESE. I CAN DOWNLOAD THE DATA, AND IF YOU PUT IN SOMETHING LIKE http://www.google.com, IT WILL THROW AN ERROR AND LOG IT TO 'errors.log' AS SPECIFIED IN AN 'assignment2' LOGGER.

3. We need to set up a logger with the name ‘assignment2’, which should be configured to write to a single file called “errors.log”. This can # be done in a separate function, or done in the main program.

>>> I WAS ABLE TO DO THIS, AND IT IS DONE VIA A LOGGER CALLED 'assignment2' AND LOGS TO 'errors.log'.

4. Next, we need to take csvData and pass it to the processData() function. The result of this call should be saved into a variable called # personData. Remember, this is a dictionary that maps IDs to tuples.

>>> THIS IS THE ONLY PART THAT I WAS NOT ABLE TO DO. I WAS ABLE TO USE THE DATETIME MODULE TO PUT IT INTO THAT FORMAT, BUT I WAS NOT ABLE TO PUT THE DATA INTO A DICTIONARY. IT CREATED 101 DICTIONARIES INSTEAD OF 1 BIG ONE. I LEFT THE CODE IN THERE SO YOU COULD SEE THE MISTAKE.

>>> GOOD NEWS, I SOLVED AROUND IT! I INTRODUCED A NEW MODULE AND SENT THE DATA TO A TEXT FILE. LATER, I READ IN THAT TEXT FILE AND SEARCH IT FOR THE PERSON, BIRTHDATE BASED ON THE USERS <STDIN> WITH ID #. I SPLIT A BUNCH OF TIMES AND MASSAGE THE OUTPUT TO GET SOMETHING CLOSE TO WHAT YOU REQUESTED.
	- ALSO, IF YOU PUT IN THE WRONG ID # (like 999) IT WILL PRINT AN ERROR MESSAGE AND LOG IT TO 'errors.log'

