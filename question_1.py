customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
salary = [155000, 755000, 455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

i = 0
while i < len(customers):
    try:
        if salary[i] > 555000 and taxes[i]/salary[i] < 0.3:
            print(customers[i])
    
        i += 1
    
    except Exception as e:
        print(f"Error: {e}")