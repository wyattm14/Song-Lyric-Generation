with open("test.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        line.lower()
        uniques |= set(line.split())

    # print(f"Unique words: {len(uniques)}")
    # print(uniques)
    print(lines.count())
    list = []
    for w in uniques:
        print(w)
        list.append(w)
