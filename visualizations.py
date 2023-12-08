
# import streamlit as st
# from datahandler import read_data
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd


# data = read_data()
# if data is not None:
#     def dayBoardingStatus(data):
#         day_ = data[data['day'].notna() & (data['boarding'].isna()) & (data['boarding_status']=='Day_boarding')]
#         boarding_ = data[(data['boarding'].notna()) & (data['day'].isna()) & (data['boarding_status']=='Day_boarding')]
#         #Create subplots with one row and two columns
#         fig, axes = plt.subplots(1, 2, figsize=(14, 6))

#         # Plot for "day" dataset
#         sns.countplot(data=day_, x='boarding_status', ax=axes[0], palette="Set1")
#         axes[0].set_title("Day schools with day and boarding status")
#         axes[0].set_xlabel("Boarding Status")
#         axes[0].set_ylabel("Number of schools")
#         # Plot for "boarding" dataset
#         sns.countplot(data=boarding_, x='boarding_status', ax=axes[1], palette="Set2")
#         axes[1].set_title("Boarding schools with day and boarding status")
#         axes[1].set_xlabel("Boarding Status")
#         axes[1].set_ylabel("Number of schools")
        
#         # Show the plots
#         return plt 

#     # #number of schools by school owner
#     def schools_by_school_owner(data):
#        # print("reaches the schools by owner function")
#         # Count the number of schools by school owner
#         school_count_by_owner = data['school_owner'].value_counts().reset_index(name='school_count')

#         # Sort the DataFrame in descending order based on the school count
#         school_count_by_owner = school_count_by_owner.sort_values(by='school_count', ascending=False)

#         # Plotting
#         plt.figure(figsize=(8, 6))
#         ax = sns.barplot(data=school_count_by_owner, x='index', y='school_count', palette="Set1", order=school_count_by_owner['index'])
#         plt.xlabel('School Owner')
#         plt.ylabel('Number of Schools')
#         plt.title('Number of Schools')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)

#         return plt
#     #schools_by_school_owner(data)

# #     #double shift
#     def double_shift(data):
        
#         # Filter the data to include only schools with double shift
#         double_shift_data = data[data['classrooms_in_double_shift'].notna()]
#         plt.figure(figsize=(10, 6))
#         sns.countplot(data=double_shift_data, x='school_status', palette="Set2")
#         plt.xlabel('School Status')
#         plt.ylabel('Number of Schools ')
#         plt.title('Number of Schools with Double Shift per School Status')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         plt.tight_layout()
#         #print("reaches the double shift function")

#         return plt 
#     #double_shift(data)

# #     # """1.2 Classrooms"""

#     #classrooms not in use

#     def plot_classrooms_not_in_use(data):
#         classrooms_not_in_use_per_district = data.groupby('district')['Number_of_classrooms_not_in_use'].sum().reset_index()
#         # Sort the DataFrame in descending order based on the number of classrooms not in use
#         classrooms_not_in_use_per_district = classrooms_not_in_use_per_district.sort_values(by='Number_of_classrooms_not_in_use', ascending=False)
#         # Plotting
#         plt.figure(figsize=(10, 6))
#         plt.bar(classrooms_not_in_use_per_district['district'], classrooms_not_in_use_per_district['Number_of_classrooms_not_in_use'], color='skyblue')
#         #plt.xlabel('District')
#         plt.ylabel('Number of Classrooms')
#         plt.title('Classrooms Not in Use')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         #plt.tight_layout()
#         #print("it reaches the classrooms in use function")
#         return plt
#    # plot_classrooms_not_in_use(data)
# #     #classrooms in use
#     def plot_classrooms_per_district(data):
        
#         # Group by district and sum the number of classrooms in use
#         classrooms_per_district = data.groupby('district')['number_of_classroom_in_use'].sum().reset_index()

#         # Sort the DataFrame in descending order based on the number of classrooms
#         classrooms_per_district = classrooms_per_district.sort_values(by='number_of_classroom_in_use', ascending=False)

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         plt.bar(classrooms_per_district['district'], classrooms_per_district['number_of_classroom_in_use'], color='skyblue')
#         #plt.xlabel('District')
#         plt.ylabel('Number of Classrooms')
#         plt.title('Classrooms in Use')
#         plt.xticks(rotation=45, ha='right')
#         plt.tight_layout()
#         plt.grid(visible=False)
#         #print("it reaches the classrooms per district function")
#         return plt
#     #plot_classrooms_per_district(data)




#     # """1.3 Desks"""

#     school_count = data['number_of_desks_not_in_use'].groupby([data['district']]).sum().astype(int).reset_index(name='desk_count')

#     def desks_not_in_use_plot(data):
#         # Group data by district and sum the number of desks not in use
#         desk_count_per_district = data['number_of_desks_not_in_use'].groupby(data['district']).sum().astype(int).reset_index(name='desk_count')

#         # Sort the DataFrame in descending order based on the number of desks not in use
#         desk_count_per_district = desk_count_per_district.sort_values(by='desk_count', ascending=False)

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         bars = plt.bar(desk_count_per_district['district'], desk_count_per_district['desk_count'], color='skyblue')
#         plt.ylabel('Number of Desks ')
#         plt.title('Desks Not in Use')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         #print("it reaches desks not in use ")
#         return plt
#     #desks_not_in_use_plot(data)

#     def desks_in_use_plot(data):
#         # Group data by district and sum the number of desks in use
#         desk_count_per_district = data['number_of_desks_in_use'].groupby(data['district']).sum().astype(int).reset_index(name='desk_count')

#         # Sort the DataFrame in descending order based on the number of desks in use
#         desk_count_per_district = desk_count_per_district.sort_values(by='desk_count', ascending=False)

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         plt.bar(desk_count_per_district['district'], desk_count_per_district['desk_count'], color='skyblue')
#         #plt.xlabel('District')
#         plt.ylabel('Number of Desks')
#         plt.title('Desks in Use')
#         plt.grid(visible=False)
#         plt.xticks(rotation=45, ha='right')
#         return plt
# #     # """Students"""

#     def plot_students_by_level(data):
#         categories = [
#             "preprimary_students",
#             "tvet_l1_to_l2_students",
#             "Prof_sec_students",
#             "tvet_l3_to_l5_students",
#             "upper_secondary_students",
#             "lower_secondary_students",
#             "primary_students",
#             "ttc_students",
#             "nursing_students",
#             "accounting_students"
#         ]

#         # Create a DataFrame to store the data
#         df = pd.DataFrame({'Category': categories})

#         # Loop through categories and add columns for male and female students
#         for category in categories:
#             male_col = f"{category}_male"
#             female_col = f"{category}_female"

#             # Sum the male and female students for each category
#             df[category] = data[[male_col, female_col]].sum(axis=1)

#         # Sum the male and female students across all levels
#         numeric_columns = df.select_dtypes(include='number').columns
#         df['All Levels'] = df[numeric_columns].sum(axis=1)

#         # Sort the DataFrame in descending order based on the total number of students
#         df = df.sort_values(by='All Levels', ascending=False)

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         bars = plt.bar(df['Category'], df['All Levels'], color='skyblue', label='Male')
#         bars2 = plt.bar(df['Category'], df['All Levels'], color='lightcoral', label='Female', bottom=df['All Levels'])

#         plt.xlabel('Level')
#         plt.ylabel('Total Students')
#         plt.title('Students by Level')
#         plt.xticks(rotation=45, ha='right')
#         plt.legend()
#         plt.grid(visible=False)

#         plt.tight_layout()
#         #print("it reaches students by level")
#         return plt
#     #plot_students_by_level(data)
#     #boarding students

#     def boarding_students_per_district(data):

#         # Group data by district and sum the total boarding students
#         district_data = data.groupby('district')['total_boarding_students'].sum().reset_index()

