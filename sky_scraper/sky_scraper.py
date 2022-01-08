"""
Pseudocode

let height = input
let stacks = height divided by 5
let weeks = 0

while stacks does not equal 1:
    if stacks is even:
        stacks = stacks divided by two
        interation(week) plus one
    else:
        stacks = stacks divided by two
        interation(week) plus two because there needs to be extra time to add in the extra remainder stack in the end of the build
    end if
end while

output interation(week)


"""



height = int(input("What is the height: "))
stacks = height/5
weeks = 0

while stacks != 1:
    if stacks % 2 == 0:
        stacks = stacks // 2
        weeks += 1
    else:
        stacks = stacks // 2
        weeks += 2

print(weeks)
