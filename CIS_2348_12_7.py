# Joshua Chan
# 1588459

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    print('Fat burning heart rate for a ' + str(age) + ' year-old: ' + str(heart_rate) + ' bpm')
# The code above will calculate the necessary bpm according to age
def get_age():
    age = int(input())
    if age > 75 or age < 18:
        raise ValueError('Invalid age.')
    return age
# The function above will take the user input for age and if it meets the criteria, will raise the error or pass
if __name__ == '__main__':
    try:
        age = get_age()
        fat_burning_heart_rate(age)
# If the age is accepted, the function fat_burning_heart_rate will proceed
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
# The code above is for when the age is not applicable
