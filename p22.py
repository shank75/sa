import heapq

def find_max_min_marks(marks):
    max_heap = []
    min_heap = []

    # Construct max heap and min heap
    for mark in marks:
        heapq.heappush(max_heap, -mark)  # Use negative to create max heap
        heapq.heappush(min_heap, mark)

    # Maximum marks is the negative of the root of max heap
    max_marks = -heapq.heappop(max_heap)
    # Minimum marks is the root of min heap
    min_marks = heapq.heappop(min_heap)

    return max_marks, min_marks

# Take input from the user
marks = []
num_students = int(input("Enter the number of students: "))
print("Enter the marks obtained by each student:")
for i in range(num_students):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

# Find maximum and minimum marks
max_marks, min_marks = find_max_min_marks(marks)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)
