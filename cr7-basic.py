import streamlit as st

# Function to display biography
def show_biography():
    st.write(
        """
        **Cristiano Ronaldo** is a Portuguese professional footballer widely regarded as one of the greatest footballers of all time. Born on February 5, 1985, in Funchal, Madeira, Portugal, Ronaldo has won numerous accolades throughout his career, including multiple FIFA Ballon d'Or awards. Known for his incredible goal-scoring ability, athleticism, and versatility on the field, Ronaldo has achieved remarkable success with clubs like Manchester United, Real Madrid, and Juventus, as well as the Portugal national team.

        Ronaldo's relentless drive for excellence and his commitment to the game have made him a global icon and an inspiration to aspiring athletes worldwide. His contributions to football continue to captivate fans around the globe.
        """
    )

# Function to display stats
def show_stats():
    st.write(
        """
        **Career Statistics:**
        - Goals Scored: 700+
        - Major Trophies: 30+
        - Ballon d'Or Awards: 5
        - UEFA Champions League Titles: 5
        """
    )

# Function to display interactive elements
def show_interactive():
    st.write("## Interactive Section")
    st.slider("Select a year", 2000, 2024, 2024)
    st.button("Click me!")

# Function to display profile picture
def show_profile_picture():
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Cristiano_Ronaldo_2018_%28cropped%29.jpg", width=600)

# Main app function
def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Select a page:", ["Home", "Biography", "Statistics", "Interactive", "Profile"])

    # Main content based on selection
    if option == "Home":
        st.title("Cristiano Ronaldo")
        st.write("Welcome to the Cristiano Ronaldo fan page!")
    
    elif option == "Biography":
        st.title("Biography")
        show_biography()
    
    elif option == "Statistics":
        st.title("Statistics")
        show_stats()
    
    elif option == "Interactive":
        st.title("Interactive Section")
        show_interactive()
    
    elif option == "Profile":
        st.title("Profile Picture")
        show_profile_picture()

if __name__ == "__main__":
    main()
