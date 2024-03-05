from tabulate import tabulate
import random
#The class Item is going to hold the existing inventory details of One Net Cafe and all the functions to do with it
class Item:
    #The existing inventory will be stored in a list called items
    items = []
    def __init__(self, item_id, name, brand, purchase_date, price, category, quantity):
        """This is the costructor function which intialises the class and its instances item_id, name, brand, purchase_date, price, category, quantity"""
        self.item_id = item_id
        self.name = name
        self.brand = brand
        self.date = purchase_date
        self.price = price
        self.category = category
        self.quantity = quantity
        Item.items.append(self)
    @classmethod
    def add(cls, item_id):
        """The class method to add an item"""
        for item in Item.items:
            if item.item_id == item_id:
                print('An item with Item ID', item_id, 'already exists')
                return
        name = input('Enter item name')
        brand = input('Enter brand')
        date = input('Enter Purchase date yyyy/mm/dd')
        price = input('Enter price')
        category = input('Enter type')
        quantity = input('Enter Quantity')
        new_item = cls(item_id, name, brand, date, price, category, quantity)
        print(new_item.item_id, 'has been added to the inventory')
    @classmethod
    def delete(cls,item_id):
        """The class method to delete an item"""
        for item in Item.items:
            if item.item_id == item_id:
                Item.items.remove(item)
                print(item.item_id, 'has been removed from the inventory.')
                return
        else:
            print('No item found with ID', item_id)
    @classmethod
    def update(cls, item_id):
        """The class method to update item details"""
        for item in Item.items:
            if item.item_id == item_id:
                while True:
                    choice=input('What field do you want to update?\n 1.Name\n 2.Brand\n 3.Purchase date\n 4. Price\n 5.Item Category\n 6.Item Quatity\n '
                                 '7. Done Updating\n Please ONLY type in the numbers in relation to the command')
                    if choice.strip()=='1'.strip():
                        new_name=input('Enter updated item name')
                        item.name = new_name
                    elif choice.strip()=='2'.strip():
                        new_brand=input('Enter updated Brand')
                        item.brand=new_brand
                    elif choice.strip()=='3'.strip():
                        new_date=input('Enter updated purchase date yyyy/mm/dd')
                        item.date=new_date
                    elif choice.strip()=='4'.strip():
                        new_price=input('Enter updated price')
                        item.price=new_price
                    elif choice.strip()=='5'.strip():
                        new_category=input('Enter updated category')
                        item.category=new_category
                    elif choice.strip()=='6'.strip():
                        new_quantity=input('Enter updated quantity')
                        item.quantity=new_quantity
                    elif choice=='7':
                        break
                    else:
                        print('choose an available option')
                print('These are the updated values\n','Item ID:',item.item_id,'Item Name:',item.name,'Item Brand:',item.brand,
                      'Item Purchase Date:',item.date,'Item Price:', item.price, 'Item Category:',item.category, 'Item Quantity:',item.quantity)
                return
        else:
            print('ID not found')
    @classmethod
    def view(cls):
        """The class method to view the items in a table"""
        headers = ['ID', 'Name', 'Brand', 'Purchase Date', 'Price', 'Category', 'Quantity']
        table = []
        for item in cls.items:
            row = [item.item_id, item.name, item.brand, item.date, item.price, item.category, item.quantity]
            table.append(row)
        sorted_table = sorted(table, key=lambda x: x[0], reverse=True)
        return (tabulate(sorted_table, headers=headers))
    @classmethod
    def save_items(cls):
        """The class method to save the items to a text file"""
        h = open('Inventory', 'w')
        y = cls.view()
        h.write(str(y))
        h.close()
