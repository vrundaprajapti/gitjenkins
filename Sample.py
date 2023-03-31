simport random

rank= ["Ace", 2, 3, 4, 5, 6, 7 , 8, 9,10,"Jack","Queen","King"]
suit=["Clubs" , "Diamonds", "Heart","Spades"]

rankop=random.choice(rank)
suitop= random.choice(suit)

#print("The card picked was " +str(rankop)+ " of " + suitop )

guess_rank=input("Guess rank : ")
guess_suit=input("Guess suit : ")

print("You guessed  : "+str(guess_rank)+ " of "+ guess_suit)

if str(guess_rank) == str(rankop) and guess_suit==suitop:
    print("The card picked was " +str(rankop)+ " of " + suitop )
    print(" \t\tYou guessed Correct card!!!")

elif guess_rank == rankop :
    print("The card picked was " +str(rankop)+ " of " + suitop )
    print(" \t\tYou guessed ccorrect rank.")

elif guess_suit == suitop :
    print("The card picked was " +str(rankop)+ " of " + suitop )
    print(" \t\tYou guessed correct suit.")

else:
    print("The card picked was " +str(rankop)+ " of " + suitop )
    print(" \t\tBetter luck next time.")


