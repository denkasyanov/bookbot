from collections import defaultdict


def get_num_words(text: str):
    word_count = len(text.split())
    return word_count


def get_num_characters(text: str):
    counts = defaultdict(int)

    for char in text:
        counts[char.lower()] += 1

    return counts


def sort_character_stats(stats: dict):
    character_list = [
        {"character": char, "count": count} for char, count in stats.items()
    ]
    character_list.sort(key=lambda x: x["count"], reverse=True)

    return character_list
