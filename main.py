from pypdf import PdfReader, PdfWriter
import panda as pd

def arabic_fonts(text: str) -> str:
  """Fix almost every font problems 
    :return: string"""
  pass

def reader(path: str) -> ...:
  """read contents from pdf file"""
  context = []
  # read using PdfReader
  with PdfReader(path) as reader:
      # pages in the file
      pages = reader.pages
      # check file status
      if not len(pages):
        # invalid file
        return f"Can't find pages in {path}"
      # extract text for each page
      for page in pages:
        context.append(page.extract_text())
        
  return context


def renew_form(pdf: str) -> ...:
  """ renew pdf formate """
  # write using PdfWriter 
  writer = PdfWriter()
  # append pdf context as file
  writer.append(pdf)
  # save it as pdf name
  with open(pdf, "wb") as f:
      writer.write(pdf)
  
  return f"{pdf} is renewed now"
  
  
def contract_no(text: str) -> str:
  pass

def tenancy_dates(text: str) -> str:
  pass

def tenancy_name(text: str) -> str:
  pass

def founder_name(text: str) -> str:
  pass

def national_address(text: str) -> str:
  pass

def payments_schedule(text: str) -> str:
  pass

def data_form(keys:list, values:list) -> ...:
  pass

def file_finder(path: str) -> ...:
  pass


