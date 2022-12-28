def longest_word(s):
  # Split the string into a list of words
  words = s.split()
  
  # Initialize a variable to track the longest word
  longest_word = ""
  
  # Iterate through the list of words to find the longest word
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  
  return longest_word

def character_frequency(s, c):
  # Initialize a counter for the number of occurrences of the character
  count = 0
  
  # Iterate through the string to count the number of occurrences of the character
  for ch in s:
    if ch == c:
      count += 1
  
  return count

def is_palindrome(s):
  # Reverse the string
  reversed_s = s[::-1]
  
  # Compare the reversed string to the original
  return s == reversed_s

def substring_index(s, substring):
  # Find the index of the first appearance of the substring using the find() method
  index = s.find(substring)
  
  return index

def word_count(s):
  # Split the string into a list of words
  words = s.split()
  
  # Create a dictionary with the words as keys and the number of occurrences as values
  word_counts = {}
  for word in words:
    if word not in word_counts:
      word_counts[word] = 1
    else:
      word_counts[word] += 1
  
  # Display the count for each word
  for word, count in word_counts.items():
    print(f"{word}: {count}")

# Test the functions
s = "This is a test string"
print(longest_word(s))
print(character_frequency(s, "i"))
print(is_palindrome(s))
print(substring_index(s, "test"))
word_count(s)
