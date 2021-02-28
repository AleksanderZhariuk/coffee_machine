from machine_features import MENU, resources
import os


KEEP_WORKING = True
INGREDIENTS_IS_OK = True


def user_choice(answer):
	global INGREDIENTS_IS_OK
	user_drink_requirements = MENU[answer]['ingredients']
	not_enough_ingredients = []
	for element in user_drink_requirements:
		if user_drink_requirements[element] > resources[element]:
			not_enough_ingredients.append(element)

	# 	PRINT NEEDABLE INGREDIENTS
	if len(not_enough_ingredients) > 0:
		needable_ingredients = '\n'.join(not_enough_ingredients)
		print(f'Sorry, there are not enough ingredients:\n{needable_ingredients}')
		INGREDIENTS_IS_OK = False
		return INGREDIENTS_IS_OK
	else:
		for element in user_drink_requirements:
			resources[element] -= user_drink_requirements[element]
		INGREDIENTS_IS_OK = True
		return INGREDIENTS_IS_OK

#	COINS OPERATIONS
def proccess_coins(drink):
	print('Please, insert coins.')
	quarters = int(input('How many quarters?: '))
	dimes = int(input('How many dimes?: '))
	nickles = int(input('How many nickles?: '))
	pennies = int(input('How many pennies?: '))

	if 'money' not in resources.keys():
		resources['money'] = 0

	summary = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)


	if summary < MENU[drink]['cost']:
		print("Sorry that's not enough money. Money refunded.")
		resources['money'] = 0
	else:
		change = round(summary - MENU[drink]['cost'], 2)
		resources['money'] += MENU[drink]['cost']
		print(f"Here is ${change} for change")


def machine_commands(answer):
	global KEEP_WORKING
	#	REPORT
	if answer == 'report':
		for key in resources:
			if key == 'money':
				print(f'Money: ${resources["money"]}')
			else:
				print(f"{key.capitalize()}: {resources[key]}ml")

	#	SECRET WORD FOR STOPPING MACHINE
	elif answer == 'off':
		print('Machine is stopped')
		KEEP_WORKING = False
		return KEEP_WORKING

	# 	DRINKS
	else:
		user_choice(answer)
		if INGREDIENTS_IS_OK == False:
			pass
		else:
			proccess_coins(answer)


#	COIN TRANSCATION
resources['money'] = 0
os.system('cls' if os.name == 'nt' else 'clear')
while KEEP_WORKING:
	user_asnwer = input('What would you like? (espresso/latte/cappuccino): ').lower()
	machine_commands(user_asnwer)
