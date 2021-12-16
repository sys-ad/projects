# my_name= "Nosa"
# my_name2= "Shafan"
# my_name3= "Michael"
# my_name4= "Donna"

# lists are indexed starting from 0
cohort_name= "2021-rtt-18"
instructors= ["Nosa", "Shafan", "Michael", "Donna"]
year_started= [2021, 2019, 2018,2021]
is_Arr= [True, False]

# print(len(instructors))
def report(instructor, year):
    return f"{instructor} started perscholas in {year} and currently teaching cohort {cohort_name}"

# print(type(year_started[0]))
year_started[0]= 2034

print("Welcome, to Perscholas Directory of instructors...")
user_input= input("Please type the instructor name to check: ").capitalize()
# print(user_input)
result= ""
for person in instructors:
    result= f"Sorry, {user_input} can not be found in the instructor list."
    if user_input == person:
        i= instructors.index(person)
        result= report(person, year_started[i])
        break
        
        
print(result)
    
