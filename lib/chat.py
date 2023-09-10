from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# set openai api key
import os
os.environ["OPENAI_API_KEY"] = "YOUR_OPEN_AI_API_KEY"

docsearch = FAISS.load_local("vector_store", OpenAIEmbeddings())

def ai_reply(query) :
    query = f"""
    Consider yourself as a friendly chatbot and answer to the questions limited by triple backtick
    ```
    {query}
    ```
    """
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = docsearch.similarity_search(query)
    reply = chain.run(input_documents=docs, question=query)
    
    return reply






