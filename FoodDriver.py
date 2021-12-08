from FoodModule import FoodModule

#Returns list of items
def getListOfItems():
    foodItems=[]
    while True:
        N=int(input("How many items will you order today? "))
        if N<=0:
            print("Number of items must be atleast 1.")
        else:
            break
    #Loop for N items
    for i in range(0,N):
        print("Item #",(i+1),"-")
        name=input("Enter food:")
        while True:
            amount=float(input("Enter amount of pounds: "))
            if amount<=0:
                print("Amount of pounds must be greater than 0.")
            else:
                break
        foodItems.append(FoodModule(name,amount))
        print("\n")
    return foodItems

#Display item list
def displayItems(items):
    print("Here's a summary of the items purchased:\n---------------------------------------------")
    for item in items:
        print(item)
        print("\n")

#Calculate total cost of all items
def calculateTotalCost(items):
    totalCost=0
    for item in items:
        totalCost+=item.getCalculatedCost()
    return totalCost

#Main function
def main():
    items=getListOfItems()
    displayItems(items)
    total=calculateTotalCost(items)
    print(f'Total cost:$ {total:.2f}')

#Driver code
main()
        