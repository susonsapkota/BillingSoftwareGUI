products = []
users = []


def clean_data():
    file = open("file.txt", "r")
    lines = file.read().splitlines()

    for line in lines:
        if line != "":  # cleaning and filtering
            products.append(line.rstrip().split(","))
    file.flush()
    file.close()


def update_inventory():
    f = open("file.txt", "w")
    for i in range(len(products)):
        for j in range(len(products[i])):
            if j < 2:
                f.write(str(products[i][j]) + ",")
            else:
                f.write(str(products[i][j]))
        f.write("\n")
    f.close()