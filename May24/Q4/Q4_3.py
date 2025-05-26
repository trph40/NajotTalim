def distinct(seq):
    seen = set()
    result = []
    for num in seq:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
