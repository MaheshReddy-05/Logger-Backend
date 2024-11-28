import pinecone
from utils.embedding_utils import generate_embedding

pinecone.init(api_key="7ff4bb0f-ae99-4062-983d-3aafc3f6bcc3", environment="us-east-1")
index_name = "llmasg"
index = pinecone.Index(index_name)
def get_nearest_logs(log_data, top_k=2):
    log_embedding = generate_embedding(log_data)

    query_response = index.query(
        vector=log_embedding,
        top_k=top_k,
        include_metadata=True
    )

    nearest_logs = [
        match["metadata"]["solution"] for match in query_response["matches"]
    ]
    return nearest_logs
