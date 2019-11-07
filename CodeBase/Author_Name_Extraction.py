# Import Section.
import os # For directory stuffs.
from datetime import datetime
from tqdm import tqdm
import json # For analyzing json data.

def nela_dataset_extraction(err_count, errors):
	"""
		This function will extract author data from NELA 2017 datset present in disk.
	"""
	try: # try 2

		author_dataset = []
		count_id = 0
		# Getting path to directory containing NELA 2017 dataset.
		path = input("\nPlease provide the path from root to directory containing NELA 2017 data: ")

		print(os.listdir(path))

		for dir1 in os.listdir(path): # for 1
			sub_path_1 = path + "\\" + dir1
			
			for dir2 in tqdm(os.listdir(sub_path_1)): # for 2
				sub_path_2 = sub_path_1 + "\\" + dir2
				# dir2 contains date
						
				for dir3 in os.listdir(sub_path_2): # for 3
					sub_path_3 = sub_path_2 + "\\" + dir3
					
					for dir4 in os.listdir(sub_path_3): # for 4
						sub_path_4 = sub_path_3 + "\\" + dir4

						# Reading json file.
						article_data = None
						try: # Nested try(2) 1.
							with open(sub_path_4, 'r', encoding="utf8") as datafile:
								article_data = json.load(datafile)
							datafile.close()
						except json.decoder.JSONDecodeError as jerr:
							# Json load error.
							print("\n\nJSONDecodeError Reported.\n\n")
							errors[err_count] = "json.decoder.JSONDecodeError: " + str(jerr) + "."
							err_count = err_count + 1
							errors[err_count] = "Encountered at: " + sub_path_4 + "."
							err_count = err_count + 1
							errors[err_count] = "count_id: " + str(count_id) + "."
							err_count = err_count + 1
							continue
						except Exception as nerr:
							# Unknown error.
							print("\n\nBad Error Reported.\n\n")
							errors[err_count] = "UNKNOWN ERROR: " + str(nerr) + "."
							err_count = err_count + 1
							errors[err_count] = "Encountered at: " + sub_path_4 + "."
							err_count = err_count + 1
							errors[err_count] = "count_id: " + str(count_id) + "."
							err_count = err_count + 1
							continue
						# End of Nested try-except(2) 1 block.
						if (article_data['author'] == '' or article_data['author'].isspace()):
							temp = str(count_id)+', '+'NULL'+', '+article_data['source']+', '+dir2+', '+dir4
						else:
							temp = str(count_id)+', '+article_data['author']+', '+article_data['source']+', '+dir2+', '+dir4
						count_id = count_id + 1
						author_dataset.append(temp)
						
					# End of for 4.
				# End of for 3.

				# Writing data to output file
				with open("Author.txt", 'a') as outputfile:
					for i in author_dataset:
						outputfile.write("%s\n"%i)

				# Freeing up memory.
				author_dataset.clear()

			# End of for 2.
		# End of for 1.

	# End of try 2

	except Exception as err:
		print("\n\nBad Error.\n\n")
		errors[err_count] = "UNKOWN ERROR: " + str(err) + "."
		err_count = err_count + 1
		errors[err_count] = "Encountered at: " + sub_path_4 + "."
		err_count = err_count + 1
		errors[err_count] = "count_id: " + str(count_id) + "."
		err_count = err_count + 1

	# End of try-except 2 block.

	return err_count
# nela_dataset_extraction function boundary.

def web_based_author_extraction(err_count, errors):
	"""
		This function will extract author data from online articles.
	"""

	print("\n\n\t\t Coming soon.....\n\n")

	return err_count
# web_based_author_extraction function boundary.

# <------------------------------------ Code Execution starts from here ------------------------------------>
print("\n\n\t Welcome to author extraction software.\n\n")

MASTER_LOOP_EXIT = 0 # Control loop variable.
errors = {} # For storing all errors for loggin purpose.
error_count = 0 # Maintaining number of error encountered during running state of program.

while (MASTER_LOOP_EXIT == 0): # while 1 

	# User option selection..
	print("\nPlease select what you want to do:")
	print("\n\t0. For exit.")
	print("\n\t1. For extracting author from NELA-2017 dataset.")
	print("\n\t2. For extracting author name from web articles.")
	user_selection = None

	try: #try 1

		user_selection = int(input("\nPlease select one option: "))
	# try 1 boundary.
	except ValueError:
		print("\n\nERROR: Not a number.\n\n")
		errors[error_count] = "Control Selection Error: Invalid value provided."
		error_count = error_count + 1
		user_selection = None

	except Exception as err:
		print("\n\nBad Input.\n\n")
		errors[error_count] = "Control Selection Error: " + str(err) + "."
		error_count = error_count + 1
		user_selection = None

	# try-except 1 boundary.

	# Directing control flow based on user selection.

	if user_selection == None:
		print("\n\tProvide a valid number as choice.\n")

	elif user_selection == 0:
		MASTER_LOOP_EXIT = 1

	elif user_selection == 1:
		error_count = nela_dataset_extraction(error_count, errors)

	elif user_selection == 2:
		error_count = web_based_author_extraction(error_count, errors)

	else:
		print("\nPlease enter valid number/choice!!!!!!!!\n\n")

# End of while 1 loop.

# Storing error log for debugging use.

timestamp = datetime.now()
timestamp = "<-------------------- Log Time: " + str(timestamp) + " -------------------->"

if error_count != 0: #if 1

	err_file = None

	try:
		
		err_file = open("error_log.txt", "a+")

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