#Values for the Item Class
Item('001', 'PC', 'Samsung', '2023/01/03', '$950', 'Computer', '30')
Item('002', 'Laptop', 'Apple', '2023/01/04', '$690', 'Computer', '50')
Item('003', 'Phone', 'Apple', '2023/03/04', '$390', 'Mobile', '70')
Item('004', 'Printer', 'HP', '2023/02/07', '$70', 'Visual', '10')
Item('005', 'Scanner', 'ASUS', '2022/06/03', '$65', 'Visual', '5')
Item('006', 'Speakers', 'Samsung', '2023/01/03', '$80', 'Audio', '25')
Item('007', 'Fax machine', 'HP', '2023/01/03', '$85', 'Computer', '15')

def select_dealers(running_count):
      """function to randomly select dealers, this acts the base function for displaying the selected dealers"""
      f = open('Dealers', 'r')
      dealers = f.readlines()
      global selected_dealers
      try:
            selected_dealers = random.sample(dealers, 4)
      except:
            print("There has been an error")
      else:
            if running_count==1:
                  print('4 dealers are selected')
            else:
                  return selected_dealers
      return selected_dealers

def dealer(count):
    """This function is designed to turn the values from the dealers file into a list of dictionaries"""
    global dealer_list
    if count==1:
        f = open('Dealers', 'r')
        x = f.readlines()
    else:
        select_dealers(0)
        x = selected_dealers
    dealer_list = []
    for y in x:
        e = y.strip().split(',')
        dealer_items = [
            {'Name': e[3], 'Brand': e[4], 'Price': e[5], 'Quantity': e[6]},
            {'Name': e[7], 'Brand': e[8], 'Price': e[9], 'Quantity': e[10]},
            {'Name': e[11], 'Brand': e[12], 'Price': e[13], 'Quantity': e[14]}
        ]
        dealer_dict = {
            'Dealer Name': e[0],
            'Contact No': e[1],
            'Location': e[2],
            'Items': dealer_items
        }
        dealer_list.append(dealer_dict)

def sort(list):
    """This function serves as a sorting algorithm to sort the dealer details by location"""
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if list[j]['Location'] > list[j + 1]['Location']:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def view_dealers():
    """This is the function to view the randomly selected dealer details and sort them by location"""
    dealer(0)
    sorted_list=sort(dealer_list)
    for l in sorted_list:
        print(l['Dealer Name'],l['Contact No'], l['Location'])

def Display_dealer_items():
      """This is the function to view the items of the selected dealers"""
      name= input('Enter required Dealers Name ')
      dealer(1)
      for u in dealer_list:
            if u['Dealer Name'].casefold()==name.casefold():
                  for i in u['Items']:
                        print(i['Name'], i['Brand'], i['Price'])
                  return
      else:
            print('Dealer not found')

#The main menu for the system
name=str(input("Welcome to the One Net Cafe console menu\n What's your name?\n"))
print('Hi', name)
while True:
    Choice =input("What would you like to do?:\n AID: Add item\n DID: Delete item\n UID: Update item\n VID: View Item\n SID: Save the items to the text file\n "
                  "SDD: Select 4 random dealers\n VRL: Display the details of the randomly selected dealers\n LDI: Display the items of the given dealer\n ESC: Quit\n")
    if Choice.casefold().strip()=='AID'.casefold():
        item_id = input('Enter item ID')
        Item.add(item_id)
    elif Choice.casefold().strip()=='DID'.casefold():
        item_id = input('Enter item ID you want to remove')
        Item.delete(item_id)
    elif Choice.casefold().strip()=='UID'.casefold():
        item_id = input('Enter item ID')
        Item.update(item_id)
    elif Choice.casefold().strip()=='VID'.casefold():
        print(Item.view())
    elif Choice.casefold().strip()=='SID'.casefold():
        Item.save_items()
    elif Choice.casefold().strip()=='SDD'.casefold():
        select_dealers(1)
    elif Choice.casefold().strip()=='VRL'.casefold():
        view_dealers()
    elif Choice.casefold().strip()=='LDI'.casefold():
        Display_dealer_items()
    elif Choice.casefold().strip()=='ESC'.casefold():
        print('Thank You for using our system',name,'\nSee you soon!')
        break
    else:
        print('Please choose one of the available commands')