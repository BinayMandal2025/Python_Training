data = [
    {
   "name":"Ravi",
    "age": 45,
    "location":"Delhi",
   },
   {
   "name":"Ram",
    "age": 46,
    "location":"Kolkata",
   },
   {
   "name":"Shyam",
    "age": 47,
    "location":"Mumbai",
   }
]
 
with open('C:/RDT/Python/Data Types/file/myfile.txt','w') as f:
    for person in data:
        for key, value in person.items():
            f.write(f"{key}:{value}\n")
        f.write("\n")
