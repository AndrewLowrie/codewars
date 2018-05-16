# Create a combat function that takes the
# player's current health and the amount
# of damage recieved, and returns the player's
# new health. Health can't be less than 0.

def combat(health, damage):
    if (health - damage) <= 0:
        return 0
    else:
        return (health - damage)


print(combat(100, 5)) # 95)
print(combat(83, 16)) # 67)
print(combat(20, 30)) # 0)
