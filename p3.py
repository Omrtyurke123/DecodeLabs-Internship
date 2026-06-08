# user_catigory = int(input(' 1 : Sci-Fi \n 2 : Thriller \n 3 : Drama \n 4 :Drama\n chose your like catigory :  '))
user_likes = input(' write your like : ').split()
# print(user_likes)
like = user_likes
data = {
    "Thriller":['Island','Se7en'],
    "Drama":[' Redemption','Godfather'],
    "Action":['FuryRoad','TheDarkKnight']
}
score={
    "Thriller":0,
    "Drama":0,
    "Action":0
}
for catigory in data:
    # print(catigory)
    for move in like:
        # print(move)
        if move in data[catigory]:
            score[catigory]+=1
            
# print(score)
best_category = max(score, key=score.get)

print("Recommended Category:", best_category)
