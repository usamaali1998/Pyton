#Match case statement (switch) : An alternativ to suing many "elif" statements
#       execute some code if a value matches a  "case"
#       benefits : cleaner and syntax more readable


def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "Its a monday"
        case 3:
            return "its a tuesday"
        case 4:
            return "its a wednesday"
        case 5:
            return "its a thursday"
        case 6:
            return "its a friday"
        case 7:
            return "Its a saturday"
        case _:
            return "not a valid day"
print(day_of_week(12))