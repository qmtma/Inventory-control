import csv # csv manipulation library
from tabulate import tabulate # table format library.
def AddItem(templist): # add item function
    print("Item Addition to stock")
    car_make = input("Enter The Car Make: ")
    car_model = input("Enter The Car Model: ")
    part_no = input("Enter Part No.: ")
    part_name = input("Enter Part Name: ")
    part_Quantity = input("Enter Part Quantity: ")
    part_price = input("Enter Part Price: ")
    # append user input to the 2d list
    templist.append([part_no, part_name, car_make,car_model,part_Quantity,part_price])
    print("Do Your Want To Save? (Y/N) ")
    answer = input()
    if answer in ["y", 'Y']: # if user confirms his inputs write the 2d list to the inventory file
        with open("inventory.csv", 'w', newline="") as CSV:
            writer = csv.writer(CSV, delimiter=',')
            writer.writerows(templist)
            print("Saved ^^")
    else: # if user answer not yes, abort changes
        print("aborted save")
        pass
    pass

def UpdateItem(templist): # updaye item quantity and/or price
    prt_no = input("Enter Part No to edit:  ")
    # looping through the list, to find the prt no entered
    printList =[]
    for item in templist:
        if prt_no==item[0]: # if prt no found
            printList.append(item)
            print(tabulate(printList,
                           headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price"],
                           tablefmt='psql'))
            update = input(" Enter Quantity to be updated (-/+): ")
            item[4]= int(item[4]) + int(update) # update quantity attribute in the list
            answer = input("Do You Want To Update The Price? (Y/N)")
            if answer in ["y","Y"]: # if the user wants to update the price
                newPrice = input("Enter New Price: ")
                item[5] = newPrice
            else: print("saving quantity changes")
    with open("inventory.csv", 'w', newline="") as CSV: # save changes to the file.
        writer = csv.writer(CSV, delimiter=',')
        writer.writerows(templist)
        print("Updates Saved ^^")
    pass

def RemoveItem(templist): # remove an item from the list
    prt_no = input("Enter Part No to edit:  ")
    for item in templist: # search for the part number
        if prt_no == item[0]:
            templist.remove(item) # Remove the item from the list
            print(item)
            answer = input("Remove and Save? (Y/N) ") # validate with the user
            if answer in ["y","Y"]:
                with open("inventory.csv", 'w', newline="") as CSV: # save cahnges to the file
                    writer = csv.writer(CSV, delimiter=',')
                    writer.writerows(templist)
                    print("Saved ^^")
    pass

def AddTotalPriceColumn(tempList): # add total price column to the table and calculate values ( price * Quantity)
    for item in tempList:
        item[5]= format(float(item[5]),".2f")
        total_price = int(item[4])*float(item[5])
        item.append(format(total_price,".2f"))
    return  tempList

def ListInventoryItems(tempList): # print inventory table
    tempList.pop(0)
    tempList= AddTotalPriceColumn(tempList)
    # tabulate formats values into a well dsigned table
    print(tabulate(tempList,
                   headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price", "Total Price"],
                   tablefmt='psql'))
    pass

def Re_Order_List(tempList):
    tempList.pop(0)
    reOrderList = [] # temp list to store items with quantity < 4
    for item in tempList:
        if int(item[4]) < 4: # if quantity is less than 4
            reOrderList.append(item) # append the item to the Re-Order list
    # print the Re-Order list
    print(tabulate(reOrderList,
                   headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price"],
                   tablefmt='psql'))
    pass

def ItemPriceThreshhold(tempList):
    tempList.pop(0)
# gets price from the user
    threshHold = input("Please Enter ThreshHold Price: ")
    ThreshHoldList = []
    for item in tempList:
        # if item price greater than threshhold price
        if float(item[5])>float(threshHold):
            # append it to the items list
            ThreshHoldList.append(item)
    # print list of items with price less than user input
    print(tabulate(ThreshHoldList,
                   headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price"],
                   tablefmt='psql'))
    pass

def FindAverage(tempList): # find average of prices
    # control variables
    count = 0
    average = 0
    sum = 0
    for item in tempList:
        count = count + 1 # counting item numbers
        sum = sum + float(item[5]) # calculating price sum
    average = sum / count
    average = format(average, ".2f") # format average to 2 decimal points
    return average

