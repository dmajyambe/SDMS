import streamlit as st
st.set_page_config(
    #page_title="School Infrastructure",
    page_icon=":school:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)
from datahandler import read_data
from visualizations import*
import streamlit as st
import pandas as pd
# Button to trigger dataset upload

# Button to trigger dataset upload in the sidebar
if st.sidebar.button("Upload New Dataset"):
    data = read_data()

# Display the dataset
if "data" in locals():
    st.write("### Dataset Preview:")
    st.write(data.head())

with st.sidebar:
    #st.header("Categories")
    #navigation = st.sidebar.radio("Navigation", ["Home", "Page 1", "Page 2"])
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
        st.pyplot(plot_pupil_teacher_ratios(data=ratios_df))
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










