from langchain.document_loaders import ReadTheDocsLoader
    

#load documents 
def readPurviewDocs():
    loader = ReadTheDocsLoader('rtdocs')
    docs = loader.load()
    len(docs)

    print(docs[0].page_content)
    print(docs[5].page_content)
    docs[5].metadata['source'].replace('rtdocs/', 'https://')

    #Create a list of URL reference and page content
    data = []
    for doc in docs:
        data.append({
            'url': doc.metadata['source'].replace('rtdocs/', 'https://'),
            'text': doc.page_content
        })

#readopenaikey
def readSampleDoc():
    with open('C:\\Users\\roshnipatil\\Documents\\GitHub\\openaikey.txt', 'r') as file:
        # Read all lines of the file
        return file.read()

#readpineconekey
with open('C:\\Users\\roshnipatil\\Documents\\GitHub\\pineconekey.txt', 'r') as file:
    # Read all lines of the file
    lines = file.readlines()
    # Print the content of the file
    for line in lines:
        print(line)


#Open the file for reading
def readSampleDoc():
    with open('C:\\Users\\roshnipatil\\Documents\\GitHub\\textpii.txt', 'r') as file:
        # Read all lines of the file
        return file.read()
        