import streamlit as st
st.set_page_config(
    page_icon=":school:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

import streamlit as st
from datahandler import read_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = read_data()
if data is not None:
    #data = read_data()
    def dayBoardingStatus(data):
        day_ = data[data['day'].notna() & (data['boarding'].isna()) & (data['boarding_status']=='Day_boarding')]
        boarding_ = data[(data['boarding'].notna()) & (data['day'].isna()) & (data['boarding_status']=='Day_boarding')]
        #Create subplots with one row and two columns
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        sns.countplot(data=day_, x='boarding_status', ax=axes[0], palette="Set1")
        axes[0].set_title("Day schools with day and boarding status")
        axes[0].set_xlabel("Boarding Status")
        axes[0].set_ylabel("Number of schools")
        # Plot for "boarding" dataset
        sns.countplot(data=boarding_, x='boarding_status', ax=axes[1], palette="Set2")
        axes[1].set_title("Boarding schools with day and boarding status")
        axes[1].set_xlabel("Boarding Status")
        axes[1].set_ylabel("Number of schools")
        
        # Show the plots
        return plt 

   # @st.cache_resource()

    def schools_by_school_owner(data):
        # Count the number of schools by school owner
        school_count_by_owner = data['school_owner'].value_counts().reset_index(name='school_count')

        # Sort the DataFrame in descending order based on the school count
        school_count_by_owner = school_count_by_owner.sort_values(by='school_count', ascending=False)

        # Plotting with matplotlib
        plt.figure(figsize=(8, 6))

        # Use 'index' as the column name for the x-axis
        plt.bar(school_count_by_owner['index'], school_count_by_owner['school_count'], color="skyblue")

        plt.xlabel('School Owner')
        plt.ylabel('Number of Schools')
        plt.title('Number of Schools')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)

        return plt

    #schools_by_school_owner(data)

#     #double shift
    def double_shift(data):
        double_shift_data = data[data['classrooms_in_double_shift'].notna()]
        plt.figure(figsize=(10, 6))
        sns.countplot(data=double_shift_data, x='school_status', palette="Set2")
        plt.xlabel('School Status')
        plt.ylabel('Number of Schools ')
        plt.title('Number of Schools with Double Shift per School Status')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        plt.tight_layout()
        #print("reaches the double shift function")

        return plt 
    #double_shift(data)

#     # """1.2 Classrooms"""

    #classrooms not in use

    def plot_classrooms_not_in_use(data):
        classrooms_not_in_use_per_district = data.groupby('district')['Number_of_classrooms_not_in_use'].sum().reset_index()
        # Sort the DataFrame in descending order based on the number of classrooms not in use
        classrooms_not_in_use_per_district = classrooms_not_in_use_per_district.sort_values(by='Number_of_classrooms_not_in_use', ascending=False)
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(classrooms_not_in_use_per_district['district'], classrooms_not_in_use_per_district['Number_of_classrooms_not_in_use'], color='skyblue')
        #plt.xlabel('District')
        plt.ylabel('Number of Classrooms')
        plt.title('Classrooms Not in Use')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        #plt.tight_layout()
        #print("it reaches the classrooms in use function")
        return plt
   # plot_classrooms_not_in_use(data)
