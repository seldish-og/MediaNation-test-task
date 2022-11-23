x = ["one", "two", "three", "four"]

for i in range(0, len(x) - 1, 2):
    print(x[i])
    print(x[i + 1])


for i in range(last_index, urls, 2):

    first_url = urls[i]
    second_url = urls[i + 1]
    make_threads(first_url, second_url)
    index.update_index(2)
