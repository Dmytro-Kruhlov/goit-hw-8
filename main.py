
from models import Quotes, Authors


if __name__ == "__main__":

    while True:
        command = input("Введіть команду: ")

        if command.startswith("name:"):
            author_name = command.split("name:")[1].strip()
            author = Authors.objects(fullname=author_name).first()
            if author:
                quotes = Quotes.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("Автор не знайдений")

        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            quotes = Quotes.objects(tags=tag)
            for quote in quotes:
                print(quote.quote)

        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip().split(",")
            quotes = Quotes.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        elif command == "exit":
            break

        else:
            print("Невідома команда")