#     #classrooms in use
    def plot_classrooms_per_district(data):
        
        # Group by district and sum the number of classrooms in use
        classrooms_per_district = data.groupby('district')['number_of_classroom_in_use'].sum().reset_index()

        # Sort the DataFrame in descending order based on the number of classrooms
        classrooms_per_district = classrooms_per_district.sort_values(by='number_of_classroom_in_use', ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(classrooms_per_district['district'], classrooms_per_district['number_of_classroom_in_use'], color='skyblue')
        #plt.xlabel('District')
        plt.ylabel('Number of Classrooms')
        plt.title('Classrooms in Use')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(visible=False)
        #print("it reaches the classrooms per district function")
        return plt
    #plot_classrooms_per_district(data)




    # """1.3 Desks"""

    school_count = data['number_of_desks_not_in_use'].groupby([data['district']]).sum().astype(int).reset_index(name='desk_count')

    def desks_not_in_use_plot(data):
        # Group data by district and sum the number of desks not in use
        desk_count_per_district = data['number_of_desks_not_in_use'].groupby(data['district']).sum().astype(int).reset_index(name='desk_count')

        # Sort the DataFrame in descending order based on the number of desks not in use
        desk_count_per_district = desk_count_per_district.sort_values(by='desk_count', ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        bars = plt.bar(desk_count_per_district['district'], desk_count_per_district['desk_count'], color='skyblue')
        plt.ylabel('Number of Desks ')
        plt.title('Desks Not in Use')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        #print("it reaches desks not in use ")
        return plt
    #desks_not_in_use_plot(data)

    def desks_in_use_plot(data):
        # Group data by district and sum the number of desks in use
        desk_count_per_district = data['number_of_desks_in_use'].groupby(data['district']).sum().astype(int).reset_index(name='desk_count')

        # Sort the DataFrame in descending order based on the number of desks in use
        desk_count_per_district = desk_count_per_district.sort_values(by='desk_count', ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(desk_count_per_district['district'], desk_count_per_district['desk_count'], color='skyblue')
        #plt.xlabel('District')
        plt.ylabel('Number of Desks')
        plt.title('Desks in Use')
        plt.grid(visible=False)
        plt.xticks(rotation=45, ha='right')
        return plt
#     # """Students"""

    def plot_students_by_level(data):
        categories = [
            "preprimary_students",
            "tvet_l1_to_l2_students",
            "Prof_sec_students",
            "tvet_l3_to_l5_students",
            "upper_secondary_students",
            "lower_secondary_students",
            "primary_students",
            "ttc_students",
            "nursing_students",
            "accounting_students"
        ]

        # Create a DataFrame to store the data
        df = pd.DataFrame({'Category': categories})

        # Loop through categories and add columns for male and female students
        for category in categories:
            male_col = f"{category}_male"
            female_col = f"{category}_female"

            # Sum the male and female students for each category
            df[category] = data[[male_col, female_col]].sum(axis=1)

        # Sum the male and female students across all levels
        numeric_columns = df.select_dtypes(include='number').columns
        df['All Levels'] = df[numeric_columns].sum(axis=1)

        # Sort the DataFrame in descending order based on the total number of students
        df = df.sort_values(by='All Levels', ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        bars = plt.bar(df['Category'], df['All Levels'], color='skyblue', label='Male')
        bars2 = plt.bar(df['Category'], df['All Levels'], color='lightcoral', label='Female', bottom=df['All Levels'])

        plt.xlabel('Level')
        plt.ylabel('Total Students')
        plt.title('Students by Level')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.grid(visible=False)

        plt.tight_layout()
        #print("it reaches students by level")
        return plt
    #plot_students_by_level(data)
    #boarding students

    def boarding_students_per_district(data):

        # Group data by district and sum the total boarding students
        district_data = data.groupby('district')['total_boarding_students'].sum().reset_index()

        # Sort the DataFrame in descending order based on the total boarding students
        district_data = district_data.sort_values(by='total_boarding_students', ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        bars = plt.bar(district_data['district'], district_data['total_boarding_students'], color='skyblue')
        #plt.xlabel('District')
        plt.ylabel(' Boarding Students')
        plt.title('Total Boarding Students')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(visible=False)
        return plt
    #boarding_students_per_district(data)



    #STEM students
    def stem_students_per_district(data):
        # Group the data by district and sum the stem_students_total
        district_data = data.groupby('district')['stem_students_total'].sum().reset_index()

        # Sort the DataFrame in descending order based on the stem_students_total
        district_data = district_data.sort_values(by='stem_students_total', ascending=False)

        # Create a bar plot
        plt.figure(figsize=(10, 6))
        bars = plt.bar(district_data['district'], district_data['stem_students_total'], color='skyblue')
        plt.ylabel('STEM Students')
        plt.title('STEM Students  ')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(visible=False)
        #print("reaches here as well")
        return plt
    #stem_students_per_district(data)

    #deliberation decision
    def deliberation_decisions(data):
        # Group the data by district and sum the students_without_deliberation_decision
        district_data = data.groupby('district')['students_without_deliberation_decision'].sum().reset_index()

        # Sort the DataFrame in descending order based on the number of students without deliberation decision
        district_data = district_data.sort_values(by='students_without_deliberation_decision', ascending=False)
        # Create a figure with custom styling
        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        colors = sns.color_palette("pastel", len(district_data))

        # Create a vertical bar plot
        ax = sns.barplot(x=district_data['district'], y=district_data['students_without_deliberation_decision'], palette=colors)

        plt.ylabel('Students')
        plt.title('Students Without Deliberation Decision')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(visible=False)
        return plt 
    def plot_teaching_staff_by_district(data):
        # Group the data by district and sum the total_teaching_staff
        district_data = data.groupby('district')['total_teaching_staff'].sum().reset_index()
        # Sort the DataFrame in descending order based on the total_teaching_staff
        district_data = district_data.sort_values(by='total_teaching_staff', ascending=False)
        # Create a bar chart for teaching staff per district
        plt.figure(figsize=(10, 6))
        plt.bar(district_data['district'], district_data['total_teaching_staff'], color='skyblue')
    # plt.xlabel('District')
        plt.ylabel('Total Teaching Staff')
        plt.title('Teaching Staff')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        return plt
    #unassigned teachers
    def plot_unassigned_teachers_by_district(data):
        # Group the data by district and sum the total_unassigned_teachers
        district_data = data.groupby('district')['total_unassigned_teachers'].sum().reset_index()

        # Sort the DataFrame in descending order based on the total_unassigned_teachers
        district_data = district_data.sort_values(by='total_unassigned_teachers', ascending=False)

        plt.figure(figsize=(10, 6))

        # Iterate through the data to add bars and labels
        plt.bar(district_data['district'], district_data['total_unassigned_teachers'], color='skyblue')
        #plt.xlabel('District')
        plt.ylabel(' Unassigned Teachers')
        plt.title('Unassigned Teachers')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        return plt

    #pupil teacher ratio

    def plot_pupil_teacher_ratios(data):
        preprimary_PTR = (data['preprimary_students_total'].sum() / data['total_preprimary_teachers'].sum()).round()
        primary_PTR = (data['primary_students_total'].sum() / data['total_primary_teachers'].sum()).round()
        Lower_sec_PTR = (data['lower_secondary_students_total'].sum() / data['total_lower_secondary_teachers'].sum()).round()
        General_Upper_PTR = (data['upper_secondary_students_total'].sum() / data['total_upper_secondary_teachers'].sum()).round()

        # Create df for the ratios
        ratios_df = pd.DataFrame({
            'Level': ['Preprimary', 'Primary', 'Lower Secondary', 'General Upper Secondary'],
            'Pupil-Teacher Ratio': [preprimary_PTR, primary_PTR, Lower_sec_PTR, General_Upper_PTR]
        })
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(data=ratios_df, x='Level', y='Pupil-Teacher Ratio')
        plt.ylabel('Pupil-Teacher Ratio')
        plt.title('Pupil-Teacher Ratio')
        plt.xticks(rotation=45, ha='right')
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')

        # Show the plot
        plt.tight_layout()
        plt.grid(visible=False)
        return plt
    #plot_pupil_teacher_ratios(data)
    #water supply
    def plot_water_facilities(data):
        # Select relevant columns related to water facilities
        water_columns = ['tap_water_supply', 'rain_water_haversting', 'safe_drinking_water', 'no_water_available']
        # Create a new DataFrame with binary values (1 or 0) indicating the presence of each water facility
        water_df = data[water_columns].applymap(lambda x: 1 if x == 1 else 0)
        water_counts = water_df.sum()
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=water_counts.index, y=water_counts.values, palette="viridis")
        plt.title('Number of Schools with Water Facilities')
        plt.xlabel('Water Facility')
        plt.ylabel('Number of Schools')
        plt.xticks(rotation=45, ha='right')
        plt.grid(visible=False)
        for i, v in enumerate(water_counts.values):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom')
        return plt
    
    #admnistrative staff
    def plot_administrative_staff_by_status(data):
        # Group by school status and calculate totals
        admin_totals = (
            data.groupby('school_status')
            .agg(
                administrative_staff_male=('administrative_staff_male', 'sum'),
                administrative_staff_female=('administrative_staff_female', 'sum')
            )
            .reset_index()
        )

        # Plotting
        plt.figure(figsize=(10, 6))
        bars = plt.bar(admin_totals['school_status'], admin_totals['administrative_staff_male'], color='skyblue', label='Male')
        bars2 = plt.bar(admin_totals['school_status'], admin_totals['administrative_staff_female'], color='lightcoral', label='Female', bottom=admin_totals['administrative_staff_male'])
        plt.xlabel('School Status')
        plt.ylabel('Administrative Staff')
        plt.title('Administrative Staff')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.grid(visible=False)
        plt.tight_layout()
        return plt
    
    #users per toilet

    def plot_toilets(data):
        plt.figure(figsize=(10, 6))
        plt.bar('Students Toilets', data['students_toilets'].sum(), color='skyblue')
        plt.bar('Staff Toilets', data['staff_toilets'].sum(), color='lightcoral')
        plt.ylabel('Total Toilets')
        plt.title('Toilet per users')
        plt.grid(visible=False)
        return plt
    def schools_with_power_sources(data):
        
        # Filter schools with power sources
        power_schools = data[(data['on_grid_electricity'] == 1) | (data['solar_power'] == 1) | (data['electric_power_generator_supply'] == 1) | (data['biogas_system'] == 1)]

        # Count the number of schools
        num_schools = len(power_schools)

        # Display the result in a Streamlit table
        st.write(f"Number of Schools with Power Sources: {num_schools}")
        st.table(power_schools[['school_name', 'district', 'on_grid_electricity', 'solar_power', 'electric_power_generator_supply', 'biogas_system']])
else:
    print("No data available.")


#streamlit app 
# Display the dataset preview
st.write("### Dataset Preview:")
st.write(data.head())

with st.sidebar:
    category = st.sidebar.radio("Show dashboard for: ", ["SCHOOL INFRASTRUCTURE", "STUDENTS", "SCHOOL STAFF", "ENERGY, WATER AND SANITATION","BOOKS AND TEXTBOOKS","ICT, SCIENCE AND TECHNOLOGY","SCHOOL NUTRITION","SPECIAL NEEDS EDUCATION"])

#checkbox = st.sidebar.checkbox("Show infrastructure dashboard") #add checkbox as widget 
if category == "SCHOOL INFRASTRUCTURE":
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown("Pupil classroom ratio")
    a1, a2 ,a3,a4,a5,a6= st.columns(6)
    preprimary_PCR=int((data['preprimary_students_total'].sum()/data['preprimary_classrooms'].sum()).round())
    primary_PCR=int((data['primary_students_total'].sum()/data['primary_classrooms'].sum()).round())
    Lower_sec_PCR=int((data['lower_secondary_students_total'].sum()/data['lower_secondary_classrooms'].sum()).round())
    General_Upper_PCR=int((data['upper_secondary_students_total'].sum()/data['upper_secondary_classrooms'].sum()).round())
    TVET_L1_L2_PCR=int((data['tvet_l1_to_l2_students_total'].sum()/data['tvet_l1_to_l2_classrooms'].sum()).round())
    TVET_L3_L5_PCR=int((data['tvet_l3_to_l5_students_total'].sum()/data['tvet_l3_to_l5_classrooms'].sum()).round())
    ratios = {
        'Preprimary PCR': preprimary_PCR,
        'Primary PCR': primary_PCR,
        'Lower Secondary PCR': Lower_sec_PCR,
        'General Upper PCR': General_Upper_PCR,
        'TVET L1-L2 PCR': TVET_L1_L2_PCR,
        'TVET L3-L5 PCR': TVET_L3_L5_PCR
    }

    a1.metric("Preprimary PCR", f"{preprimary_PCR}")
    a2.metric("Primary PCR",f"{primary_PCR}")
    a3.metric("Lower Sec PCR", f"{Lower_sec_PCR}")
    a4.metric("Gen Upper Sec PCR", f"{General_Upper_PCR}")
    a5.metric("TVET L1-L2 PCR", f"{TVET_L1_L2_PCR}")
    a6.metric("TVET L3-L5 PCR", f"{TVET_L3_L5_PCR}")
    tab1,tab2,tab3=st.tabs(["PCR per district",'PTR by level','School setting'])
    with  tab1:
        if st.checkbox("Show PCR table"):
            def compute_overall_pcr(data):
                data['total_students'] = pd.to_numeric(data['total_students'], errors='coerce')
                data['total_classrooms'] = pd.to_numeric(data['total_classrooms'], errors='coerce')
                data['pcr'] = data['total_students'] / data['total_classrooms']
                overall_pcr = data.groupby('district')['pcr'].mean().reset_index()
                overall_pcr['pcr'] = overall_pcr['pcr'].round().astype(int)
                overall_pcr = overall_pcr.sort_values(by='pcr', ascending=False)
                #st.write("Overall Pupil Classroom Ratio (PCR) by District:")
                st.table(overall_pcr[['district', 'pcr']].set_index('district'))
            compute_overall_pcr(data)
    with tab2:
        if st.checkbox("Show PTR table"):
            def compute_ptr_by_level(data):
        # Ensure numeric columns are treated as numeric
                numeric_cols = [
                    'total_preprimary_teachers', 'preprimary_students_total',
                    'total_primary_teachers', 'primary_students_total',
                    'total_lower_secondary_teachers', 'lower_secondary_students_total',
                    'total_upper_secondary_teachers', 'upper_secondary_students_total',
                    #'total_tvet_l3_to_l5_teachers', 'tvet_l3_to_l5_students_total',
                    #'total_tvet_l1_to_l2_teachers', 'tvet_l1_to_l2_students_total',
                    'Prof_sec_teacher_total', 'Prof_sec_students_total',
                    #'total_ttc_teachers', 'ttc_students_total'
                ]

                data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')

        # List of levels and corresponding columns
                levels = ['preprimary', 'primary', 'lower_secondary', 'upper_secondary', 'prof_sec']
                level_columns = {
                            'preprimary': ('preprimary_students_total', 'total_preprimary_teachers'),
                            'primary': ('primary_students_total', 'total_primary_teachers'),
                            'lower_secondary': ('lower_secondary_students_total', 'total_lower_secondary_teachers'),
                            'upper_secondary': ('upper_secondary_students_total', 'total_upper_secondary_teachers'),
                            'prof_sec': ('Prof_sec_students_total', 'Prof_sec_teacher_total'),
                        }


        # Create a dictionary to store the PTR for each level
                ptr_dict = {}

        # Create a list to store individual PTR DataFrames
                ptr_dfs = []

                for level, (students_col, teachers_col) in level_columns.items():
                    # Calculate Pupil Teacher Ratio (PTR) for the current level
                    data[f'ptr_{level}'] = data[students_col] / data[teachers_col]

                    # Group by district and calculate overall PTR for the current level in each district
                    overall_ptr = data.groupby('district')[f'ptr_{level}'].mean().reset_index()

                    # Round the PTR column to whole numbers
                    overall_ptr[f'ptr_{level}'] = overall_ptr[f'ptr_{level}'].round().astype(int)

                    # Sort the DataFrame by PTR in descending order
                    overall_ptr = overall_ptr.sort_values(by=f'ptr_{level}', ascending=False)

                    # Store the PTR DataFrame in the list
                    ptr_dfs.append(overall_ptr[['district', f'ptr_{level}']].set_index('district'))

                # Concatenate individual PTR DataFrames into a single table
                ptr_table = pd.concat(ptr_dfs, axis=1)

                return ptr_table

            ptr_table = compute_ptr_by_level(data)

            st.write("Combined Pupil Teacher Ratio (PTR) by District:")
            st.table(ptr_table)
            

    with tab3:
        schools_count = data.groupby(['school_settings', 'school_status']).size().unstack(fill_value=0)
        st.write('Schools by school setting and status')
        show_table = st.checkbox("Here is the table")
        if show_table:
         st.table(schools_count) # show table for schools by school setting 
    #create tabs for different categories
    tab1, tab2, tab3,tab4,tab5 = st.tabs(["School owner", "Boarding status", "Shift program","Classrooms","Desks"])

    with tab1:
        st.write("Schools by school owner")
        st.pyplot(schools_by_school_owner(data))

    with tab2:
        st.write("Schools boarding status")
        boarding_status_counts = data['boarding_status'].value_counts()
            # Create a donut chart
        fig, ax = plt.subplots()
        ax.pie(boarding_status_counts, labels=boarding_status_counts.index, autopct='%1.1f%%', startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.4))
        ax.axis('equal')
        ax.legend(boarding_status_counts.index, title="Boarding Status", loc="center left", bbox_to_anchor=(1, 0.5))
        st.pyplot(fig)
        show_table2=st.checkbox("Check to show schools missing boarding status")
        if show_table2:
            empty_boarding_status = data[data['boarding_status'].isna()]
            st.table(empty_boarding_status['school_name'])

    with tab3:
        st.write("Schools with doubleshift")
        st.pyplot(double_shift(data))
    with tab4:
        #classrooms_checkbox = st.checkbox("Show classrooms in use", value=True)
        #classrooms_not_in_use_chec=st.checkbox("Show classrooms not in use",value=True)
        #if classrooms_checkbox:
        st.write("Classrooms in use per district")
        st.pyplot(plot_classrooms_per_district(data))
        #if classrooms_not_in_use_chec:
        st.write("Classrooms not in use per district")
        st.pyplot(plot_classrooms_not_in_use(data))
    with tab5:
        st.write("Desks not in use per district")
        st.pyplot(desks_not_in_use_plot(data))
        show_table3=st.checkbox("Check to show schools with desks not in use")
        if show_table3:
            schools_with_desks_not_in_use = data[data['number_of_desks_not_in_use'].notna()]
            st.table(schools_with_desks_not_in_use[['district','school_name']])    
        st.write("Desks in use per district")
        st.pyplot(desks_in_use_plot(data))
        
        
elif category=="STUDENTS":
   tab1, tab2, tab3,tab4= st.tabs(["Students by level", "Students by Boarding status", "Stem status ","Deliberation"])
   with tab1:
        st.write("Students  by level")
        st.pyplot(plot_students_by_level(data))
   with tab2:
       st.write("Students by boarding status")
       st.pyplot(boarding_students_per_district(data))
   with tab3:
       st.write("Students by STEM status")
       st.pyplot(stem_students_per_district(data))
   with tab4:
       st.write("Students without deliberation")
       st.pyplot(deliberation_decisions(data))
       
#school staff
elif category=="SCHOOL STAFF":
    tab1,tab2,tab3=st.tabs(['Teaching staff by district','Unassigned Teachers','Pupil Teacher Ratio'])
    with tab1:
        st.write("Teaching staff by district")
        st.pyplot(plot_teaching_staff_by_district(data))
        st.write("Administrative staff")
        st.pyplot(plot_administrative_staff_by_status(data))
        checkbox=st.checkbox("Check to display the table for administrative staff")
        if checkbox:
    
            # Select relevant columns
            admin_data = data[['district', 'administrative_staff_male', 'administrative_staff_female', 'total_administrative_staff']]

    # Group by district and calculate totals
            admin_totals = admin_data.groupby('district').sum().reset_index()

    # Add a row for overall totals
            overall_totals = pd.DataFrame({'district': ['Total'],
                                   'administrative_staff_male': admin_totals['administrative_staff_male'].sum(),
                                   'administrative_staff_female': admin_totals['administrative_staff_female'].sum(),
                                   'total_administrative_staff': admin_totals['total_administrative_staff'].sum()})

    # Format columns to remove trailing zeros and add thousand separators
            for col in ['administrative_staff_male', 'administrative_staff_female', 'total_administrative_staff']:
                admin_totals[col] = admin_totals[col].apply(lambda x: '{:,.0f}'.format(x).rstrip('0').rstrip('.') if pd.notna(x) else x)
                overall_totals[col] = overall_totals[col].apply(lambda x: '{:,.0f}'.format(x).rstrip('0').rstrip('.') if pd.notna(x) else x)

    # Concatenate the overall totals row to the grouped data
            admin_data_with_totals = pd.concat([admin_totals, overall_totals], ignore_index=True)

    # Display the data in a table using Streamlit
            st.table(admin_data_with_totals)

    with tab2:
        st.write("Total Unassigned Teachers by district")
        st.pyplot(plot_unassigned_teachers_by_district(data))
    with tab3:
        st.write("Pupil Teacher Ratios")
        st.pyplot(plot_pupil_teacher_ratios(data))
elif category=="ENERGY, WATER AND SANITATION":
    tab1,tab2,tab3,tab4=st.tabs(['Water supply in schools','Toilets',"Handwashing","Energy"])
    with tab1:
        st.write("School water supply")
        st.pyplot(plot_water_facilities(data))
        
    with tab2:
        st.write("School toilets")
        def display_toilet_stats(data):
    
            toilet_stats = (
                data.groupby('school_status')
                .agg(
                    students_toilet=('students_toilets', 'sum'),
                    staff_toilets=('staff_toilets', 'sum'),
                    toilets_for_students_with_disabilities=('toiletes_for_students_with_disabilities', 'sum'),
                    toilets_for_staff_with_disabilities=('toiletes_for_staff_with_disabilities', 'sum'),
                )
                .reset_index()
            )
            numeric_cols = toilet_stats.columns[1:]  # Exclude 'school_status' column
            toilet_stats[numeric_cols] = toilet_stats[numeric_cols].astype(float)
            toilet_stats[numeric_cols] = toilet_stats[numeric_cols].applymap(lambda x: '{:,.0f}'.format(x).rstrip('0').rstrip('.'))

            return toilet_stats
        toilet_stats_data = display_toilet_stats(data)
        st.table(toilet_stats_data)
        st.write("Users per toilet")
        st.pyplot(plot_toilets(data))
    with tab3:
        st.write("Schools without handwashing facilities")
        def schools_with_no_handwashing_facilities(data):
    
            no_handwashing_facilities = (
                data[data['have_handwashing_facilities'].isnull()]
                .groupby('school_status')
                .size()
                .reset_index(name='Number of Schools')
            )

            return no_handwashing_facilities
        no_handwashing_facilities_data = schools_with_no_handwashing_facilities(data)
        st.table(no_handwashing_facilities_data)
    with tab4:
        st.write("Schools with energy sources")
        def schools_with_power_sources(data):
            # Filter schools with power sources
            power_schools = data[(data['on_grid_electricity'] == 1) | 
                                (data['solar_power'] == 1) | 
                                (data['electric_power_generator_supply'] == 1) | 
                                (data['biogas_system'] == 1)]

            # Select only the specified columns and group by school_status
            count_per_status = power_schools.groupby('school_status')[['on_grid_electricity', 'solar_power', 'electric_power_generator_supply', 'biogas_system']].sum()

            # Remove trailing zeros
            count_per_status =     count_per_status = count_per_status.applymap(lambda x: '{:,}'.format(int(x)))

            # Ensure "Public" comes first
            count_per_status = count_per_status.reindex(['PUBLIC'] + list(count_per_status.index.difference(['PUBLIC'])))

            # Display the result in a Streamlit table
            #st.write("Number of Schools with Power Sources:")
            st.table(count_per_status)

        # Example usage:
        # Assuming 'data' is your DataFrame
        schools_with_power_sources(data)


           
    #BOOKS AND TEXTBOOKS
elif category=="BOOKS AND TEXTBOOKS":
    tab1,tab2=st.tabs(['Number of books in schools','Library in schools'])
    with tab1:
        st.write("Total number of books per school status")
        def books_per_school_status(data):
    # Group the data by school_status and sum the total_books
            books_by_status = (
                data.groupby('school_status')
                .agg(
                    total_books=('number_of_books', 'sum'),
                )
                .reset_index()
            )

            # Sort the DataFrame so that 'public' comes first
            books_by_status = books_by_status.sort_values(by='school_status', ascending=False)

            # Format the total_books column
            books_by_status['total_books'] = books_by_status['total_books'].astype(str).str.rstrip('0').str.rstrip('.')
            books_by_status['total_books'] = books_by_status['total_books'].apply(lambda x: '{:,.0f}'.format(float(x)))

            return books_by_status

        books_by_status_data = books_per_school_status(data)

        st.table(books_by_status_data)
    with tab2:
        st.write("Schools without library")
        def schools_with_no_library(data):
    # Filter schools with no library
            no_library_schools = (
                data[data['Library'].isnull()]
                .groupby('school_status')
                .agg(
                    num_schools=('school_name', 'count'),
                    school_names=('school_name', ', '.join)
                )
                .reset_index()
            )

            # Sort the DataFrame so that 'public' comes first
            no_library_schools = no_library_schools.sort_values(by='school_status', ascending=False)

            # Format the num_schools column
            no_library_schools['num_schools'] = no_library_schools['num_schools'].apply(lambda x: '{:,.0f}'.format(x))

            return no_library_schools

        no_library_schools_data = schools_with_no_library(data)
        st.table(no_library_schools_data[['school_status', 'num_schools']])

        # Checkbox to show school names
    #show_school_names = st.checkbox("Show School Names")
elif category=="ICT, SCIENCE AND TECHNOLOGY":
    a1, a2= st.columns(2)

    total_computers = data['total_computers'].sum()
    #st.write(f"Total Computers: {total_computers}")
    a1.metric("Total student Computers", f"{total_computers}") # sum of total_computers

    # Calculate and display the user-to-computer ratio
    total_students = data['total_students'].sum()
    user_to_computer_ratio =round( total_students / total_computers,0)
    #st.write(f"User-to-Computer Ratio: {user_to_computer_ratio:.2f}")
    a2.metric("Pupil Computer Ratio", f"{user_to_computer_ratio:.2f}")



