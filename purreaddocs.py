from langchain.document_loaders import ReadTheDocsLoader
    

#load documents 
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
