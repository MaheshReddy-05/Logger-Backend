from langchain.embeddings.openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(openai_api_key="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")

def generate_embedding(text):
    return embedding_model.embed_query(text)
