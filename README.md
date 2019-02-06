# Directory-Print
This script will print all files in a given directory.

I wrote this script to print hundreds of PDFs in a directory. 
When selecting all the PDFs in the directory and printing at once, they would not print in order which was a requirement.
The old solution was to right click each file one by one and select print. 
This solution iterates over every file in a folder and prints it in the order they are listed. 
Ten seconds is given between each print to ensure the data for each file reaches the printer before beginning the next print job.
Once every file is printed in the folder the script terminates.
