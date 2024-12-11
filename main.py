# Third party imports here
import streamlit as st
import time
# Local imports here
from pinecone_service import query_from_pinecone


# Streamlit App
def main():
    """
    Main function for the Streamlit app.

    This function displays a title for the app, an input field for the user to enter their query, 
    and a button to trigger the query. When the button is clicked, it calls the query_from_pinecone function
    and displays the result in a square container.

    :return: None
    """
    if "processing" not in st.session_state:
        st.session_state["processing"] = False

    if "input_message" not in st.session_state:
        st.session_state["input_message"] = ""

    if "query_output" not in st.session_state:
        st.session_state["query_output"] = ""

    def send_action():
        if st.session_state["processing"]:
            return

        if not st.session_state["input_message"].strip():
            st.warning("Query is required.")
            return

        st.session_state["processing"] = True
        st.session_state["query_output"] = ""

        # Call the query_from_pinecone function
        st.session_state["query_output"] = query_from_pinecone(
            st.session_state["input_message"])

        st.session_state["processing"] = False

    st.title('Query App')

    # Using a form so that Enter triggers submission as well as the button
    # Query input and button inside the form
    st.text_input(
        "Enter your query:",
        key="input_message",
        disabled=st.session_state["processing"]
    )
    st.button(
        "Submit", disabled=st.session_state["processing"], on_click=send_action)

    # Display the query output in a square container after submit
    if st.session_state["query_output"]:
        with st.container():
            # Using a square container with a border for the output
            st.markdown(
                f'<div style="border: 2px solid black; padding: 20px; border-radius: 10px; width: 100%; max-width: 400px; background-color: #f9f9f9;">'
                f'<h3>Query Results:</h3>'
                # Display the query result
                f'<pre>{st.session_state["query_output"]}</pre>'
                f'</div>', unsafe_allow_html=True
            )


if __name__ == "__main__":
    main()

    # if st.button("Submit"):
    #     if user_input:
    #         # Call the Pinecone query function with the user input
    #         result = query_from_pinecone(user_input)
    #         st.write("Query Results:")
    #         st.json(result)  # Display the result in a readable format
    #     else:
    #         st.warning("Please enter a query.")
