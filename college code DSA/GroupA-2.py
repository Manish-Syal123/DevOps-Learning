# List of tuples representing students, where each tuple contains the student's name, marks scored, and attendance status
students = [("Alice", 80, "present"), ("Bob", 75, "present"), ("Charlie", 90, "present"), ("Dave", 50, "absent"), ("Eve", 65, "present")]

def average_score():
  # Calculate the sum of the marks scored by all students
  #total_marks = sum(mark for _, mark, _ in students)
  total_marks=0
  for tup in students:
      total_marks+=tup[1]

  # Calculate the number of students
  num_students = len(students)
  
  # Calculate the average score
  avg_score = total_marks / num_students
  
  return avg_score

def highest_lowest_scores():
  # Initialize variables to track the highest and lowest scores
  highest_score = 0
  lowest_score = 100
  
  # Iterate through the list of tuples to find the highest and lowest scores
  for _, mark, _ in students:
    if mark > highest_score:
      highest_score = mark
    if mark < lowest_score:
      lowest_score = mark
  
  return highest_score, lowest_score

def count_absentees():
  # Initialize a counter for the number of absentees
  num_absentees = 0
  
  # Iterate through the list of tuples to count the number of absentees
  for _, _, attendance in students:
    if attendance == "absent":
      num_absentees += 1
  
  return num_absentees

def highest_frequency_mark():
  # Create a dictionary with the marks as keys and the number of occurrences as values
  mark_counts = {}
  for _, mark, _ in students:
    if mark not in mark_counts:
      mark_counts[mark] = 1
    else:
      mark_counts[mark] += 1
  
  # Find the mark with the highest frequency
  highest_frequency = 0
  highest_frequency_mark = None
  for mark, count in mark_counts.items():
    if count > highest_frequency:
      highest_frequency = count
      highest_frequency_mark = mark
  
  return highest_frequency_mark

# Test the functions
print(average_score())
print(highest_lowest_scores())
print(count_absentees())
print(highest_frequency_mark())
