# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

#Benjamin Page
#2/7/2019
#Variable "authors" was misspelled, print statement was not in parentheses. There is no definition for 'author date' or 'authors.items'.

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889" }

for authors, date in authors.items():
    print ("%s" % %author, + " died in ", + "%s." % date)
