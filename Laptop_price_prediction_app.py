import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
 # Load the trained model
model = joblib.load('D:/Laptop_interface/model_of_prediction.pkl')
st.set_page_config(page_title="Laptop Price Predictor Model", page_icon="💻", layout="wide")
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(" Select a page 📖 ", ["Laptop info page"," 🏡 Prediction page", " 📊 Charts", " 💾 Storing", "Feedback"])


def laptop_info_page():
    st.markdown(
    """
    <style>
    /* Style the entire sidebar content */
    [data-testid="stSidebarContent"] {
        border: 3px solid #FFD700; /* Gold border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px; /* Padding inside border */
        background-color: #5E6B75; /* Matching background */
        color: #FFD700; /* Text color */
        }
        

        /* Style sidebar radio buttons */
    [data-testid="stSidebarContent"] label {
        font-size: 18px;
        color: #FFD700; /* Yellow text */
        display: flex;
        align-items: center;
        }


    /* Sidebar text color */
    [data-testid="stSidebar"] * { /* text color of sidebar */
        color: #FFD700;
    }
    
    </style>
    <style>
    div[data-baseweb="select"] > div{  /* set the text color */
            color: #FF7F50;
        }
    </style>
    <h1 style='color: #FF7F50;'> 💻 Laptop Configuration Guide</h1>
    <h2 style='color: #66BB6A;'>Understand different laptop specifications to make an informed decision</h2>  
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/laptop-office-plant-black-background-top-view_169016-34505.jpg");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .brand-text {
    color: #1e90ff; /* dodger Blue */ 
    font-size: 16px;
    font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
    )


    st.markdown("<span style= 'color:#00FFFF;'>♦️ Brand</span>", unsafe_allow_html=True )  
    st.markdown(""" <span class='brand-text'>A laptop’s brand determines its build quality, support, and reputation. 
    Some brands focus on durability and performance, while others emphasize design and affordability. 
    Choosing a well-known brand ensures better reliability and service availability. 
    Different brands offer unique features and software support to enhance user experience.</span>""", unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**Dell/HP/Lenovo** </span> – <span style='color: #2ca02c;'>Reliable performance, suitable for work and business use.</span>
    - <span class='brand-text'>**Apple** </span>–<span style='color: #2ca02c;'> Premium build, macOS ecosystem, and great for creative professionals.</span>
    - <span class='brand-text'>**Asus/MSI/Acer**</span> – <span style='color: #2ca02c;'> Good value options, often catering to gaming and performance needs.</span>
    - <span class='brand-text'>**Microsoft/Google**</span> – <span style='color: #2ca02c;'>Specialized laptops like Surface for productivity and Chromebooks for web-based users.</span>
    """, unsafe_allow_html=True)

    # Processor Section
    st.markdown("<span style= 'color:#00FFFF;'> ♦️ Processor (CPU)</span>", unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    Processor is the brain of the laptop. The processor is the core component that handles all tasks and operations. 
    A faster processor provides better multitasking, gaming, and software performance.
    It has multiple cores and threads, allowing smooth execution of heavy applications. 
    The processor’s efficiency also affects battery life and power consumption. Where higher numbers indicate better performance.
    Here are some common types and there inportance:</span>""",unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**Intel Core i3** –<span style='color: #2ca02c;'> Suitable for basic tasks (browsing, MS Office, streaming).</span>
    - <span class='brand-text'>**Intel Core i5** – <span style='color: #2ca02c;'> Good for multitasking and light gaming.</span>
    - <span class='brand-text'>**Intel Core i7/i9** –<span style='color: #2ca02c;'> Best for heavy tasks like programming, video editing, and gaming.</sspan>
    - <span class='brand-text'>**AMD Ryzen 3/5/7/9** – <span style='color: #2ca02c;'> Alternative to Intel with good performance at lower prices.</span>
    """, unsafe_allow_html=True)
    # RAM Section
    st.markdown("<span style= 'color:#00FFFF;'>♦️ RAM (Memory)</span>", unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    Ram is the memory,Ram  Determines how many apps one can run at once.
    RAM directly impacts how fast and smooth a laptop runs multiple applications.
    Higher RAM allows for better multitasking, gaming, and handling of large files.
    It plays a crucial role in software responsiveness and system stability. 
    Insufficient RAM can cause slow performance and frequent lag during usage.:</span>""",unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**4GB RAM**</span> –<span style='color: #2ca02c;'> Only for very basic tasks.</span>
    - <span class='brand-text'>**8GB RAM**</span> –<span style='color: #2ca02c;'> Recommended for general users.</span>
    - <span class='brand-text'>**16GB RAM**</span> – <span style='color: #2ca02c;'>Best for professionals and gamers.</span>
    - <span class='brand-text'>**32GB+ RAM** </span>– <span style='color: #2ca02c;'>Required for high-end tasks like 3D rendering.</span>
    """, unsafe_allow_html=True)
    # Storage Section
    st.markdown("<span style= 'color:#00FFFF;'>♦️ Storage Type</span>", unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    Laptops come with HDD (slower, more storage) or SSD (faster, better performance). 
    Storage determines how much data, applications, and files a laptop can hold. 
    There are different types of storage, with some offering higher speed and efficiency than others. 
    Choosing the right storage ensures faster boot times and smoother performance.
    Some laptops offer expandable or hybrid storage options for flexibility.</span>""",unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**HDD (Hard Disk Drive)**</span> –<span style='color: #2ca02c;'> Slower but offers more storage at a lower price.</sapn>
    - <span class='brand-text'>**SSD (Solid State Drive)**</span> – <span style='color: #2ca02c;'>Much faster and improves overall laptop speed.</span>
    - <span class='brand-text'>**Hybrid (HDD + SSD)**</span> –<span style='color: #2ca02c;'> A mix of both for better performance.</span>
    """, unsafe_allow_html=True)
    # Operating System Section
    st.markdown("<span style= 'color:#00FFFF;'>♦️ Operating System", unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    The operating system controls the interface, software compatibility, and overall usability of a laptop.
    Different systems offer unique features, security, and performance optimizations. 
    It affects how applications run and how user-friendly the experience is.
    The right OS depends on personal preference and required functionality.</span>""", unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**Windows** </span>–<span style='color: #2ca02c;'> Most common, supports a wide range of applications and gaming.</span>
    - <span class='brand-text'>**macOS**</span> –<span style='color: #2ca02c;'> Found in Apple laptops, optimized for creative professionals.</span>
    - <span class='brand-text'>**Linux**</span> – <span style='color: #2ca02c;'>Preferred by developers for customization and security.</span>
    - <span class='brand-text'>**ChromeOS**</span> –<span style='color: #2ca02c;'> Lightweight OS for web-based tasks, mainly on Chromebooks.</span>
    """, unsafe_allow_html=True)
    # Processor Generation
    st.markdown("<span style= 'color:#00FFFF;'>♦️ Processor Generation </span>",unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    Processor generation defines the efficiency, speed, and new features of a laptop’s CPU. 
    Newer generations offer better performance, improved battery life, and advanced technology. 
    It enhances the laptop’s ability to handle modern applications and multitasking. 
    Upgrading to a higher generation provides better long-term usability and future-proofing.</span>""",unsafe_allow_html=True)
    st.markdown(""" 
    - <span class='brand-text'>**Intel 8th-10th Gen**</span> –<span style='color: #2ca02c;'> Suitable for basic use and budget-friendly options.</span>
    - <span class='brand-text'>**Intel 11th-12th Gen**</span> –<span style='color: #2ca02c;'> Improved speed, battery efficiency, and AI support.</span>
    - <span class='brand-text'>**Intel 13th-14th Gen**</span> – <span style='color: #2ca02c;'>Latest performance with advanced AI processing and power optimization.</span>
    - <span class='brand-text'>**AMD Ryzen 3000-7000 Series**</span> –<span style='color: #2ca02c;'> Competitive alternative to Intel with good efficiency.</span>
    """, unsafe_allow_html=True)
    # Storage Capacity
    st.markdown( "<span style= 'color:#00FFFF;'>♦️ Storage Capacity</span>", unsafe_allow_html=True)
    st.markdown(""" <span class='brand-text'>
    Storage capacity determines how much data, applications, and media files a laptop can hold. 
    A larger capacity is useful for storing high-resolution videos, software, and documents. 
    Different storage types like HDDs and SSDs affect speed and reliability. 
    Choosing the right capacity ensures smooth performance and enough space for future needs.</span>""",unsafe_allow_html=True)
    st.markdown("""
    - <span class='brand-text'>**HDD (Hard Disk Drive)**</span> –<span style='color: #2ca02c;'> Affordable, large capacity, but slower speeds.</span>
    - <span class='brand-text'>**SSD (Solid State Drive)**</span> –<span style='color: #2ca02c;'> Faster performance, better durability, but costlier.</span>
    - <span class='brand-text'>**256GB-512GB SSD**</span> –<span style='color: #2ca02c;'> Suitable for most users with cloud storage support.</span>
    - <span class='brand-text'>**1TB+ HDD/SSD**</span> –<span style='color: #2ca02c;'> Ideal for gaming, video editing, or large file storage.</span>
    """, unsafe_allow_html=True)
    # Screen size
    st.markdown(" <span style= 'color:#00FFFF;'> ♦️ Screen Size</span>", unsafe_allow_html=True)
    st.markdown("""<span class='brand-text'>
    Screen size affects portability, viewing experience, and usability. 
    Larger screens provide better visuals for entertainment, gaming, and professional work, 
    while smaller screens improve portability and battery efficiency. The ideal size depends on personal preference and usage needs. 
    A good screen enhances productivity and reduces eye strain.</span>""",unsafe_allow_html=True)


    st.markdown("""
    - <span class='brand-text'>**11-13 inches**</span> –<span style='color: #2ca02c;'> Ultra-portable, ideal for travel and basic tasks.</span>
    - <span class='brand-text'>**14 inches**</span> –<span style='color: #2ca02c;'> Balanced between portability and usability.</span>
    - <span class='brand-text'> **15.6 inches**</span> –<span style='color: #2ca02c;'> Standard size, suitable for work and entertainment.</span>
    - <span class='brand-text'>**17+ inches**</span> –<span style='color: #2ca02c;'>  Large display, best for gaming, video editing, or professional use.</span>
    """, unsafe_allow_html=True)

   
    
    st.success("🔎 Tip: Always check for upgrade options when buying a laptop!")


def home_page():
    df = pd.read_csv("D:/final_laptop_datascrape.csv")
    #Ram correction
    df['RAM_Size'] = df['RAM_Size'].str.extract('(\d+)')
    df['RAM_Size'] = df['RAM_Size'].replace('Not Available', 0)
   #df['RAM_Size'] = df['RAM_Size'].str.replace('GB DDR5 RAM',' ')
#df['RAM_Size'] = df['RAM_Size'].str.replace('GB DDR4 RAM',' ')
    df['RAM_Size'] = df['RAM_Size'].fillna(0)  # Fill NaN values with 0
    df['RAM_Size'] = df['RAM_Size'].astype('int32')
    df['Screen_Size_Inches'].astype(float)

#Processor_Generation
    df['Processor_Generation'] = df['Processor_Generation'].str.extract('(\d+)')
    df['Processor_Generation'] = df['Processor_Generation'].replace('Not Available', 0) 
    df['Processor_Generation'] = df['Processor_Generation'].fillna(0)
    df['Processor_Generation'].fillna(0)
    df['Processor_Generation'] = df['Processor_Generation'].astype('int32')

#review

    df['Reviews'] = df['Reviews'].replace('Not Available', 0)
    df['Reviews'] = df['Reviews'].fillna(0)
    df['Reviews']=df['Reviews'].astype('float64')


#converting storage capacity from TB to GB
    print(df['Storage_Capacity'])
    print("Unique values before conversion:", df['Storage_Capacity'].unique())

# Function to convert storage capacity to GB
    def convert_to_gb(Storage_Capacity):
        if pd.isna(Storage_Capacity):
            return np.nan
        Storage_Capacity = str(Storage_Capacity).strip().upper()  # Normalize case and strip spaces

    # Remove any unexpected characters or additional spaces
        Storage_Capacity = Storage_Capacity.replace(' ', '').replace('GB', ' GB').replace('TB', ' TB')

    # Handle "Not Available"
        if Storage_Capacity == 'Not Available' or Storage_Capacity == '0':
            return np.nan  # Optionally replace '0' with NaN to handle it later

    # Convert TB to GB
        if 'TB' in Storage_Capacity:
            return float(Storage_Capacity.replace('TB', '').strip()) * 1024  # Convert TB to GB
        elif 'GB' in Storage_Capacity:
            return float(Storage_Capacity.replace('GB', '').strip())
        else:
            return np.nan  # Handle unexpected formats

# Apply conversion function
    df['Storage_Capacity'] = df['Storage_Capacity'].apply(convert_to_gb)

# Replace NaN values with 0 (for 'Not Available')
    df['Storage_Capacity'] = df['Storage_Capacity'].fillna(0).astype('int32')

    df["urls"] = df["urls"].astype(str)

    st.markdown(
    """
    <style>
    /* Style the entire sidebar content */
    [data-testid="stSidebarContent"] {
        border: 3px solid #FFD700; /* Gold border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px; /* Padding inside border */
        background-color: #5E6B75; /* Matching background */
        color: #FFD700; /* Text color */
        }
        

        /* Style sidebar radio buttons */
    [data-testid="stSidebarContent"] label {
        font-size: 18px;
        color: #FFD700; /* Yellow text */
        display: flex;
        align-items: center;
        }


    /* Sidebar text color */
    [data-testid="stSidebar"] * { /* text color of sidebar */
        color: #FFD700;
    }
    
    </style>
    <style>
    div[data-baseweb="select"] > div{  /* set the text color */
            color: #FF7F50;
        }

    
    </style>
    <h1 style='color: #FF7F50;'>Laptop Price Prediction</h1>
    <h2 style='color: #66BB6A;'>Enter the Required features Values to predict Laptop Price</h2>
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/laptop-office-plant-black-background-top-view_169016-34505.jpg");  
        background-size: cover;            /* Change this to your desired background color */
        background-position: center;
        background-repeat: no-repeat;/* Change this to your desired "background-color "to change color */
    }
    .stNumberInput label {
        color: #00FFFF; 
        }
    .stTextInput label{
        color: #00FFFF;
    }
    .stSelectbox > label{
         color: #00FFFF;
     }
     .stNumberInput input {
        color: #FF7F50; 
        }
    .stTextInput input{
        color: #FF7F50;
    }
    
    .stButton > button {        
        background-color: black;  /* Change text color to gold */
        color: white; 
    }
    '''.predict { 
        font-size: 20px; 
        font-weight: bold; 
        color: blue; 
    }'''
    
    </style>
    """,
    unsafe_allow_html=True
    )
# 🔹 **Auto-Fill Based on Laptop Selection**
    selected_laptop = st.selectbox("Select a Laptop Processor For autofilling", df["Processor_Type"].unique())

    # Extract default values for the selected laptop
    default_values = df[df["Processor_Type"] == selected_laptop].iloc[0] if selected_laptop in df["Processor_Type"].values else None



# Brand (string)
    Brand = st.selectbox("Brand",["brand ","ASUS","Acer","Apple","CHUWI","Colorful","DELL","FUTOPIA","HP","Infinix","Lenovo","MICROSOFT","MSI","Primebook","SAMSUNG","Thomson","Ultimus","ZEBRONICS","realme","walker"] ,index =["brand ","ASUS","Acer","Apple","CHUWI","Colorful","DELL","FUTOPIA","HP","Infinix","Lenovo","MICROSOFT","MSI","Primebook","SAMSUNG","Thomson","Ultimus","ZEBRONICS","realme","walker"].index(default_values["Brand"]) if default_values is not None else 0)
    # Reviews (convert to float)
    Reviews = st.number_input("Reviews", min_value=0.0, format="%.1f",value=float(default_values["Reviews"]) if default_values is not None else 0.0)

# Processor Type
    Processor_Type = st.selectbox("Processor Type", sorted(df["Processor_Type"].unique()),index=sorted(df["Processor_Type"].unique()).index(default_values["Processor_Type"]) if default_values is not None else 0)

# RAM Size (convert to int)
    RAM_Size = st.selectbox("RAM Size (GB)", [0, 2, 4, 6, 8, 12, 16, 24, 32, 64], index=[0, 2, 4, 6, 8, 12, 16, 24, 32, 64].index(int(default_values["RAM_Size"])) if default_values is not None else 0)
# Storage Capacity (convert to int)
    Storage_Capacity = st.selectbox("Storage Capacity (in GB)", [0, 256, 512, 1024, 2048],index=[0, 256, 512, 1024, 2048].index(int(default_values["Storage_Capacity"])) if default_values is not None else 0)
# Storage Type (string)
    Storage_Type = st.selectbox("Storage Type", ["select Storage type ","HDD", "SSD"],index=["select Storage type","HDD", "SSD"].index(default_values["Storage_Type"]) if default_values is not None else 0)

# Screen Size (convert to float)
    Screen_Size_Inches = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1,format="%.1f",value=float(default_values["Screen_Size_Inches"]) if default_values is not None else 10.0)

# Operating System (string)
    Operating_System = st.selectbox("Operating System", ["opearing system","Windows 11", "Windows 10", "Linux", "MacOS"], index=["opearing system","Windows 11", "Windows 10", "Linux", "MacOS"].index(default_values["Operating_System"]) if default_values is not None else 0) 
# Processor Generation (convert to int)
    Processor_Generation = st.selectbox("Processor Generation", [0, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 0], index=[0, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 0].index(int(default_values["Processor_Generation"])) if default_values is not None else 0)

# 🔹 **Predict Price & Find Laptop Link**
    if st.button("Predict"):
    # Create a DataFrame from the user input
        features = pd.DataFrame([[Reviews, Brand, Processor_Type, RAM_Size, Storage_Capacity, Storage_Type, 
                              Screen_Size_Inches, Operating_System, Processor_Generation]],
                            columns=['Reviews', 'Brand', 'Processor_Type', 'RAM_Size', 
                                     'Storage_Capacity', 'Storage_Type', 'Screen_Size_Inches', 
                                     'Operating_System', 'Processor_Generation'])

    # Make a prediction using the model
        prediction = model.predict(features)

        st.markdown( f"<span style='font-size:20px; font-weight:bold; color:#BBDEFB;'> Predicted Price: ${prediction[0]:.2f}</span>", unsafe_allow_html=True)

    # Filter dataset to find the laptop link based on user selection
        matched_laptops = df[
        (df["Brand"] == Brand) & 
        (df["Processor_Type"] == Processor_Type) & 
        (df["RAM_Size"] == RAM_Size) & 
        (df["Storage_Capacity"] == Storage_Capacity) & 
        (df["Storage_Type"] == Storage_Type) & 
        (df["Screen_Size_Inches"] == float(Screen_Size_Inches)) & 
        (df["Operating_System"] == Operating_System) & 
        (df["Processor_Generation"] == Processor_Generation)
        ]

        if not matched_laptops.empty:
            product_url = matched_laptops["urls"].values[0]  # Get the first matching URL
            st.markdown(f"[Click here to view this laptop on Flipkart]({product_url})", unsafe_allow_html=True)
        else:
            st.write("Laptop link not found for the given configuration.")


def Charts_page():
    st.markdown(
    """
    <style>
    /* Style the entire sidebar content */
    [data-testid="stSidebarContent"] {
        border: 3px solid #FFD700; /* Gold border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px; /* Padding inside border */
        background-color: #5E6B75; /* Matching background */
        color: #FFD700; /* Text color */
        }
        

        /* Style sidebar radio buttons */
    [data-testid="stSidebarContent"] label {
        font-size: 18px;
        color: #FFD700; /* Yellow text */
        display: flex;
        align-items: center;
        }


    /* Sidebar text color */
    [data-testid="stSidebar"] * { /* text color of sidebar */
        color: #FFD700;
    }
    
    </style>
    <h1 style='color: #FF7F50;'>Laptop Feature Charts</h1>
    <h2 style='color: #66BB6A;'>Plotting a bar charts for the feature columns...</h2>
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/laptop-office-plant-black-background-top-view_169016-34505.jpg");  
        background-size: cover;            /* Change this to your desired background color */
        background-position: center;
        background-repeat: no-repeat;/* Change this to your desired "background-color "to change color */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

