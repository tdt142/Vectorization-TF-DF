class Document:
    def __init__(self, doc_id):
        self.id = doc_id
        self.tfdict = {}
        
    def tokenize(self, text):
        #Remove the punctuation
        word2 = text.lower().replace(',','')
        word3 = word2.replace('.','')
        word4 = word3.replace('-','')
        word5 = word4.replace(';','')
        word6 = word5.replace(':','')
        word7 = word6.replace('""','')
        word8 = word7.replace('!','')
        word9 = word8.replace('/','')
        word10 = word9.replace(']','')
        
        #Split words by space
        words = word10.split(" ")
        for word in words:
            if word not in self.tfdict:
                self.tfdict[word] = 1 #Add word to dictionay if it is not in, and set the frequency to 1
            else:
                self.tfdict[word] = self.tfdict[word] + 1 #Increase word's frequency by 1 if it is in the dictionary

def vectorize(data_path):
    data_path = "files"
    dfs = {}
    for i in range (1, 21): #For loop to go over 20 txt files (change this number if you have more document)
        with open('files//' + str(i) +'.txt') as txtf:
            content = txtf.read() #Read the files
            doc = Document(i) #Call Document Class
            doc.tokenize(content) #Process the content
            save_dictionary(doc.tfdict,'results/tf_'+str(i)+'.txt') #Save to the term frequency dictonary and format the name
            for freq in doc.tfdict: #check the word in term frequency dictionary
                if freq not in dfs: 
                    dfs[freq] = 1 #Add the word to the document dictionary if it is not in, and set document frequency to 1
                else:
                    dfs[freq] = dfs.get(freq,0)+1 #Increase the word's frequency in the dictionary by 1
        txtf.close()
    save_dictionary(dfs,'results/df.txt') #Save the document dictionary and format the name

def save_dictionary(dict_data, file_path_name):
    f =  open(file_path_name, "w+") #Open file to write data
    for key in dict_data:
        val = dict_data[key]
        f.write(key + '\t' + str(val) +'\n') #write data to file in pair of key and value, and format.
    f.close()

vectorize("files\./") #Process the text files in the directory