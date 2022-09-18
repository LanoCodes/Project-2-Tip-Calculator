print('\n*** Welcome to Tip Calculator Pro ***\n')

choice = 'y'

while(choice == 'y'):
  bill_total = float(input('What was the total bill? $'))
  tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
  party_total = int(input('How many people should split the bill? '))
  
  bill_incl_tip = bill_total * ((tip_percentage/100) + 1.0)
  
  total_per_person = round((bill_incl_tip / party_total), 2)

  final_amount = '{:.2f}'.format(total_per_person)
  
  print(f'Each person should pay: ${final_amount}')

  choice = input('\nCalculate another tip? y or n\n')