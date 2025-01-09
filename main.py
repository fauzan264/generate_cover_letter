from functions import utils

# apply to
apply_to = "Shopee"
for_position = "Backend"
# school
major = "Informatics Engineering"
degree = "Bachelor’s degree" # bebas, bahasa inggris atau indo tergantung template
school = "Universitas Mercu Buana"
# previous position
position = "Tech Support"
company = "GoTo Logistics"
# your full name
full_name = "Ahmad Fauzan"

data = {
    "apply_to": apply_to,
    "for_position": for_position,
    "major": major,
    "school": school,
    "position": position,
    "company": company,
    "full_name": full_name
}

# for row in csv_reader:
template = utils.load_file()
description = template.format(**data)

utils.save_file(description)