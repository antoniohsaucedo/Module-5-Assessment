log_file = open("um-server-01.txt") # creates an active instance of a log file, open this file um-server-01.txt


def sales_reports(log_file): # In Python a function is defined using the def keyword
    for line in log_file: # Loop over each line of the log_file
        line = line.rstrip() # We use the rstrip() method which returns a copy of the string and remove any white spaces at the end of the string. 
        day = line[0:3] # We access an array element by referring to the index number and save it to day
        if day == "Mon": # Only print orders that start with “Mon”
            print(line) # Only print Monday orders


sales_reports(log_file) # We call the funtion sales_reports and passed in argument (log_file)