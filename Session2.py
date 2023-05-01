name = input("Enter name :")
family = input ("Enter family :")

score1 = float (input ("Enter score lesson one :"))
score2 = float (input ("Enter score lesson two :"))
score3 = float (input ("Enter score lesson three :"))

average = (score1+score2+score3)/3
if average>=17: 
    print("Great")

elif 12<=average<17:
    print("Normal")

elif average<12:
    print( "Fail" )
print("my name is", name,"family",family,"average is :" ,average)