#         # Sort the DataFrame in descending order based on the total boarding students
#         district_data = district_data.sort_values(by='total_boarding_students', ascending=False)

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         bars = plt.bar(district_data['district'], district_data['total_boarding_students'], color='skyblue')
#         #plt.xlabel('District')
#         plt.ylabel(' Boarding Students')
#         plt.title('Total Boarding Students')
#         plt.xticks(rotation=45, ha='right')
#         plt.tight_layout()
#         plt.grid(visible=False)
#         return plt
#     #boarding_students_per_district(data)



#     #STEM students
#     def stem_students_per_district(data):
#         # Group the data by district and sum the stem_students_total
#         district_data = data.groupby('district')['stem_students_total'].sum().reset_index()

#         # Sort the DataFrame in descending order based on the stem_students_total
#         district_data = district_data.sort_values(by='stem_students_total', ascending=False)

#         # Create a bar plot
#         plt.figure(figsize=(10, 6))
#         bars = plt.bar(district_data['district'], district_data['stem_students_total'], color='skyblue')
#         plt.ylabel('STEM Students')
#         plt.title('STEM Students  ')
#         plt.xticks(rotation=45, ha='right')
#         plt.tight_layout()
#         plt.grid(visible=False)
#         #print("reaches here as well")
#         return plt
#     #stem_students_per_district(data)

#     #deliberation decision
#     def deliberation_decisions(data):
#         # Group the data by district and sum the students_without_deliberation_decision
#         district_data = data.groupby('district')['students_without_deliberation_decision'].sum().reset_index()

#         # Sort the DataFrame in descending order based on the number of students without deliberation decision
#         district_data = district_data.sort_values(by='students_without_deliberation_decision', ascending=False)
#         # Create a figure with custom styling
#         plt.figure(figsize=(10, 6))
#         sns.set_style("whitegrid")
#         colors = sns.color_palette("pastel", len(district_data))

#         # Create a vertical bar plot
#         ax = sns.barplot(x=district_data['district'], y=district_data['students_without_deliberation_decision'], palette=colors)

#         plt.ylabel('Students')
#         plt.title('Students Without Deliberation Decision')
#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         plt.grid(visible=False)
#         return plt 
#     def plot_teaching_staff_by_district(data):
#         # Group the data by district and sum the total_teaching_staff
#         district_data = data.groupby('district')['total_teaching_staff'].sum().reset_index()
#         # Sort the DataFrame in descending order based on the total_teaching_staff
#         district_data = district_data.sort_values(by='total_teaching_staff', ascending=False)
#         # Create a bar chart for teaching staff per district
#         plt.figure(figsize=(10, 6))
#         plt.bar(district_data['district'], district_data['total_teaching_staff'], color='skyblue')
#     # plt.xlabel('District')
#         plt.ylabel('Total Teaching Staff')
#         plt.title('Teaching Staff')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         return plt
#     #unassigned teachers
#     def plot_unassigned_teachers_by_district(data):
#         # Group the data by district and sum the total_unassigned_teachers
#         district_data = data.groupby('district')['total_unassigned_teachers'].sum().reset_index()

#         # Sort the DataFrame in descending order based on the total_unassigned_teachers
#         district_data = district_data.sort_values(by='total_unassigned_teachers', ascending=False)

#         plt.figure(figsize=(10, 6))

#         # Iterate through the data to add bars and labels
#         plt.bar(district_data['district'], district_data['total_unassigned_teachers'], color='skyblue')
#         #plt.xlabel('District')
#         plt.ylabel(' Unassigned Teachers')
#         plt.title('Unassigned Teachers')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         return plt

#     #pupil teacher ratio

#     def plot_pupil_teacher_ratios(data):
#         preprimary_PTR = (data['preprimary_students_total'].sum() / data['total_preprimary_teachers'].sum()).round()
#         primary_PTR = (data['primary_students_total'].sum() / data['total_primary_teachers'].sum()).round()
#         Lower_sec_PTR = (data['lower_secondary_students_total'].sum() / data['total_lower_secondary_teachers'].sum()).round()
#         General_Upper_PTR = (data['upper_secondary_students_total'].sum() / data['total_upper_secondary_teachers'].sum()).round()

