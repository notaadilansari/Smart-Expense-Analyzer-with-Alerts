def smart_exp_analyzer():
	num_expenses = int(input("Enter number of Expenses : "))
	exp_amt=[]
	category_total={}
	for i in range(1,(num_expenses +1)):
		amt = int(input(f"Expense {i} amount : "))
		category=input(f"Expense {i} category : ")
		exp_amt.append(amt)
		if amt>500:
			print("Alert : High expense detected")
		category_total[category]=category_total.get(category,0)+amt
	#calculating total expense
	total_exp=sum(exp_amt)
	#calculating avg expense
	avg_exp=total_exp/num_expenses
	#printing category-wise total
	print(category_total)
	#finding and printing the  highest category
	h = list(category_total.values())
	h.sort()
	highest_spending = h[-1]
	for key,value in category_total.items():
		if value==highest_spending:
			highest_category=key
	print(f"Highest Spending in {highest_category} is {highest_spending}")
	if avg_exp<=200:
			print("Controlled Spending")
	elif 200<avg_exp<=400:
			print("Moderate Spending")
	else:
			print("High Spending")
smart_exp_analyzer()
