def read_inventory(filename):
    try: 
        with open(filename, 'r') as file:
            inventory = {}
            for line in file:
                product, quantity, price = line.strip().split(',')
                inventory[product] = (int(quantity), float(price))
            return inventory
    except FileNotFoundError:
        return{}
    
def add_product():

def update_product():

def display_inventory():

def check_status():

def write_inventory():