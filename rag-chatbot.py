# dependencies to install
    # pip install python
    # pip install openai
    # pip install langchain
    # pip install langchain-core
    # pip install langchain-community
    # pip install guardrails-ai


from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from openai import OpenAI
from guardrails.hub import GibberishText
from guardrails import Guard
import os
import shutil


DATA_PATH = "data" # path to sources (blogs)
DB_PATH = "chroma" # path to vector database

PROMPT_TEMPLATE =  PromptTemplate.from_template("""
Answer my question given the following context and your own knowledge.

-----

{context}

-----

Now, here is my question: {question}

""")

RAIL_SPEC = """
<rail version="0.1">

<output>
    <object>
        <string name="response" description="the generated LLM response" on-fail="reask">
        <string name="context" description="mentions whether the response was generated with context or without context" format="two-words" on-fail-two-words="reask">
    </object>
</output>

"""


####################### CREATE THE VECTOR DATABASE ###########################

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob = "*.md")
    documents = loader.load()
    return documents


def chunk_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 500,
        length_function = len,
        add_start_index = True
    )

    chunks = text_splitter.split_documents(documents)
    print(f"I have split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


def save_to_db(chunks: list[Document]):
    if os.path.exists(DB_PATH): # shut down existing database
        shutil.rmtree(DB_PATH)
    db = Chroma.from_documents( # create new db
        chunks, OpenAIEmbeddings(), persist_directory = DB_PATH)
    print("Created database.")
    return db

def generate_db():
    docs = load_documents()
    chunks = chunk_documents(docs)
    db = save_to_db(chunks)
    return db


########################## QUERY THE VECTOR DATABASE ###########################

def get_context_from_db(db: Chroma, query: str):
    documents = db.similarity_search(query, k = 3)
    context = "\n\n-----\n\n".join(doc.page_content for doc in documents)
    # print("\n\n-----\n\n" + context + "\n\n-----\n\n")
    return context

########################## CREATE CLIENT ###########################
    

def complete_chat(client: OpenAI, messages: list[dict[str, str]]):
    response = client.chat.completions.create(
        model = "llama3",
        messages = messages,
        temperature = 0.2,
        stream = False
    )

    return response


########################################################################

def main():
    db = generate_db()
    guard = Guard().use(GibberishText, threshold = 0.5, validation_method = "sentence", on_fail = "reask") # set up guardrail

    # SET UP
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3LCJ1c2VybmFtZSI6ImRlbW8ifQ.Si_m0xXsLKQIfSFNCG5xplR27uFDuGOAkkD5FnaVL2M"
    client = OpenAI(base_url="https://llama3-api.clusters.model-suite.simplismart.ai", api_key = token, default_headers = {"username":"demo"})
    opening_statement = "Hi! You can ask me anything about Simplismart."
    messages = [
        {"role": "system", "content": "You are a helpful chatbot that answers the user's questions based on given context."},
        {"role": "assistant", "content": opening_statement}
    ]

    # INTERACTION
    print("\n" + opening_statement + "\n")
    while True:
        # user input
        question = input("> ")
        if question == "quit":
            print("Goodbye!")
            break
        print("\n")

        # guardrails
        guard.validate(question) # guardrail validation

        context = get_context_from_db(db, question)
        prompt = PROMPT_TEMPLATE.format(context = context, question = question)
        messages.append({"role": "user", "content": prompt})

        # generated output
        response = complete_chat(client, messages)
        print(response.choices[0].message.content)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})
        print("\n")


main()