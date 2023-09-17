#
import random
playerin=True
dealerin=True
#create deck of cards, player's and dealer's hand
deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
playerhand=[]
dealerhand=[]

#deal the cards
def dealcards(turn):
  card=random.choice(deck)
  turn.append(card)
  deck.remove(card)

#calculate total of each hand
def total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total      
      
#check for winner
def showdealerscards():
  if len(dealerhand)==1:
    return dealerhand[0]
  elif len(dealerhand)==2:
    return dealerhand[0],dealerhand[1]
  elif len(dealerhand)==3:
    return dealerhand[0],dealerhand[1],dealerhand[2]
  elif len(dealerhand)==4:
    return dealerhand[0],dealerhand[1],dealerhand[2],dealerhand[3]  
for _ in range(1): 
  dealcards(playerhand)
  dealcards(dealerhand)  

#game loop
while playerin or dealerin:
  
   
  print("Dealer's hand is " ,showdealerscards()," = ",total(dealerhand) )
  print("Your hand is",playerhand,"=",total(playerhand),"\n")
  if playerin :
     stayorhit=input("0 to Stay\n1 to Hit\n")
  if total(dealerhand)>16:
    dealerin=False
  else :
    if playerin==False:
      dealcards(dealerhand)
  if stayorhit=='0':
    playerin=False
  else :
    dealcards(playerhand)
  if total(playerhand)>=21:
    break
  elif total(dealerhand)>=21:
    break
if total(playerhand)==21:
  print("You have",playerhand," = 21!\nBlackJack !    \nYou Win !")
elif total(dealerhand)==21 and playerin==False :
  print("Dealer has",dealerhand," = 21!\nBlackJack !    \nDealer Wins !")
elif total(playerhand)>21:
   print("You have",playerhand,' = ',total(playerhand), "You are out !     \nDealer Wins !")
elif total(dealerhand)>21 and playerin==False:
   print(" You have",playerhand ,"=",total(playerhand),"    Dealer has",dealerhand," = " ,total(dealerhand),"Dealer's out !     \nYou Win !")
elif 21-total(dealerhand)<21-total(playerhand):
  print("You have",playerhand," = ",total(playerhand),"and Dealer has ",dealerhand,"= ",total(dealerhand),"\nDealer Wins!")
elif 21-total(dealerhand)>21-total(playerhand) or total(dealerhand)==total(playerhand) :
  print("You have",playerhand," = ",total(playerhand),"and Dealer has ",dealerhand,"= ",total(dealerhand),"\nYou Win!") 


  
  
