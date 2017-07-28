import urllib
 
def read_text():									
 	quotes = open("F:\FULL STACK NANODEGREE\project 1\movie_quotes.txt")		
 	contents_of_file=quotes.read()							
 	print (contents_of_file)
 	quotes.close()									
 	check_profanity(contents_of_file)							
 
def check_profanity(text_to_check):
 	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)		
 	output=connection.read()								
 	print (output)					 
 	connection.close()										 
 
read_text()
 				
## for better output

##import urllib
##
##def read_text():									
##	quotes = open("F:\FULL STACK NANODEGREE\project 1\movie_quotes.txt")		
##	contents_of_file=quotes.read()							
##	#print (contents_of_file)
##	quotes.close()									
##	check_profanity(contents_of_file)							
##
##def check_profanity(text_to_check):
##	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)		
##	output=connection.read()								
##	#print (output)					 
##	connection.close()
##	if "true" in output:
##		print("profanity alert")
##	elif "false" in output:
##		print("curse word found")
##	else:
##		print("cant scan properly")
##
##
##read_text()
##		
##
