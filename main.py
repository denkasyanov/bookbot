import sys
from stats import get_num_characters, get_num_words, sort_character_stats


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def print_report(path: str):
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")

    print("--------- Character Count -------")
    character_stats = get_num_characters(text)
    sorted_character_stats = sort_character_stats(character_stats)
    for char_stat in sorted_character_stats:
        if char_stat["character"].isalpha():
            print(f"{char_stat['character']}: {char_stat['count']}")

    print("============= END ===============")


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print_report(path)


main()
