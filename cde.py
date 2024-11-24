import streamlit as st

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = "Error"
    return result

def main():
    st.title("Calculator")

    # Initialize session state
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    if 'display_key' not in st.session_state:
        st.session_state.display_key = 0

    # Input display
    st.text_input("Enter expression", key="display", value=st.session_state.expression, disabled=True)

    # Function to handle button clicks
    def handle_click(button):
        if button == "=":
            st.session_state.expression = evaluate_expression(st.session_state.expression)
        elif button == "C":
            st.session_state.expression = ""
        else:
            st.session_state.expression += button
        st.session_state.display_key += 1
        st.rerun()

    # Buttons with symbols (using Unicode escape sequences)
    buttons = [
        '7', '8', '9', '\u00F7',  # Division symbol ÷
        '4', '5', '6', '+',  # Plus symbol +
        '1', '2', '3', '\u00D7',  # Multiplication symbol ×
        '0', '.', '=', '\u2212',  # Minus symbol −
        'C'
    ]

    # Display buttons in a grid
    cols = st.columns(4)
    for i, button in enumerate(buttons):
        with cols[i % 4]:
            if st.button(button, key=f"button_{button}_{st.session_state.display_key}"):
                handle_click(button)

if __name__ == "__main__":
    main()
