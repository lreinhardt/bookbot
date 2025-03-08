def count_words(s):
    return len(s.split())


def count_characters(s:str):
    d = {}

    for c in s.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    return d


def sort_on(d:dict):
    return d["count"]


def sort_characters_count(d:dict[str,int]):
    sorted_list = []

    for c in d:
        if not c.isalpha():
            continue
        sorted_list.append({"character": c, "count": d[c]})
        sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list
