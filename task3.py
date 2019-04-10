# #    This program is free software: you can redistribute it and/or modify
# #    it under the terms of the GNU General Public License as published by
# #    the Free Software Foundation, either version 3 of the License, or
# #    (at your option) any later version.

# #    This program is distributed in the hope that it will be useful,
# #    but WITHOUT ANY WARRANTY; without even the implied warranty of
# #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# #    GNU General Public License for more details.

# #    You should have received a copy of the GNU General Public License
# #    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# # 2019 May/June Prerelease Material.
# # Solved by Sadman Tariq
# # https://github.com/SadmanTariq/2019PrereleaseWithSolution

print("This solution is created by Sadman Tariq.")
print("https://github.com/SadmanTariq/2019PrereleaseWithSolution \n")

# ------TASK 1------

temp_cond = True  # Temporary placeholder
while temp_cond:
    try:
        numItems = int(input("Enter amount of items to be put on aution " +
                             "(atleast 10): "))
        if numItems >= 10:
            temp_cond = False
    except ValueError:
        print("\nCan only be numbers.")

# Lists containing different properties of auction items.
# Dictionary would have worked better but O' Level restrictions.
ItmNumList = []
ItmDescList = []
ReservePriceList = []
NumBidsList = []       # List containing number of bids for each item
BidList = []           # List containing highest bid for each item
BuyerNumList = []      # List containing buyer number of highest bidders
SoldList = []          # List containing whether each item is sold or not

# Getting input.
for i in range(numItems):
    cond = True
    while cond:
        num = input("Enter item number: ")
        if num not in ItmNumList:
            ItmNumList.append(num)
            cond = False
        else:
            print("Item number needs to be unique.")

    ItmDescList.append(input("Enter item description: "))
    ReservePriceList.append(int(input("Enter reserve price: $")))
    NumBidsList.append(0)
    BidList.append(0)
    BuyerNumList.append("")
    SoldList.append(False)

# ------TASK 2------

# Print all the available items for selection using Item Number.
print("Available items:")
for i in range(numItems):
    print(ItmNumList[i], ItmDescList[i], sep=": ")

WantToBid = True  # When false; break out of loop.
while WantToBid:
    choice = input("Do you want to place a bid? (y/n): ")
    if choice == 'n':
        WantToBid = False

    elif choice == 'y':
        SelectedItem = ''  # Holds item number of selected item.
        BidAmount = 0
        BuyerNumber = ''

        correct = False  # True if selected item is available.
        while not correct:
            SelectedItem = input("Enter item number from above: ")
            if SelectedItem in ItmNumList:
                # Index of item from list.
                list_index = ItmNumList.index(SelectedItem)

                print()
                print(SelectedItem, ItmDescList[list_index])
                print("Highest bid: $" + str(BidList[list_index]))

                correct = True
            else:
                print("Invalid item number; try again.")

        correct = False  # Bid is correct.
        while not correct:
            BidAmount = int(input("Enter your bid: $"))
            if BidAmount > BidList[ItmNumList.index(SelectedItem)]:
                correct = True
            else:
                print("Bid amount must be higher than previous bid.")

        BuyerNumber = input("Enter buyer number: ")
        list_index = ItmNumList.index(SelectedItem)

        BidList[list_index] = BidAmount
        BuyerNumList[list_index] = BuyerNumber
        NumBidsList[list_index] += 1

# ------TASK 3------
TotalFee = 0.0
LessThanReservePrice = []
NoBids = []  # Items with no bids.

for i in range(numItems):
    if BidList[i] >= ReservePriceList[i]:  # Sold?
        SoldList[i] = True
        TotalFee += BidList[i] * 0.1  # Fee is 10% of bid.
    else:
        LessThanReservePrice.append(ItmNumList[i])
    if NumBidsList[i] == 0:  # No bids?
        NoBids.append(ItmNumList[i])


# Printing information.
print("\n------------------------")
print("Total fee: " + str(TotalFee))
print("Items sold: " + str(numItems - len(LessThanReservePrice)))

print("\nThe {0} items that have not".format(len(LessThanReservePrice)),
      "reached their reserved price are:")
for x in LessThanReservePrice:
    print(x, " Highest bid: $", BidList[ItmNumList.index(x)], sep='')

print("\nThe {0} items that have recieved no bids are:".format(len(NoBids)))
print(', '.join(NoBids))  # Print NoBids delimited with ', '

input()  # Wait before exiting.
