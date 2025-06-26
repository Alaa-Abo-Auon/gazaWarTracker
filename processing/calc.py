import pandas as pd

# Load the Excel file
df = pd.read_excel("data/Book1.xlsx")


def total_martyr_count():
    # Specify the column name to search for
    target_column_name = "Martyr Count"

    if target_column_name in df.columns:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
        print(f"Column '{target_column_name}' not found.")
        return None


def total_injured_count():
    # Specify the column name to search for
    target_column_name = "Injured Count"

    if target_column_name in df.columns:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
        print(f"Column '{target_column_name}' not found.")
        return None


def total_martyr_injured_count():
    return total_martyr_count()+total_injured_count()


def most_damaged_region():
    target_column_name_1 = "Damaged Homes Count"
    target_column_name_2 = "Region"
    if target_column_name_1 in df.columns and target_column_name_2 in df.columns:
    #Add damaged house count for each region
        regions = df["Region"].unique()
        region_damaged_homes_count = dict.fromkeys(regions, 0)
        region = df["Region"]
        damaged_homes_count = df["Damaged Homes Count"]
        for i in range(region.count()):
            region_damaged_homes_count[region[i]] += damaged_homes_count[i]
    # then conclude that the one with the lowest
    # count is the most damaged and is most likely dangerous to live in.
        lowest_damaged_region = max(region_damaged_homes_count, key=region_damaged_homes_count.get)
        return lowest_damaged_region
    else:
        print(f"Column '{target_column_name_1}' or '{target_column_name_2}' not found.")
        return None

def least_damaged_region():
    target_column_name_1 = "Damaged Homes Count"
    target_column_name_2 = "Region"
    if target_column_name_1 in df.columns and target_column_name_2 in df.columns:
        #Add damaged house count for each region
        regions = df["Region"].unique()
        region_damaged_homes_count = dict.fromkeys(regions, 0)
        region = df["Region"]
        damaged_homes_count = df["Damaged Homes Count"]
        for i in range(region.count()):
            region_damaged_homes_count[region[i]] += damaged_homes_count[i]
        # then conclude that the one with the lowest
        # count is the least damaged and is probably the most habitable.
        lowest_damaged_region = min(region_damaged_homes_count, key=region_damaged_homes_count.get)
        return lowest_damaged_region
    else:
            print(f"Column '{target_column_name_1}' or '{target_column_name_2}' not found.")
            return None


# def most_victim_dates():
#     #Add all the martyr and injured count on a
#     # specific date.

def attack_type_count():
#     #Sum attacks of each type.
    target_column_name = "Attack Type"
    if target_column_name in df.columns:
        attack_types = df["Attack Type"].unique()
        attack_type_count = dict.fromkeys(attack_types, 0)
        attack_type = df["Attack Type"]
        for i in range(attack_type.count()):
            attack_type_count[attack_type[i]] += 1
        return attack_type_count
    else:
        print(f"Column '{target_column_name}' not found.")
        return None


def martyr_percentage_by_region(region):
    # Calculate the percentage of martyrs in a given region.
    target_column_name = "Martyr Count"
    if target_column_name in df.columns:
        total_martyrs = total_martyr_count()
        if total_martyrs == 0:
            return 0
        region_martyrs = df[df["Region"] == region][target_column_name].sum()
        return (region_martyrs / total_martyrs) * 100
    else:
        print(f"Column '{target_column_name}' not found.")
        return None
