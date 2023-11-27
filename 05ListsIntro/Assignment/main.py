def make_abc():
    result = ["a", "b", "c"]
    return result

print("Demenstate make abc")
print(make_abc())


def equal_edges(items):
    first = items[0]
    last = items[-1]
    result = first == last 

    if first == last:
        return True
    else:
        return False
    
print("Demenstrate equal_edges")
print("[1, 2, 1] ->", equal_edges([1, 2, 1]))

