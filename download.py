import base64


def download_document(document, doc_name:str) -> str:
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    
    document.save("temp_test.docx")

    with open("temp_test.docx", "rb") as f:
        #Read the whole file at once
        data = f.read()
    
    b64 = base64.b64encode(data).decode()
    
    f.close()

    href = f'<a href="data:file/csv;base64,{b64}" download="{doc_name}">Download {doc_name} </a>'

    return href
