from functions import utils
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    # apply to
    apply_to = "Sea Labs"
    for_position = "Back End Engineer"

    # school
    major = os.getenv("MAJOR")
    degree = os.getenv("DEGREE") # free, english or indonesian depending on template
    school = os.getenv("SCHOOL")
    
    # previous position
    position = os.getenv("POSITION")
    company = os.getenv("COMPANY")

    # your full name
    full_name = os.getenv("FULL_NAME")

    data = {
        "apply_to": apply_to,
        "for_position": for_position,
        "major": major,
        "degree": degree,
        "school": school,
        "position": position,
        "company": company,
        "full_name": full_name
    }

    # for row in csv_reader:
    template = utils.load_file()
    description = template.format(**data)

    utils.save_file(description)

if __name__ == "__main__":
    main()