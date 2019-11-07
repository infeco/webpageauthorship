# import section.
from datetime import datetime
import json

# <------------------ Program execution begins from here -------------------->

file_name = input("Please provide the file name: ")

errors = {} # For storing all errors for loggin purpose.
error_count = 0 # Maintaining number of error encountered during running state of program.

try: # try 1.

	with open(file_name, 'r') as f: # with 1.

		line_id = ""
		line_count = 0
		source_with_author_null = {} # Contains source name having no author name.
		source_count = {} # Contains total article found from particular source.
		author_same_source = {} # Contains source name having same name for author as of source.
		article_id_list_with_same_source_author = [] # Article id for same author and source.
		article_id_list_with_null_author = [] # Article id for article with no author name.

		for line in f: # for 1.
			
			try: # try 1-1.
				temp = line.split(',')
				line_id = temp[0].strip() # Extracting Id.
				author = temp[1].strip() # Extracting Author name.
				source = temp[2].strip() # Extracting News source.

				if(source in source_count.keys()): # if 2.
					source_count[source] = source_count[source] + 1
				else:
					source_count[source] = 1
				# end of if-else 2.
				
				if('NULL' in author): # if 3.
					if (source in source_with_author_null.keys()):
						source_with_author_null[source] = source_with_author_null[source] + 1
					else:
						source_with_author_null[source] = 1

					article_id_list_with_null_author.append(line_id)
				# if 3.

				if(author in source): # if 4.
					if (source in author_same_source.keys()):
						author_same_source[source] = author_same_source[source] + 1
					else:
						author_same_source[source] = 1

					article_id_list_with_same_source_author.append(line_id)
				# end of if 4.
				line_count = line_count + 1
			# End of try 1-1.

			except Exception as nerr:
				print("\n\nError Encountered at line: %s.\n\n"%str(line_count))
				errors[error_count] = "UNKOWN ERROR: " + str(nerr) + "."
				error_count = error_count + 1
				errors[error_count] = "Encountered at line: " + str(line_count) + "."
				error_count = error_count + 1
				errors[error_count] = "line_id: " + line_id + "."
				error_count = error_count + 1
				continue

			# End of try-except 1-1 block.
		# End of for 1.
	f.close()
	# End of with 1.

	# Storing all data.

	with open('Source_with_author_null', 'w') as f1:
		json.dump(source_with_author_null, f1)

	with open('Source_count', 'w') as f1:
		json.dump(source_count, f1)

	with open('Author_same_source', 'w') as f1:
		json.dump(author_same_source, f1)

	with open('Article_id_list_with_same_source_author', 'w') as f1:
		json.dump(article_id_list_with_same_source_author, f1)

	with open('Article_id_list_with_null_author', 'w') as f1:
		json.dump(article_id_list_with_null_author, f1)
# End of try 1.

except Exception as err:
	print("\n\nBad Error.\n\n")
	errors[error_count] = "UNKOWN ERROR: " + str(err) + "."
	error_count = error_count + 1

# End of try-except 1 block.

# Storing error log for debugging use.

timestamp = datetime.now()
timestamp = "<-------------------- Log Time: " + str(timestamp) + " -------------------->"

if error_count != 0: #if 1

	err_file = None

	try:
		
		err_file = open("Analyzer_error_log.txt", "a+")

		err_file.write("\n\n")
		err_file.write(timestamp)
		err_file.write("\n\n")

		# Logging data.
		for log in errors:

			report = str(log) + ": " + errors[log] + "\n"
			err_file.write(report)


	except Exception as e:
		print("Logs not reported.")

	finally:
		if err_file == None:
			pass
		else:
			err_file.close()
# end of if 1

print("\n\n\n----------------------- Thank You -----------------------\n\n\n")