


# get list of retrieved text
# items retrieved from pinecone 
    contexts = [item['metadata']['text'] for item in res['matches']]

    augmented_query = "\n\n---\n\n".join(contexts)+"\n\n-----\n\n"+query
     print(augmented_query)







   