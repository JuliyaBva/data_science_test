from random import randint

def frequency_of_dice_rolls(n, m, s):

    random_dice_rolls = []
    while len(random_dice_rolls) < n:
        random_dice_rolls.append(randint(1, 6))
    print(f"\nRandom dice rolls: {random_dice_rolls}")

    values = [x for x in random_dice_rolls if x >= s]
    print(f"Values not less than s: {values}")

    frequency = {}
    for i in values:
        if i in frequency:
            continue
        else:
            frequency[i] = values.count(i)
    print(f"Frequency: {frequency}")
    
    frequency_m_sum = sum([value for value in frequency.values() if value == m])
    print(f"General amount: {frequency_m_sum}\n")
   
    probability = round(frequency_m_sum / n, 2)

    print(f"Probability: {probability}\n") # other values were printed to simplify result analysis


frequency_of_dice_rolls(17, 2, 2)