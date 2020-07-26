Subsetting rows
A large part of data science is about finding which bits of your dataset are interesting. One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as filtering rows or selecting rows.

There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.

dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
You can filter for multiple conditions at once by using the "logical and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["col_b"] == "tan")]
homelessness is available and pandas is loaded as pd.

Instructions 1/3
35 XP
Instructions 1/3
35 XP
1
Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.

Take Hint (-10 XP)
2
Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.

3
Filter homelessness for cases where the number of family members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result