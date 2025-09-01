#Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
my_tuple = ("Laptop", 50000, "Black" ,'Samsung', "Electronics")
print("My Tuple:", my_tuple)

#Access and print the second element of the tuple product.
second_item = my_tuple[1]
print("Second item in the tuple:",second_item)

#Slice and print the last two elements of the product tuple.
print("#Slice last two elements:",my_tuple[3: 5])

#Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in my_tuple:
    print("Electronics is present in tuple")
else:
    print("Electronics is not present in tuple")

#Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900).
my_second_tuple = (1000, 1500, 1200, 1100, 900)
print(my_second_tuple)
# Count how many times 1000 appears.
print("Count of 1000 in tuple:", my_second_tuple.count(1000))

#Find and print the maximum and minimum price from the prices tuple.
print("max price in tuple:", max(my_second_tuple))
print("min price in tuple:", min(my_second_tuple))

#Use a loop to print each item from the product tuple on a new line.
for a in my_second_tuple:
    print("elements in tuple:", a, "\n")

#Convert the product tuple to a list. 
my_list = list(my_second_tuple)
# Change the price to 55000,
my_list.append(55000)
#  then convert it back to a tuple. 
my_converted_tuple = tuple(my_list)
# Print the updated tuple.
print("updated tuple:", my_converted_tuple)

#Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
temp_tuple = ("In Stock",)
result_tuple = my_tuple + temp_tuple
print("Result tuple:", result_tuple)

#Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
my_convert_list = list(result_tuple)
my_convert_list.remove("Electronics")
new_tuple = tuple(my_convert_list)
print("After Remove Electronics New tuple:", new_tuple)

# Unpack the tuple product into three variables and print each variable.
name, price, color, *rest = new_tuple
print("Unpacked Values - Name:", name, ", Price:", price, ", Color:", color)

#Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
prod1 = ("TV", "Radio", "Music Player")
prod2 = ("Car", "Bus", "Byke")
prod3 = ("Table", "Chair", "Bed")

nested_prod = (prod1, prod2,prod3)
print("second product:", nested_prod[1: 2])
