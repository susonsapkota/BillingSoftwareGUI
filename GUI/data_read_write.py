
cleaned_data = []


# reads the inventory from .txt and stores in variable
def clean_data():
    file = open("file.txt", "r")
    lines = file.read().splitlines()

    for line in lines:
        cleaned_data.append(line.rstrip().split(","))
    file.flush()
    file.close()


# displays the available products
def display_product():
    print("Available Products:")
    print("==========================================")
    # Formatting so output looks good
    print("ID\t\tProduct\t\tPrice\t\tAvailable Quantity")
    print("0:\t\t" + cleaned_data[0][0] + "\t\t" + cleaned_data[0][1] + "\t\t\t" + cleaned_data[0][2])
    print("1:\t\t" + cleaned_data[1][0] + "\t\t" + cleaned_data[1][1] + "\t\t\t" + cleaned_data[1][2])
    print("2:\t\t" + cleaned_data[2][0] + "\t\t\t" + cleaned_data[2][1] + "\t\t\t" + cleaned_data[2][2])

    print("===========================================")


# database maintain(quantity reduces after each costumer buys that product)
# this again stores to database which is the same .txt file
def update_inventory():
    f = open("file.txt", "w")

    for k in range(len(user_input.products)):

        cleaned_data[user_input.products[k]][2] = int(cleaned_data[user_input.products[k]][2]) - int(
            user_input.quantity[k])
        cleaned_data[user_input.products[k]][2] = str(cleaned_data[user_input.products[k]][2])

        for i in range(len(cleaned_data)):
            for j in range(len(cleaned_data[i])):
                if j < 2:
                    f.write(cleaned_data[i][j] + ",")
                else:
                    f.write(cleaned_data[i][j])
            f.write("\n")
    f.flush()
    f.close()
