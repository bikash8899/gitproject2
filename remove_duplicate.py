#Function to remove duplicate nos. in a list
def remove (duplicate):
    nlst = []
    for word in duplicate:
        if word not in nlst:
            nlst.append(word)
    return nlst
d = [1, 2, 2, 23, 4, 5, 6]
print(remove(d))
