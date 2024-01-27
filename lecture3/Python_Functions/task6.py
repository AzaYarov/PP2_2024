def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#This way the function will receive a dictionary of arguments, and can access the items accordingly: