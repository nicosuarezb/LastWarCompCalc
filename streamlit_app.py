import streamlit as st

# Function to calculate the required level 1 components
def calculate_level_1_components(components, target_level=8):
    required_components = 1  # We need 1 component of level 8
    total_level_1_needed = 0

    for level in range(target_level, 0, -1):
        if level == 1:
            total_level_1_needed += required_components
        else:
            available = components.get(level, 0)
            if available < required_components:
                missing = required_components - available
                lower_level_needed = missing * 3
                required_components = lower_level_needed
            else:
                required_components = 0

    return total_level_1_needed

# Streamlit app layout
st.title("Level 1 Component Calculator")

# User inputs for the number of components at each level
st.subheader("Enter the number of components you have for each level:")
level_1 = st.number_input("Level 1 components:", min_value=0, value=1, step=1)
level_2 = st.number_input("Level 2 components:", min_value=0, value=0, step=1)
level_3 = st.number_input("Level 3 components:", min_value=0, value=0, step=1)
level_4 = st.number_input("Level 4 components:", min_value=0, value=1, step=1)
level_5 = st.number_input("Level 5 components:", min_value=0, value=2, step=1)
level_6 = st.number_input("Level 6 components:", min_value=0, value=2, step=1)
level_7 = st.number_input("Level 7 components:", min_value=0, value=2, step=1)

# Button to calculate the required level 1 components
if st.button("Calculate"):
    # Dictionary of components entered by the user
    components = {
        1: level_1,
        2: level_2,
        3: level_3,
        4: level_4,
        5: level_5,
        6: level_6,
        7: level_7
    }

    # Perform the calculation
    level_1_needed = calculate_level_1_components(components)
    
    # Display the result
    st.success(f"Total level 1 components needed: {level_1_needed}")