def ItemsGreaterThanAverage(tempList):
    tempList.pop(0)
    average = FindAverage(tempList) # get the average
    averageList =[] # temp list to hold items above average price
    for item in tempList:
        # search the list/ compare price to the average. if greater, add to the list
        if float(item[5])> float(average):
            averageList.append(item)
    # print list of items with greater than average price
    print(tabulate(averageList,
                   headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price"],
                   tablefmt='psql'))
    pass

def TotalInventoryPrice(tempList): # obtain total sum of all total prices. sum of ( Quantity*Price )
    tempList = AddTotalPriceColumn(tempList) # make sure program is using the list with total price column
    price = 0
    for item in tempList:
        price = price + float(item[6]) # calculate sum per item total price
    price = format(price, ".2f") # format to two decimal points
    return price

def FindLeastQuantity(tempList): # find the item with least quantity
    i = tempList[1][4] # get an item quantity for comparison basis ( initial minimum )
    minItem = None # control variable
    for item in tempList:
        if int(item[4])<int(i): # if item quantity less than the initial minimum
            minItem = item # get items details
            i = int(item[4]) # update minimum quantity
    minItem.pop(6) # remove total from the table
    minItem.append("Least Quantity Item") # mark item with status for function 8
    return minItem

def FindMinPrice(tempList):
    i = tempList[1][5] # initial minimum price
    minItem = None
    for item in tempList:
        # if item price less than initial minimum
        if float(item[5])<float(i):
            i = item[5] # update initial minimum
            minItem =item # store items data
    minItem.pop(6) # remove total price column form the table
    minItem.append("Min Price Item") # mark the row with status
    return minItem

def FindMaxPrice(tempList):
    i = tempList[1][5] # initial maximum value
    maxItem = None
    for item in tempList:
        # if item value greater than initial max
        if float(item[5]) >float(i):
            i = item[5] # update i
            maxItem = item # strore item data
    maxItem.pop(6) # remove total price column
    maxItem.append("Max Price item ") # mark row with the status
    return maxItem

def GetStatistics(tempList):
    tempList.pop(0)
    average =FindAverage(tempList) # call average function and obtain average
    StockValue = TotalInventoryPrice(tempList) # call total inventory function and obtain total stock value
    minQuantityItem = FindLeastQuantity(tempList) # find the item with least quantity
    minPriceItem = FindMinPrice(tempList) # find the item with minimum price
    maxPriceItem = FindMaxPrice(tempList) # find the item with maximum price
    statisticsList = [maxPriceItem,minPriceItem,minQuantityItem] # append reults to a list to for tabulate function
    print(f"The Average Price is : {average}") # using F-String to print the average
    print(f"The Total Stock Value Is : {StockValue}") # using F-String to print stock value
    # Format statistical items into a table
    print(tabulate(statisticsList,
                   headers=["PartNo", "PartName", "Make", "Model", "Quantity", "Price", "Status"],
                   tablefmt='psql'))
    pass

with open("inventory.csv", 'r') as CSV: # opens inventory in read mode
    data = csv.reader(CSV, delimiter=',') # using CSV reader.
    tempList = []
    for row in data: # reading data and storing them in a 2d list
        tempList.append(row)
    Exit= True #exit Flag
    while(Exit):
        # Display menu
        print("****Inventory Control System****")
        print("[1] Add Part")
        print("[2] Update Part")
        print("[3] Remove Part")
        print("[4] Display Inventory")
        print("[5] Display Re-Order List")
        print("[6] Parts Above Given Price")
        print("[7] Parts Above The Average Price")
        print("[8] Stock Statistics")
        print("[9] Add Part")
        choice = input("Enter Function Number: ")
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("invalid choice type again")
            continue
        elif choice == "1":
            AddItem(tempList)
        elif choice == "2":
            UpdateItem(tempList)
        elif choice == "3":
            RemoveItem(tempList)
        elif choice == "4":
            ListInventoryItems(tempList)
        elif choice == "5":
            Re_Order_List(tempList)
        elif choice == "6":
            ItemPriceThreshhold(tempList)
        elif choice == "7":
            ItemsGreaterThanAverage(tempList)
        elif choice == "8":
            GetStatistics(tempList)
        else:
            Exit= False
