import os


# strip sequence numbers and dates from IBM i source code
def clean_source_line(line: str) -> str:
    
    #All source code has sequence numbers and dates in the first 12 characters
    # IBM i sequence numbers are 7 digits, dates are 6 digits
    # so we strip the first 12 characters pretty simple
    return line[12:].rstrip()

#lil recursive function to clean the source file
def clean_source_file(lines: list[str]) -> list[str]:
    
    cleaned_list = []
    for line in lines:
        cleaned_line = clean_source_line(line)
        
        cleaned_list.append(cleaned_line)
    return cleaned_list
#open, clean, and hand off to watson
def read_source_member(library: str, file: str, member: str) -> str:
    path = f"data/source/raw/{library}/{file}/{member}.rpgle"

    with open(path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()
    
    clean_lines = clean_source_file(raw_lines)
    return "\n".join(clean_lines)
