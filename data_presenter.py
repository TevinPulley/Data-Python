# import math 
# open_file = open ("CupcakeInvoices.csv")

# total = 0

# for line in open_file:
    #1.print all data
    # print(line)

    #2.print cupcakes
    #values = line.split(',')
    #print(values[2])

    #3.loop through and print the total for each invoice
    # values = line.split(',')
    # total = int(values[3]) * float(values[4])
    # print(total)

    #4. print out total for all invoices combined. (this one was kind of tricky. i had to take a peak at the solutions to be honest)
    # values = line.split(',')
    # total = total + (int(values[3]) * float(values[4]))

    # print(total)
    #5. close your open file
    # open_file.close()

    #Going Further 
choclate_c = 0
vanilla_c = 0
strawberry_c = 0 

open_file = open("CupcakeInvoices.csv")

for line in open_file:
    values = line.split(',')
    if values[2] == "Chocolate":
        total = int(values[3]) * float(values[4])
        choclate_c += total
        
open_file.close()

open_file = open("CupcakeInvoices.csv")

for line in open_file:
    values = line.split(',')
    if values[2] == "Vanilla":
        total = int(values[3]) * float(values[4])
        vanilla_c += total
        
open_file.close()

open_file = open("CupcakeInvoices.csv")

for line in open_file:
    values = line.split(',')
    if values[2] == "Strawberry":
        total = int(values[3]) * float(values[4])
        strawberry_c += total
        
 
open_file.close()

print(strawberry_c, choclate_c, vanilla_c)

###### I was trying to get these to come out as a single response down below. i couldn't figure it out nor find help for it. 
######### I would still like to know how to do this so if you see this please reach out to me!
# for line in open_file:
#     values = line.split(',')
#     if values[2] == "Strawberry":
#         total = int(values[3]) * float(values[4])
#         strawberry_c += total
        
#         print(max in range(strawberry_c))
# open_file.close()

# strawberry_totals = []

# for line in open_file:
#     values = line.split(',')
#     if values[2] == "Strawberry":
#         total = int(values[3]) * float(values[4])
#         strawberry_c += total
#         strawberry_totals.append(strawberry_c)
#         print(sum(strawberry_totals))
# open_file.close()
  