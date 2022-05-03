This code base loads the assam-river-tender csv file into elasticsearch database. Then it searches for a list of positive words in the whole database. 
Using this filtered data the code then extracts the river names from the field - tender/title using nltk and adds a field named river/name with relevent value. 


Reason for choosing elasticsearch - it's best for usecases where we have to search for a text/keyword in a huge corpus of data. Positive words in this case. And it has the ability to infer schema using the given csv file.


Process followed to extract rivername: Used NLTK to get noun tags that are succeeded and preceeded by the word - 'river' to fetch river names. 
