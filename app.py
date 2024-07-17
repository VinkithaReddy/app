import pandas as pd
import streamlit as st

# Function to read and preprocess data from Excel
def read_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to calculate datewise total duration and counts
def calculate_metrics(df):
    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Filter activities of interest (inside/outside, picking/placing)
    inside_activities = df[df['location'].str.lower() == 'inside']
    outside_activities = df[df['location'].str.lower() == 'outside']
    
    # Calculate total duration and counts datewise
    inside_duration = inside_activities.groupby('date')['time'].count()
    outside_duration = outside_activities.groupby('date')['time'].count()
    
    picking_count = df[df['activity'].str.lower() == 'picked'].groupby('date')['time'].count()
    placing_count = df[df['activity'].str.lower() == 'placed'].groupby('date')['time'].count()
    
    return inside_duration, outside_duration, picking_count, placing_count

# Streamlit app
def main():
    st.title('Activity Metrics')
    file_path = 'rawdata.xlsx'  # Update with your Excel file path
    
    # Read data
    data = read_data(file_path)
    
    # Calculate metrics
    inside_duration, outside_duration, picking_count, placing_count = calculate_metrics(data)
    
    # Display results
    st.subheader('Datewise Total Duration (Inside and Outside)')
    st.write('Inside Activities:')
    st.write(inside_duration)
    st.write('Outside Activities:')
    st.write(outside_duration)
    
    st.subheader('Datewise Number of Picking and Placing Activities')
    st.write('Picking Activities:')
    st.write(picking_count)
    st.write('Placing Activities:')
    st.write(placing_count)

if __name__ == '__main__':
    main()
