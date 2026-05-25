#Python Slot Game
import random

def spin_row():
    symbols=['🍉','🍈','⭐','🍒','🔔']
    # result=[]
    # for symbol in range(3):
    #     result.append(random.choice(symbols))
    # return result
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print(" ".join(row))

def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍉":
            return bet*2
        elif row[0]=="🍈":
            return bet*3
        elif row[0]=="⭐":
            return bet*4
        elif row[0]=="🍒":
            return bet*5
        elif row[0]=="🔔":
            return bet*10
    return 0

balance=100
print("-----------------------")
print("PYTHON SLOTS")
print("SYMBOLS- 🍉🍈⭐🍒🔔")
print("-----------------------")

while balance>0:
    bet=int(input("Enter the amount you would like to bet :"))
   
    if bet<=0:
        print("your bet should be greater than 0")
        continue
    
    if bet>balance:
        print("Insufucient Funds")
        continue
    balance-=bet
    row=spin_row()
    print_row(row)

    if payout(row,bet)>0:
        print(f"You won ₹{payout(row,bet)}")
        balance+=payout(row,bet)
    else:
        print("You lost this round")

    print(f"So finally, your balance = ₹{balance}")

print("Please top up some money to bet more")