# Upload Excel file
    # Specify the file path (replace with your file path)
    file_path = "D:/final_laptop_datascrape.csv"

# Load the CSV file directly using pandas
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df['Prices'] = df['Prices'].astype(str).str.replace(',', '').str.strip()
    df['Prices'] = pd.to_numeric(df['Prices'], errors='coerce')
    df = df.dropna(subset=['Prices'])
    
    
    # Use Streamlit columns to organize plots
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    with col1:
    # First plot
        plt.figure(figsize=(6, 4))
        df['Brand'].value_counts().plot(kind="bar", color='teal')
        plt.title('Frequency of Laptop Brands', color='purple')
        plt.xlabel('Brand', color='blue')
        plt.ylabel('Frequency', color= 'blue')
        plt.tick_params(axis='y', colors='red')
        plt.tick_params(axis='x', colors='red')  
        st.pyplot(plt)

    with col2:
    # Second plot
        plt.figure(figsize=(6, 4.5))
        top_5_prices = df['Prices'].dropna().value_counts().nlargest(5)
        top_5_prices.plot(kind='bar',color='teal')
        plt.title('Top 5 Laptop Prices',color='purple')
        plt.xlabel('Price' ,color='blue')
        plt.ylabel('Frequency', color='blue')
        plt.tick_params(axis='y', colors='red')
        plt.tick_params(axis='x', colors='red')
        st.pyplot(plt)
    with col3:
        mode_os = df['Operating_System'].mode()[0]  # Get the mode
        df['Operating_System'] = df['Operating_System'].replace('Not Available', mode_os)
        avg_price_by_os = df.groupby('Operating_System')['Prices'].mean().reset_index()

