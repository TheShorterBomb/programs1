def letter_grade(percent):
    if percent >= 97:
        return 'A+'
    elif percent > 93:
        return 'A'
    elif percent > 90:
        return 'A-'
    elif percent >= 87:
        return 'B+'
    elif percent > 83:
        return 'B'
    elif percent > 80:
        return 'B-'
    elif percent >= 77:
        return 'C+'
    elif percent > 73:
        return 'C'
    elif percent > 70:
        return 'C-'
    elif percent >= 67:
        return 'D+'
    elif percent > 63:
        return 'D'
    elif percent > 60:
        return 'D-'
    else:
        return 'F'


print(letter_grade(int(input())))
