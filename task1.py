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
        print("Input can only be numbers.")

# Lists containing different properties of auction items.
# Dictionary would have worked better but O' Level restrictions.
ItmNumList = []
ItmDescList = []
ReservePriceList = []
NumBidsList = []       # List containing number of bids for each item

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
