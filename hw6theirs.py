# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
print ''
vcount = 0
ccount = 0

vowel = ('a', 'A', 'E', 'I', 'O', 'U', 'e', 'i', 'o', 'u')
str1 = "Python Is A Great Programming Language!"

for i in str1:
    if i in vowel:
        vcount += 1
        ccount = len("Python Is A Great Programming Language!") - vcount



print 'vowel count:',vcount,'consonant count:', ccount

print 'Total len:', len("Python Is A Great Programming Language!")
print ''


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
print ''
list = [1, 2.2, 3, 4.2]
average = 0
for i in list:
    print i
    average = sum(list)/len(list)
print 'Average:', average

print ''
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

list2 = [5.2, 6.8, 7.5]

list1 = [1, 2.2, 3, 4.2]

list1.append(list2)

average = 0



###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"




###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
