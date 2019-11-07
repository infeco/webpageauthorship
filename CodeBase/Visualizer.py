import matplotlib.pyplot as plt
import json

# Data to plot
labels = 'No author name', 'Same author as source', 'Author name present'
sizes = []
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice

try: # try 1.

	source_with_author_null = {} # Contains source name having no author name.
	source_count = {} # Contains total article found from particular source.
	author_same_source = {} # Contains source name having same name for author as of source.
	article_id_list_with_same_source_author = [] # Article id for same author and source.
	article_id_list_with_null_author = [] # Article id for article with no author name.
	total_article_count = 0

	# Loading data.
	with open('Source_with_author_null', 'r') as f1:
		source_with_author_null = json.load(f1)

	with open('Source_count', 'r') as f1:
		source_count = json.load(f1)

	with open('Author_same_source', 'r') as f1:
		author_same_source = json.load(f1)

	with open('Article_id_list_with_same_source_author', 'r') as f1:
		article_id_list_with_same_source_author = json.load(f1)

	with open('Article_id_list_with_null_author', 'r') as f1:
		article_id_list_with_null_author = json.load(f1)

	with open('Author.txt', 'r') as f1:
		for line in f1:
			total_article_count = total_article_count + 1

	author_null_count = len(article_id_list_with_null_author)
	author_same_count = len(article_id_list_with_same_source_author)
	article_with_author_count = total_article_count - author_null_count - author_same_count
	sizes.append(author_null_count)
	sizes.append(author_same_count)
	sizes.append(article_with_author_count)

# End of try 1.

except Exception as err:
	print(err)

# End of try-except 1 block.
# Plot

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()