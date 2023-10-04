import json
from models import Authors



with open("authors.json", "r", encoding='utf-8') as file:
    data = json.load(file)


for item in data:
    author = Authors(
        fullname=item["fullname"],
        born_date=item["born_date"],
        born_location=item["born_location"],
        description=item["description"]
    )
    author.save()





