import streamlit as st

st.title("Feet and Inches Calculator")

# Initialize session state
if 'num_inputs' not in st.session_state:
    st.session_state.num_inputs = 1

# Operation selection
operation = st.radio(
    "Select Operation",
    ["Add", "Subtract"],
    horizontal=True
)

# Reset button
if st.button("Reset", use_container_width=True):
    st.session_state.num_inputs = 1
    st.rerun()

st.markdown("---")
total_inches = None

def add_new_input():
    st.session_state.num_inputs += 1

# Handle inputs dynamically
for i in range(st.session_state.num_inputs):
    st.subheader(f"Distance #{i+1}")
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        feet = st.number_input(
            "Feet",
            min_value=0.0,
            value=0.0,
            key=f"feet_{i}",
            on_change=add_new_input if i == st.session_state.num_inputs - 1 else None
        )
    with col2:
        inches = st.number_input(
            "Inches",
            min_value=0.0,
            max_value=11.0,
            value=0.0,
            key=f"inches_{i}"
        )
    with col3:
        if i == st.session_state.num_inputs - 1:  # Only show Next button for last row
            if st.button("Next", key=f"next_{i}"):
                add_new_input()

    # Calculate running total
    current_value = (feet * 12) + inches
    if total_inches is None:
        total_inches = current_value
    else:
        if operation == "Add":
            total_inches += current_value
        else:
            total_inches -= current_value

st.markdown("---")
if st.button("Calculate", use_container_width=True):
    if total_inches is not None:
        # Handle negative results
        if total_inches < 0:
            total_inches = abs(total_inches)
            sign = "-"
        else:
            sign = ""
            
        result_feet = total_inches // 12
        result_inches = total_inches % 12
        
        st.success(f"Result: {sign}{int(result_feet)} feet {int(result_inches)} inches")

# Add some helpful information
st.markdown("---")
st.markdown("**Note:** 1 foot = 12 inches")
