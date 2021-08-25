def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output += [item]
    return output

    print("원본:", example)
    print("변환:", flatten(example))