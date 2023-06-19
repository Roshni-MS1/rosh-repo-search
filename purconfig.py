
openai.api_key = os.getenv("OPENAI_API_KEY")
embed_model = "text-embedding-ada-002"
tokenizer = tiktoken.get_encoding('p50k_base')
#tokenizer = tiktoken.get_encoding("cl100k_base")