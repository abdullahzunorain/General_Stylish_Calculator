import streamlit as st

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app
def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #f7f7f7;
        }
        .title {
            text-align: center;
            color: #4b7bec;
            font-family: 'Arial', sans-serif;
        }
        .stButton button {
            background-color: #4b7bec;
            color: white;
            font-size: 16px;
            padding: 0.5em 1em;
            border-radius: 8px;
        }
        .result-box {
            background-color: #ebeff5;
            padding: 20px;
            margin-top: 20px;
            border-radius: 8px;
            font-weight: bold;
            color: #2d3436;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with styling
    st.markdown("<h1 class='title'>General Calculator</h1>", unsafe_allow_html=True)
    st.write("A stylish, user-friendly calculator powered by **Streamlit**.")

    # Side-by-side input layout
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
    
    with col2:
        num2 = st.number_input("Enter the second number", value=0.0, step=1.0)
    
    # Operation selection as buttons
    st.markdown("<h3>Select an operation:</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        add_clicked = st.button("➕ Add")
    
    with col2:
        sub_clicked = st.button("➖ Subtract")
    
    with col3:
        mul_clicked = st.button("✖️ Multiply")
    
    with col4:
        div_clicked = st.button("➗ Divide")

    # Perform calculation based on the selected button
    result = None
    if add_clicked:
        result = add(num1, num2)
    elif sub_clicked:
        result = subtract(num1, num2)
    elif mul_clicked:
        result = multiply(num1, num2)
    elif div_clicked:
        result = divide(num1, num2)
    
    # Display the result
    if result is not None:
        st.markdown("<div class='result-box'>The result is: {}</div>".format(result), unsafe_allow_html=True)

    # Footer with more styling
    st.markdown("""
        <hr>
        <footer style='text-align: center;'>
            <small>Made By Abdullah Zunorain❤️... using Streamlit</small>
        </footer>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
