from pyspark.sql import SparkSession

import numpy as np

from pyspark.sql import *

import matplotlib.pyplot as plt

logFile = "facebook_combined.txt"  # Should be some file on your system

spark = SparkSession.builder.appName("Mutual Friends").getOrCreate()

logData = spark.read.text(logFile)

friendsList =[]

singleUser = []

i = 0

Friends_df = Row("User1", "User2")

friendList_df= []

for item in logData.collect():

#    print "Friends", item[0]

    friendsList.append(item[0])

    tempUser = friendsList[i].split()

    singleUser.append(tempUser)

    for j in range(2):

        singleUser[i][j] = singleUser[i][j].encode("ascii")

#        print "Users of row" , i, ": ", singleUser[i][j]

    friendList_df.append(Friends_df(singleUser[i][0], singleUser[i][1]))

    i +=1

 

singleUser1= np.array(singleUser)

singleUser1 = singleUser1.flatten()

#print (singleUser)

allUsers= []

for item in singleUser1:

    if item not in allUsers:

        allUsers.append(item)

#dframe = pd.DataFrame(colums = ['user', 'Friends'])     

#print allUsers

frndsOfSingleUserInSepRows = []

frndsOfAllUsers = []

#print "FKLK" , allUsers[0]

j = 0

for user in allUsers:

    frndsOfSingleUserInSepRows = []

    for i in range(logData.count()):

        if user == singleUser[i][0]:

            frndsOfSingleUserInSepRows.append(singleUser[i][1])

        if user == singleUser[i][1]:

            frndsOfSingleUserInSepRows.append(singleUser[i][0])

#    print "user: ", user, frndsOfSingleUserInSepRows

    frndsOfAllUsers.append(frndsOfSingleUserInSepRows)

    frndsOfSingleUserInSepRows = [0 for i in range(len(frndsOfSingleUserInSepRows))]

#print "--------------------------------------------------------"

#print "--------------------------------------------------------"

   

#print frndsOfAllUsers

i = 0

arr = []

mutualFriendCountArray = []

mutualCountsAllFriendsPerUSer = []

lenOfMFrnds =[]

for user in allUsers:

    mutualFriendCountArray = []

    for eachItem in frndsOfAllUsers[i]:  #First data to comapre for mutual frnd

#            print eachItem

            val = allUsers.index(eachItem) #place where user in present

            arr = frndsOfAllUsers[val] # sec array to compare mutual friends

            tempArr = set(frndsOfAllUsers[i])

            tempArr.intersection_update(frndsOfAllUsers[val])

#            tempArr = list(tempArr)

#            print "Input Array1" , frndsOfAllUsers[i]

#            print "Input Array2", frndsOfAllUsers[val]

#            print "MuTUAL array" , list(tempArr)

            mutualFriendCountArray.append(len(tempArr))

    print "Number of Mutual friends: ", user, mutualFriendCountArray

    mutualCountsAllFriendsPerUSer.append(mutualFriendCountArray)

    mutualFriendCountArray =  [0 for l in range(len(mutualFriendCountArray))]

    tempArr = [0 for k in range(len(tempArr))]

    i+=1

print "--------------------------------------------------------"

print "--------------------------------------------------------"

 

#print mutualCountsAllFriendsPerUSer

maxMutualFriendPerUser = []

for eachUser in mutualCountsAllFriendsPerUSer:

    eachUser = np.array(eachUser)

    maxMutualFriendPerUser.append(eachUser.max())
#for printing max mutual friends   

#b=0

#for user in allUsers:

#    print "Max number of mutual friends for user:", user,"is ", maxMutualFriendPerUser[b]

#    b+=1

plt.title("Histogram Plot for Maximum Mutual Friends")

plt.xlabel("Maximum Mutual Friends")  

plt.ylabel("Frequency")

xLabel = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

yLabel = [50, 100, 150, 200, 250, 300, 350, 400]

plt.gca().set_xticklabels(xLabel)

plt.gca().set_yticklabels(yLabel)

plt.hist(maxMutualFriendPerUser, bins=30)              