# Plot using Seaborn's barplot
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Operating_System', y='Prices', data=avg_price_by_os, palette='husl')

# Rotate the x-axis labels for better readability
        plt.xticks(rotation=90)
        plt.title('Average Price of Laptops by Operating System', color='purple')
        plt.xlabel('Operating System',color='blue')
        plt.ylabel('Average Price',color='blue')
        plt.tick_params(axis='y', colors='red')
        plt.tick_params(axis='x', colors='red')

# Display the plot in Streamlit
        st.pyplot(plt)
    with col4:
        mode_os = df['Storage_Capacity'].mode()[0]  # Get the mode
        df['Storage_Capacity'] = df['Storage_Capacity'].replace('Not Available', mode_os)
        avg_price_by_os = df.groupby('Storage_Capacity')['Prices'].mean().reset_index()

# Plot using Seaborn's barplot
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Storage_Capacity', y='Prices', data=avg_price_by_os, palette='husl')

# Rotate the x-axis labels for better readability
        plt.xticks(rotation=90)
        plt.title('Average Price of Laptops by Storage_Capacity',color='purple')
        plt.xlabel('Storage_Capacity',color='blue')
        plt.ylabel('Average Price',color='blue')
        plt.tick_params(axis='y', colors='red')
        plt.tick_params(axis='x', colors='red')
        
