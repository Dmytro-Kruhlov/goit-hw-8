from models import Quotes, Authors
import redis
from redis_lru import RedisLRU


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def quote_by_tag(com):
    tag = command.split("tag:")[1].strip()
    quotes = Quotes.objects(tags__iregex=f".*{tag}.*")
    for quote in quotes:
        print(quote.quote)

@cache
def quote_by_author(com):
    author_name = command.split("name:")[1].strip()
    author = Authors.objects(fullname__iregex=f"^{author_name}.*").first()
    if author:
        quotes = Quotes.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print("Автор не знайдений")


if __name__ == "__main__":
    while True:
        command = input("Введіть команду: ")

        if command.startswith("name:"):
            quote_by_author(command)

        elif command.startswith("tag:"):
            quote_by_tag(command)

        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip().split(",")
            quotes = Quotes.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        elif command == "exit":
            break

        else:
            print("Невідома команда")
