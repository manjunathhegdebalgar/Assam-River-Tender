This code base loads the assam-river-tender csv file into elasticsearch database. Then it searches for a list of positive words in the whole database. 
Using this filtered data the code then extracts the river names from the field - tender/title using nltk and adds a field named river/name with relevent value. 