# Display the plot in Streamlit
        st.pyplot(plt)



def Storing_page():



    st.markdown(
    """
    <style>
    /* Style the entire sidebar content */
    [data-testid="stSidebarContent"] {
        border: 3px solid #FFD700; /* Gold border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px; /* Padding inside border */
        background-color: #5E6B75; /* Matching background */
        color: #FFD700; /* Text color */
        }
        

        /* Style sidebar radio buttons */
    [data-testid="stSidebarContent"] label {
        font-size: 18px;
        color: #FFD700; /* Yellow text */
        display: flex;
        align-items: center;
        }


    /* Sidebar text color */
    [data-testid="stSidebar"] * { /* text color of sidebar */
        color: #FFD700;
    }
    
    </style>

    <h1 style='color: #FF7F50;'>Store the Laptop Configuration along with the Predicted price</h1>
    <h2 style='color: #66BB6A;'>Enter the Configuration to store that data in .csv file</h2>
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/laptop-office-plant-black-background-top-view_169016-34505.jpg");  /* Change this to your desired background color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .stNumberInput label {
        color: #00FFFF;   /* light blue */
    }
    .stTextInput label{
        color: #00FFFF;
    }
    .stNumberInput input {
        color: #FF7F50; 
    }
    .stTextInput input{
        color: #FF7F50;
    }
    .stButton > button {        
        background-color: black;  /* Change text color to gold */
        color: white; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # User input for configuration
    Review = st.number_input("Enter the Review")
    brand = st.text_input("Enter the brand")
    processor_type = st.text_input("Enter the processor type")
    ram_size = st.number_input("Enter the RAM size")
    storage_capacity = st.text_input("Enter the storage Type")
    Storage_Type = st.number_input("Enter the Storage capacity")
    Screen_Size_Inches = st.number_input("Enter the Screen size (in inches)")
    Operating_System = st.text_input("Enter the Operating System")
    Processor_Generation = st.number_input("Enter the Processor Generation")
    predicted_price = st.number_input("Predicted Price", value=0)

# Button to save data to CSV
    if st.button("Save Data"):
    # Create a DataFrame with user input
        new_data = pd.DataFrame({
        'Review' : [Review],
        'Brand': [brand],
        'Processor Type': [processor_type],
        'RAM Size': [ram_size],
        'Storage Capacity': [storage_capacity],
        'Storage Type' : [Storage_Type],
        'Screen size (in inches)': [Screen_Size_Inches],
        'Operating System': [Operating_System],
        'Processor Generation': [Processor_Generation],
        'Predicted Price': [predicted_price]
        })

    # Append to CSV (create new file if it doesn't exist)
        if not brand.strip():
            st.warning("⚠ Please Fill the complete form.") 
        else:
            st.markdown("<span style='color:#BBDEFB;'>Data saved to CSV!</span>", unsafe_allow_html=True)

        new_data.to_csv('user_data.csv', mode='a', header=not pd.io.common.file_exists('user_data.csv'), index=False)
        

def feedback_page():
    st.markdown(
    """
    <h1 style='color: #FF7F50;'>Feedback</h1>
    <h2 style='color: #66BB6A;'>💬 Laptop Review & Feedback</h2>

    <style>
    /* Style the entire sidebar content */
    [data-testid="stSidebarContent"] {
        border: 3px solid #FFD700; /* Gold border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px; /* Padding inside border */
        background-color: #5E6B75; /* Matching background */
        color: #FFD700; /* Text color */
        }
        

        /* Style sidebar radio buttons */
    [data-testid="stSidebarContent"] label {
        font-size: 18px;
        color: #FFD700; /* Yellow text */
        display: flex;
        align-items: center;
        }


    /* Sidebar text color */
    [data-testid="stSidebar"] * { /* text color of sidebar */
        color: #FFD700;
    }
    
    </style>
    <style>
    div[data-baseweb="select"] > div{  /* set the text color */
            color: #FF7F50;
        }
    </style>
    
        
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/laptop-office-plant-black-background-top-view_169016-34505.jpg");  
        background-size: cover;            /* Change this to your desired background color */
        background-position: center;
        background-repeat: no-repeat;/* Change this to your desired "background-color "to change color */
    }
 
    .stTextInput label{
        color: #00FFFF;
    }
    .stSelectbox > label{
         color: #00FFFF;
     }
     
    .stTextInput input{
    color: #FF7F50;
    }
    .stSlider label {
        color: #00FFFF; /* Coral color */
       
    }
    
    .stTextArea label {
       color: #00FFFF
    }
    
    .stTextArea textarea{
      color: #FF7F50;
    }

    
    .stButton > button {        
    background-color: black;  /* Change text color to gold */
    color: white; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    FEEDBACK_FILE = "feedback.csv"
    def load_feedback():
        if os.path.exists(FEEDBACK_FILE):
            return pd.read_csv(FEEDBACK_FILE)
        return pd.DataFrame(columns=["email","status","age", "Experience ", "Rating", "Pros", "Cons", "Feedback", "Purchase Platform"])

    def save_feedback(email,status,age, experience, rating, pros, cons, feedback, platform):
        new_entry = pd.DataFrame([[ email,status,age,experience, rating, pros, cons, feedback, platform]], columns=["Email","status","age", "Experience Level", "Rating", "Pros", "Cons", "Feedback", "Purchase Platform"])
        if os.path.exists(FEEDBACK_FILE):
            df = pd.read_csv(FEEDBACK_FILE)
            df = pd.concat([df, new_entry], ignore_index=True)
        else:
            df = new_entry
        df.to_csv(FEEDBACK_FILE, index=False)
    
    def is_valid_email(email):
        """Check if the email is in a valid format using regex"""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email)
    
    def is_valid_age(age):
        """Ensure age is a valid positive integer and not zero."""
        try:
            age = int(age)  # Convert to integer
            return age > 0  # Check if greater than 0
        except ValueError:
            return False  # Return False if conversion fails


    # Input fields
    email = st.text_input("Your Email (Required)")
    age = st.text_input("Please specify your age")
    status = st.selectbox("Your Status",[" ","Student","Employee","Other"])
    experience = st.selectbox("User Experience ", [" ","Poor", "Good","Average", "Very Good","Nice"])
    rating = st.slider("Rating (1-5)", 1, 5, 3)
    pros = st.text_area("Pros (What you liked)")
    cons = st.text_area("Cons (What you didn't like)")
    feedback = st.text_area("Detailed Review")
    platform = st.selectbox("Where did you buy?", [" ","Flipkart", "Amazon", "Official Store", "Other"])

    # Submit button
    if st.button("Submit Feedback"):
        if not email.strip() or not is_valid_email(email):
            st.warning("⚠ Please enter a valid email address.")
        elif not feedback.strip():
            st.warning("⚠ Please provide us your detailed review") 
        elif not status.strip():
            st.warning("⚠ Please fill in all required fields.")
        elif not experience.strip():
            st.warning("⚠ Please fill in all required fields.")
        elif not platform.strip():
            st.warning("⚠ Please fill in all required fields.")
        elif not is_valid_age(age):
            st.warning("❌ Please enter a valid age greater than 0.")
        else:
            save_feedback(email,status,age,experience, rating, pros, cons, feedback, platform)
            st.success("✅ Thank you for your feedback!")

     
        



   





# Display the selected page
if page == "Laptop info page":
    laptop_info_page()
elif page == " 🏡 Prediction page":
    home_page()  # Calls the function to render the Home page
elif page == " 📊 Charts":
    Charts_page()  # Calls the function to render the Recommendations page
elif page == " 💾 Storing":
    Storing_page()
elif page == "Feedback":
    feedback_page()
