# SPLIT THE DOCS INTO CHUNKS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def split_docs(docs: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=100,
                                                   length_function=len,
                                                   is_separator_regex=False)
    return text_splitter.split_documents(docs)