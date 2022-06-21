
# day_name-->weekday_name

import time
from matplotlib.style import use
import numpy as np
import pandas as pd
import time
import pandas as pd
import numpy as np

# Creating a dictionary containing the data sources for the three cities
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'
             }

# Function to figure out the filtering requirements of the user


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')

    # Initializing an empty city variable to store city choice from user
    # You will see this repeat throughout the program

    city = input(
        "Enter the city name (chicago,new york city,washington)\n").lower()

    # Running this loop to ensure the correct user input gets selected else repeat

    while city not in CITY_DATA.keys():
        print("please Enter the city name correct: ")
        city = input(
            "Enter the city name (chicago,new york city,washington)\n").lower()

    # Creating a dictionary to store all the months including the 'all' option
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while True:
        month = input(
            "Enter the month (january, february, march,april, may, june, all)").lower()
        if month in months:
            break
        else:
            print("Wrong input")

    # Creating a list to store all the days including the 'all' option
    days = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("choose a day or all").lower()
        if day in days:
            break
        else:
            print("Wrong input")
    print('-'*80)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    # Load data for city
    print("\nLoading data.......")

    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['start hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # Returns the selected file as a dataframe (df) with relevant columns
    return df

# Function to calculate all the time-related statistics for the chosen data


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most Popular Month (1 = January,...,6 = June): {} '.format(
        df['month'].mode()[0]))

    print("\nMost Popular Day: {}".format(df['day_of_week'].mode()[0]))

    print("\nMost Popular Start Hour: {}".format(df['start hour'].mode()[0]))

    # Prints the time taken to perform the calculation
    # You will find this in all the functions involving any calculation
    # throughout this program
    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*80)

# Function to calculate station related statistics


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Uses mode method to find the most common start station

    print(
        f"The most commonly used start station: {df['Start Station'].mode()[0]}")

    # Uses mode method to find the most common end station

    print(
        f"\nThe most commonly used end station: {df['End Station'].mode()[0]}")

    # Uses str.cat to combine two columsn in the df
    # Assigns the result to a new column 'Start To End'
    # Uses mode on this new column to find out the most common combination
    # of start and end stations
    df['Route'] = df['Start Station']+df['End Station']

    print(
        f"\nThe most frequent combination of trips are from {df['Route'].mode()[0]}.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

# Function for trip duration related statistics


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('Total time Travel: ', (df['Trip Duration'].sum().round()))
    print('Average time Travel: ', (df['Trip Duration'].mean().round()))
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

# Function to calculate user statistics


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # The total users are counted using value_counts method
    # They are then displayed by their types (e.g. Subscriber or Customer)

    # Display counts of user types
    print(df['User Type'].value_counts().to_frame())

    # This try clause is implemented to display the numebr of users by Gender
    # However, not every df may have the Gender column, hence this...
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())
        print('Most Common year of birth : ', int(df["Birth Year"].mode()[0]))
        print('Most latest year of birth : ', int(df["Birth Year"].max()))
        print('Most earliest year of birth : ', int(df["Birth Year"].min()))

    else:
        print("There is no data in this city'sheet")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

# Function to display the data frame itself as per user request


def display_data(df):
    '''To Display the first 5 rows of the prompt city: '''
    print("Check the data if it's available...\n")
    # counter variable is initialized as a tag to ensure only details from
    # a particular point is displayed
    i = 0
    user_enter = input('would you display 5 rows of data ? (yes,no)').lower()
    if user_enter not in ['yes', 'no']:
        print("Enter valid input..!!!!")
    elif user_enter != 'yes':
        print("Thank you ^~^")
    else:
        while i+5 < df.shape[0] and user_enter=='yes':
            print(df.iloc[i:i+5])
            i += 5
            user_enter = input('would you display 5 rows of data ? (yes,no)').lower()
            if user_enter !='yes':
                print("thanks alot :)")
                break
        
    

# Main function to call all the previous functions


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
