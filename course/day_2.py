import  PyPDF2
def extract_text_from_pdf(pdf_file):
  text=""
  with open(pdf_file,'rb')as file:
    reader=PyPDF2.PdfReader()file
    for page in read.pages:
      text +=page.extract_text()
  return text

def clean_text():
  return "".join(text.split())

def sliding_window_chunk(chunk,text_size=1000,overlap_size=20):
  words=text.split()
  chunks=[]
  start = 0
  while start < len(words):
    end = start + chunk_size
    chunk = words[start:end]
    chunks.append(" ".join(chunk))
    if end == len(words):
      break
    start = end - overlap_size
  return chunks

if __name__ == "__main__":
    pdf_path = "policy.pdf"  # Replace with your PDF file path
    text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(text)
    chunks = sliding_window_chunk(cleaned_text, chunk_size=100, overlap_size=20)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n{'-'*50}\n")
