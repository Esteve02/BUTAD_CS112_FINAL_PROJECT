class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for product in self.products:
                print(f"{product.name} - Price: ${product.price:.2f} - Stock: {product.stock}")

    def check_stock(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.stock
        return None

def add_product_to_inventory():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    return Product(name, price, stock)

def main():
    inventory = Inventory()

    while True:
        print("\n1. Add product to inventory")
        print("2. Display inventory")
        print("3. Check stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product = add_product_to_inventory()
            inventory.add_product(product)
            print("Product added to the inventory.")

        elif choice == "2":
            inventory.display_inventory()

        elif choice == "3":
            product_name = input("Enter product name to check stock: ")
            stock = inventory.check_stock(product_name)
            if stock is not None:
                print(f"Stock of {product_name}: {stock}")
            else:
                print(f"{product_name} not found in the inventory.")

        elif choice == "4":
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
