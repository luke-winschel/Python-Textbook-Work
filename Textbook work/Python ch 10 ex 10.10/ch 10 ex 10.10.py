#(Invoice Class) Create a class called invoice that a hardware store might use after an item is sold.  The invoice should include: a part number (a str), a part description (a str),
#the quantity of the item sold (an int), and a price per item (a decimal).  Your class should have an __int__ method that enables each of the variables.
#Provide a calculate_invoice method that returns the invoice amount.


#Create class
class Invoice:
    """Invoice Class for items purchased at a hardware store"""
    #Intialize part number
    part_num = input(str("Enter the part number purchased: "))
    def __int__(part_num):
        return part_num
    
    #Intialize part description
    part_desc = str(input("Enter a part description: "))
    def __int__(part_desc):
        return part_desc
    
    #Initialize quantity
    quantity = int(input("Enter the number of parts sold: "))
    def __int__(quantity):
        return quantity
    
    #Initialize price per item
    price = float(input("Enter the cost of the item: "))
    def __int__(price):
        return price
    
    #Initialize Invoice Calculation
    calculate_invoice = price * quantity
    def __int__(quantity, price, calculate_invoice):
        return calculate_invoice

    #Initialize complete invoice with all details
    receipt = (f"Invoice \n Your order:\n {part_num} quantity:{quantity}: ${price}\n {part_desc} \n\n Total: \n ${calculate_invoice}")
    def __int__(receipt):
        return receipt
    
    print(receipt)
        
Invoice()