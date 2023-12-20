swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100:
    print("Well done - Provincial Colours!")
elif 100 < total_time <= 105:
    print("Well done - Provincial Half Colours!")
elif 105 < total_time <= 110:
    print("Well done - Provincial Scroll!")
else:
    print("No award - Keep training!")

print(f"Total time taken: {total_time} minutes")
