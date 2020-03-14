# Write your code here
class CoffeeMachine:
    def __init__(self):  
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.money = 550
        self.disposable_cups= 9
        self.all_resources = [self.water, self.milk, self.beans, self.disposable_cups]
        self.coffee_type = None
        self.current_state = 'action' 
        self.active = True
        self.command_to_state = {
            'buy':'choosing_coffee',
            'fill':'filling',
            'take':'take_money',
            'remaining':'remaining_resources',
            'exit' : 'exiting'
        }
        self.required_resources = {
            1 : [250, 0, 16, 1, 4],
            2 : [350, 75, 20, 1, 7],
            3 : [200, 100, 12, 1, 6]
            }
        
    def set_new_state(self, command):
        self.current_state = self.command_to_state[command]

    def receive_input(self, command):
        while True:
            if self.current_state == 'action':
                self.set_new_state(command)
                if self.current_state in ['choosing_coffee', 'filling'] : break
                else: continue

            if self.current_state == 'choosing_coffee':
                self.current_state = 'making_coffee'
            
            if self.current_state == 'making_coffee':
                self.make_coffee(command)
                
            if self.current_state == 'filling':
                self.fill(command)

            if self.current_state == 'take_money':
                self.take()

            if self.current_state == 'remaining_resources':
                self.remaining()

            if self.current_state == 'exiting':
                self.active = False

            break
    def check_resources(self, coffee_type):
        check =  [x - y for x, y in zip(self.all_resources, self.required_resources[self.coffee_type])]
        if min(check) >= 0: return None
        else:
            if check.index(min(check)) == 0 : return 'water'
            if check.index(min(check)) == 1 : return 'milk'
            if check.index(min(check)) == 2 : return 'coffee beans'
            if check.index(min(check)) == 3 : return 'money'
            if check.index(min(check)) == 0 : return 'disposable cups'
            
    def make_coffee(self, coffee_type): 
        if coffee_type in ['1' , '2' , '3']: 
            self.coffee_type = int(coffee_type)
        else: 
            self.coffee_type = str(coffee_type)

        if self.coffee_type in [1, 2, 3]:
            scarce_resource = self.check_resources(self.coffee_type) #control that there are enough resource
            if scarce_resource == None:
                print('I have enough resources, making you a coffee!')
                self.water, self.milk, self.beans, self.disposable_cups = [x - y for x, y in zip(self.all_resources, self.required_resources[self.coffee_type][0:4])]
                self.money = self.money + self.required_resources[self.coffee_type][4]
                self.all_resources = [self.water, self.milk, self.beans, self.disposable_cups]
            else:
                print('Sorry, not enough {0}!'.format(scarce_resource))  
        print()
        
    def fill(self, resource_fill):
        print()
        self.water = self.water + resource_fill[0]
        self.milk = self.milk + resource_fill[1]
        self.beans = self.beans + resource_fill[2]
        self.disposable_cups = self.disposable_cups + resource_fill[3]
        self.all_resources = [self.water, self.milk, self.beans, self.disposable_cups]
        print()

    def take(self):
        print('I gave you {0}'.format(self.money))
        self.money = 0
        print()

    def remaining(self):
        print()
        print('The coffee machine has:')
        print('{0} of water'.format(self.water))
        print('{0} of milk'.format(self.milk))
        print('{0} of coffee beans'.format(self.beans))
        print('{0} of disposable cups'.format(self.disposable_cups))
        print('{0} of money'.format(self.money))
        print()

#main program
coffee_machine = CoffeeMachine()
while coffee_machine.active == True:
    coffee_machine.current_state = 'action'
    command = str(input('Write action (buy, fill, take, remaining, exit):'))
    coffee_machine.receive_input(command)

    if coffee_machine.current_state == 'choosing_coffee':
        print()
        command = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_machine.receive_input(command)

    if coffee_machine.current_state == 'filling':
        print()
        resource_fill = []
        resource_fill.append(int(input('Write how many ml of self.water do you want to add:')))
        resource_fill.append(int(input('Write how many ml of self.milk do you want to add:')))
        resource_fill.append(int(input('Write how many grams of coffee self.beans do you want to add:')))
        resource_fill.append(int(input('Write how many disposable cups of coffee do you want to add:')))
        command = resource_fill
        coffee_machine.receive_input(command)

    
    
    