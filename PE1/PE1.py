def count_unique_words(statement):
    exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

    words = statement.split()

    word_count = {}
    for word in words:
        if word.lower() not in exclude_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    lower_case_words = {word: count for word, count in word_count.items() if word.islower()}
    upper_case_words = {word: count for word, count in word_count.items() if word.isupper() or word.istitle()}

    sorted_lower_case_words = sorted(lower_case_words.items())
    sorted_upper_case_words = sorted(upper_case_words.items())

    for word, count in sorted_lower_case_words:
        print(f"{word:<10} - {count}")
    for word, count in sorted_upper_case_words:
        print(f"{word:<10} - {count}")

    total_filtered_words = sum(word_count.values())
    print(f"Total words filtered: {total_filtered_words}")

statement = input("Enter a string statement:\n")
count_unique_words(statement)