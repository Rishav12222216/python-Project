# inputting all the contacts

contacts = {
"JAIDEEP": 9346158730,
"lokesh": 9010584269,
"chaitanya": 9515245161,
"yash": 9515958818,
"nikhil": 7801070363,
"deva": 9494731626,
"Ravi kiran": 9347280958,
"sandeep": 9392322385,
"rishab": 7004998632,
"koushik": 6300413811,
"kartheek": 7671944891,
"pardhu": 9505543949,
"rangaraju": 9392383422,
"jeshwanth": 9133172728,
"murali": 9640742433,
"harsha": 9392306018,
"adarsh": 8948282304,
}
9

# Searches the dictionary and prints the key value pair incase the key isn't present, it adds it to the dict and prints it''

def single_search():
	name = input(">>>Enter the name of the contact you wish to search for: ")
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
		b = input("\nNo such contact found\nIf you wish to add one, type 'Yes' else type 'No': ")
		if b == "yes":
			new_contact(name)
			print(f"{name}: {contacts[name]}")
		elif b == "no":
				pass
		else:
			print("Enter either yes or no n")

# Searches the dictionary and prints multiple key value pair and incase any key isn't present, it adds it to the dict and prints it along with the others.


def multiple_search():
	result = {}
	s1 = []
	s = 0
	name1 = input(">>>Enter the names of the contacts seperated by commas 2: ").split(",")
	for i in name1:
		i = i.upper()
		if i in contacts:
			result[i] = contacts[i]
		else:
			s1.append(i)
			s += 1
		if s > 0:
			c = (input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or No: ")).lower()
			if c == "yes":
				for i in s1:
					new_contact(i)
					if i in contacts:
						result[i] = contacts[i]
						print()
						print(result)
			elif c == "no":
				print()
				if result == {}:
					pass
				else:
					print()
					print(result)
	     	
#adds new contact every time its called			
	     		
def new_contact(contact_name):
		print()
		contact_number=int(input(">>>Enter their contact number👀: "))
		contacts[contact_name]=contact_number
	     
choice=int(input("Would you like to: \n\n1. Search for a single contact👤  \n2. List all the contacts📜 \n3. Search for multiple contacts \n \n>>>Enter your choice: "))

if choice==1:
	single_search()
	
elif choice==2:
	print()
	print(contacts)
	
elif choice==3:
	multiple_search()

else:
	print("Choose from the given options!")
