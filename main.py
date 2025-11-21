import re
from pypdf import PdfReader, PdfWriter
import pandas as pd


def arabic_fonts(text: str) -> str:
    """Fix almost every font problems
    :return: string"""
    pass

def reader(path: str) -> str | list:
    """read contents from pdf file"""
    context = []
    # read using PdfReader
    with PdfReader(path) as rd:
        # pages in the file
        pages = rd.pages
        # check file status
        if not len(pages):
        # invalid file
            return f"Can't find pages in {path}"
        # extract text for each page
    for page in pages:
        context.append(page.extract_text())

    return context


def renew_form(pdf: str) -> str:
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
    for item in text:
        if "Contract No" in item:
            contract_number = item.split("Contract No")[1].split(":")[0].replace(". ", "")

            return contract_number

    return "Contract No not found."

def tenancy_dates(text: str) -> str:
    """tenancy dates"""
    pass

def tenancy_name(text: str) -> str:
    """tenancy name"""
    pass

def founder_name(text: str) -> str | list | None:
    """founder name"""
    company_name = None
    for item in text:
        if "name/Founder" in item:
            # filter company name
            # company_name = "".join(text[i:i + 2]).split("Organization")[0]
            company_name = "".join(item).split("Organization")[0]

            # filter only company name
            company_name = company_name.rsplit(" ", 1)[0].replace("name/Founder", "")[:-3]

    return company_name

def national_address(text: str) -> str:
    """national address format"""
    for item in text:
        if "National Address" in item:
            national_addr = item.replace("National Address", "")

            return national_addr

    return "National Address not found."

def payments_schedule(text: str) -> str | list | None:
    """payments schedule """
    pattern = r"\d{2}-\d{2}-\d{4}\s+\d{2}-\d{2}-\d{4}\s+[\d.]+\s+\d+\s+\d{2}-\d{2}-\d{4}\s+\d{2}-\d{2}-\d{4}"
    payments = None
    for item in text:
        payments = re.findall(pattern, item)

    # check status
    print([i for i in payments])
    return payments

def data_form(keys:list, values:list) -> str | list | None:
    """data form"""
    pass

def file_finder(path: str) -> str | list | None:
    """file finder"""
    pass



