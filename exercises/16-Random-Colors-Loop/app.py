import random
# que significa =4
def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    # ✅ ↓ your loop here ↓ ✅
    for i in range(10):
        num_random = random.randint(0,3)
        color_random = get_color(num_random)
        students_array.append(color_random)
    return students_array

print(get_allStudentColors())