#         # Create df for the ratios
#         ratios_df = pd.DataFrame({
#             'Level': ['Preprimary', 'Primary', 'Lower Secondary', 'General Upper Secondary'],
#             'Pupil-Teacher Ratio': [preprimary_PTR, primary_PTR, Lower_sec_PTR, General_Upper_PTR]
#         })
#         plt.figure(figsize=(10, 6))
#         ax = sns.barplot(data=ratios_df, x='Level', y='Pupil-Teacher Ratio')
#         plt.ylabel('Pupil-Teacher Ratio')
#         plt.title('Pupil-Teacher Ratio')
#         plt.xticks(rotation=45, ha='right')
#         for p in ax.patches:
#             ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                         ha='center', va='center', xytext=(0, 10), textcoords='offset points')

#         # Show the plot
#         plt.tight_layout()
#         plt.grid(visible=False)
#         return plt
#     #plot_pupil_teacher_ratios(data)
#     #water supply
#     def plot_water_facilities(data):
#         # Select relevant columns related to water facilities
#         water_columns = ['tap_water_supply', 'rain_water_haversting', 'safe_drinking_water', 'no_water_available']
#         # Create a new DataFrame with binary values (1 or 0) indicating the presence of each water facility
#         water_df = data[water_columns].applymap(lambda x: 1 if x == 1 else 0)
#         water_counts = water_df.sum()
#         plt.figure(figsize=(10, 6))
#         ax = sns.barplot(x=water_counts.index, y=water_counts.values, palette="viridis")
#         plt.title('Number of Schools with Water Facilities')
#         plt.xlabel('Water Facility')
#         plt.ylabel('Number of Schools')
#         plt.xticks(rotation=45, ha='right')
#         plt.grid(visible=False)
#         for i, v in enumerate(water_counts.values):
#             ax.text(i, v + 0.1, str(v), ha='center', va='bottom')
#         return plt
    
#     #admnistrative staff
#     def plot_administrative_staff_by_status(data):
#         # Group by school status and calculate totals
#         admin_totals = (
#             data.groupby('school_status')
#             .agg(
#                 administrative_staff_male=('administrative_staff_male', 'sum'),
#                 administrative_staff_female=('administrative_staff_female', 'sum')
#             )
#             .reset_index()
#         )

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         bars = plt.bar(admin_totals['school_status'], admin_totals['administrative_staff_male'], color='skyblue', label='Male')
#         bars2 = plt.bar(admin_totals['school_status'], admin_totals['administrative_staff_female'], color='lightcoral', label='Female', bottom=admin_totals['administrative_staff_male'])
#         plt.xlabel('School Status')
#         plt.ylabel('Administrative Staff')
#         plt.title('Administrative Staff')
#         plt.xticks(rotation=45, ha='right')
#         plt.legend()
#         plt.grid(visible=False)
#         plt.tight_layout()
#         return plt
    
#     #users per toilet

#     def plot_toilets(data):
#         plt.figure(figsize=(10, 6))
#         plt.bar('Students Toilets', data['students_toilets'].sum(), color='skyblue')
#         plt.bar('Staff Toilets', data['staff_toilets'].sum(), color='lightcoral')
#         plt.ylabel('Total Toilets')
#         plt.title('Toilet per users')
#         plt.grid(visible=False)
#         return plt
#     def schools_with_power_sources(data):
        
#         # Filter schools with power sources
#         power_schools = data[(data['on_grid_electricity'] == 1) | (data['solar_power'] == 1) | (data['electric_power_generator_supply'] == 1) | (data['biogas_system'] == 1)]

#         # Count the number of schools
#         num_schools = len(power_schools)

#         # Display the result in a Streamlit table
#         st.write(f"Number of Schools with Power Sources: {num_schools}")
#         st.table(power_schools[['school_name', 'district', 'on_grid_electricity', 'solar_power', 'electric_power_generator_supply', 'biogas_system']])
# else:
#     print("No data available.")