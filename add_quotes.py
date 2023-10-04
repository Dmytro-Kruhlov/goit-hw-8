import json
from models import Authors, Quotes

with open("quotes.json", "r", encoding='utf-8') as f:
    q_data = json.load(f)


for item in q_data:
    a_name = item["author"]
    q_author = Authors.objects(fullname=a_name).first()
    quote = Quotes(
        tags=item["tags"],
        author=q_author,
        quote=item["quote"]
    )
    quote.save()