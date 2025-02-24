def timeGrouping(outputDir, input_time):
    """
    Groups input time data based on a threshold (20 seconds) and writes the groups to a file.
    
    Args:
        outputDir (str): The directory where the output file will be saved.
        input_time (list): List of time values to be grouped.
    
    Returns:
        None: This function writes to a file and does not return anything.
    """

    # Define the path to the output file where grouped times will be saved.
    output_file = f'{outputDir}\\grouping.txt'

    # Initialize the list that will store all the time groups.
    all_groups = []
    
    # Start the first group with the first time in the input list.
    current_group = [input_time[0]]
    a = input_time[0]  # Store the first time for comparison.

    # Iterate through the rest of the input time list to group times based on a threshold.
    for i in range(1, len(input_time)):
        # If the difference between the current time and the last time is less than or equal to 20 seconds,
        # add the time to the current group.
        if input_time[i] - a <= 20:
            current_group.append(input_time[i])
        else:
            # If the difference is greater than 20 seconds, finalize the current group and start a new one.
            all_groups.append(current_group)
            current_group = [input_time[i]]  # Start a new group with the current time.
            a = input_time[i]  # Update the last time for comparison.

    # After finishing the loop, append the final group.
    all_groups.append(current_group)

    # Open the output file in append mode to write the groups.
    with open(output_file, "a") as file:
        # For each group, print it to the console and write it to the file.
        for index, group in enumerate(all_groups):
            print(f'Group-{index}: {group}')  # Print the group to the console for feedback.
            file.write(f'{group}\n')  # Write the group to the file.
