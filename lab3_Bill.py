# Bill Kamau | Lab 3 | Intro to Python


# Ticket 1
# PREDICT: 13
# DO: Make a username and print its length.

Bkamau = "looplearner21"
print(len(Bkamau))

# EXPLAIN: Yes, len() counts every character in the string, including letters and numbers.


# Ticket 2
# PREDICT: The first character will be l and the last character will be 1.
# DO: Print the first and last characters using len() to find the last index.

print(Bkamau[0])
print(Bkamau[len(Bkamau) - 1])

# EXPLAIN: The last index is len(username) - 1 because indexes start counting at 0, so the length is one greater than the last index.


# Ticket 3
# PREDICT: Yes, both lines will look identical on the screen.
# DO: Build the welcome banner using concatenation and an f-string.

print("Welcome to Loop, @" + Bkamau + "!")
print(f"Welcome to Loop, @{Bkamau}!")

# EXPLAIN: The f-string felt easier to me because I can put the variable directly inside the sentence without using multiple plus signs.


# Ticket 4
# PREDICT: I think Python will give an error because I am trying to change one character inside a string.
# DO: This breaks on purpose.

try:
    Bkamau[0] = "X"  # run this, it breaks on purpose
except TypeError as error:
    print(error)

# ERROR: TypeError: 'str' object does not support item assignment

# Now make the whole username uppercase.
print(Bkamau.upper())

# EXPLAIN: Immutable means that a string cannot have one of its individual characters changed after the string has been created.


# Ticket 5
# PREDICT: 3 will print for the count, and "Oldest post" will print first.
# DO: Create a feed list with three captions.

feed = [
    "Oldest post",
    "First day at Loop",
    "Learning lists today"
]

print(len(feed))
print(feed[0])

# EXPLAIN: I used index 0 because the first item in a Python list is always at index 0.


# Ticket 6
# PREDICT: The new fourth post will have index 3.
# DO: Add a fourth caption using append().

feed.append("Python practice is fun")
print(feed)

# EXPLAIN: The fourth post is at index 3 because Python starts counting indexes at 0, making the four indexes 0, 1, 2, and 3.


# Ticket 7
# PREDICT: "Oldest post" will be removed, and the remaining posts will be in alphabetical order.
# DO: Remove the first post and sort the remaining posts.

feed.pop(0)
feed.sort()
print(feed)

# EXPLAIN: I used pop(0) to remove the first post and sort() to arrange the remaining posts alphabetically.


# Ticket 8
# PREDICT: 200 will print for the follower count, and profile[0] will cause a KeyError because 0 is not a key in the dictionary.
# DO: Create the profile dictionary.

profile = {
    "username": Bkamau,
    "followers": 200,
    "verified": True
}

print(profile["followers"])

# This breaks on purpose.
try:
    print(profile[0])  # run this, it breaks on purpose
except KeyError as error:
    print(error)

# ERROR: KeyError: 0

# EXPLAIN: Dictionaries look up values by key name because dictionaries store information as key-value pairs rather than numbered positions.


# Ticket 9
# PREDICT: .get("age") will print None because the "age" key does not exist.
# DO: Add 50 followers and add a bio.

profile["followers"] = profile["followers"] + 50
profile["bio"] = "Learning Python and building cool projects."

print(profile)

print(profile.get("age"))

# EXPLAIN: .get() is safer because it returns None when a key is missing instead of causing an error like profile["age"] would.


# Ticket 10
# PREDICT: @looplearner21 has 250 followers and 3 posts. Top post: First day at Loop
# DO: Use one f-string with information from both the dictionary and the feed list.

print(
    f"@{profile['username']} has {profile['followers']} followers "
    f"and {len(feed)} posts. Top post: {feed[0]}"
)

# EXPLAIN: I used a dictionary (profile), a list (feed), and strings and numbers stored inside those data structures to build the summary.