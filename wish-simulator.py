import random
import statistics
import matplotlib.pyplot as plt

def sim_character_pulls(num_five_star, num_four_stars):
    four_star_pity = 1
    five_star_pity = 1
    wish_count = 0

    four_star_guarantee = False
    five_star_guarantee = False
    five_stars_pulled = 0
    four_stars_pulled = [0, 0, 0]

    while five_stars_pulled < num_five_star or four_stars_pulled[0] < num_four_stars[0] or four_stars_pulled[1] < num_four_stars[1] or four_stars_pulled[2] < num_four_stars[2]:
        wish_count += 1

        # five star hard pity
        if five_star_pity == 90:
            if five_star_guarantee or random.randint(1, 2) == 1:
                five_stars_pulled += 1
                five_star_guarantee = False
            else:
                five_star_guarantee = True
            five_star_pity = 1
            four_star_pity +=1
            continue
        # four star hard pity
        elif four_star_pity >= 10:
            # hit banner four star
            if four_star_guarantee or random.randint(1, 2) == 1:
                four_stars_pulled[random.randint(1, 3) - 1] += 1
                four_star_guarantee = False
            # missed banner four stars
            else:
                four_star_guarantee = True
            five_star_pity += 1
            four_star_pity = 1
            continue
        five_star_chance = 0.006 + 0.06 * (five_star_pity - 73) if five_star_pity > 73 else 0.006
        four_star_chance = 0.565 if four_star_pity == 9 else 0.051

        # pulled five star
        if random.random() <= five_star_chance:
            if five_star_guarantee or random.randint(1, 2) == 1:
                five_stars_pulled += 1
                five_star_guarantee = False
            else:
                five_star_guarantee = True
            five_star_pity = 1
            four_star_pity += 1
        # pulled four star
        elif random.random() <= four_star_chance:
            # hit banner four star
            if four_star_guarantee or random.randint(1, 2) == 1:
                four_stars_pulled[random.randint(1, 3) - 1] += 1
                four_star_guarantee = False
            # missed banner four stars
            else:
                four_star_guarantee = True
            five_star_pity += 1
            four_star_pity = 1
        # three star
        else:
            five_star_pity += 1
            four_star_pity += 1

    return wish_count


if __name__ == '__main__':
    while True:
        num_trials = 10000
        wish_counts = []

        # get user input
        while True:
            num_five_stars = input("Number of banner 5-star wanted: ")
            try:
                num_five_stars = int(num_five_stars)
                break
            except ValueError:
                print("Please enter an integer")

        while True:
            num_four_star_1 = input("Number of first banner 4-star wanted: ")
            try:
                num_four_star_1 = int(num_four_star_1)
                break
            except ValueError:
                print("Please enter an integer")

        while True:
            num_four_star_2 = input("Number of second banner 4-star wanted: ")
            try:
                num_four_star_2 = int(num_four_star_2)
                break
            except ValueError:
                print("Please enter an integer")

        while True:
            num_four_star_3 = input("Number of third banner 4-star wanted: ")
            try:
                num_four_star_3 = int(num_four_star_3)
                break
            except ValueError:
                print("Please enter an integer")

        for i in range(num_trials):
            wish_counts.append(sim_character_pulls(num_five_stars, [num_four_star_1, num_four_star_2, num_four_star_3]))

        wish_counts.sort()

        # create a plot modeling the distribution given user parameters
        plt.plot(wish_counts, [i/num_trials for i in range(num_trials)])
        plt.title("Distribution of {} 5-stars and [{}, {}, {}] 4-stars".format(
            num_five_stars, num_four_star_1, num_four_star_2, num_four_star_3))
        plt.xlabel("Number of Pulls")
        plt.ylabel("Chance within Number of Pulls")
        plt.show()

        # create a histogram modelling the distribution
        plt.hist(wish_counts, bins=90, histtype="stepfilled", density=True)
        plt.title("Histogram of {} 5-stars and [{}, {}, {}] 4-stars".format(
            num_five_stars, num_four_star_1, num_four_star_2, num_four_star_3))
        plt.xlabel("Number of Pulls")
        plt.ylabel("Frequency")
        plt.show()

        # print quick info on statistics
        print("Mean pulls: {}".format(sum(wish_counts)/num_trials))
        print("Median pulls: {}".format(statistics.median(wish_counts)))
        print("Mode pulls: {}".format(statistics.mode(wish_counts)))
        print("----------------------------------------")
        print("10% chance within {} wishes".format(wish_counts[num_trials // 10]))
        print("25% chance within {} wishes".format(wish_counts[num_trials // 4]))
        print("50% chance within {} wishes".format(wish_counts[num_trials // 2]))
        print("75% chance within {} wishes".format(wish_counts[num_trials * 3 // 4]))
        print("90% chance within {} wishes".format(wish_counts[num_trials * 9 // 10]))
        print("----------------------------------------")
        print("Min pulls: {}".format(min(wish_counts)))
        print("Max pulls: {}".format(max(wish_counts)))
        print("\n")