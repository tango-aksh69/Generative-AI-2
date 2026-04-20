import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(page_title="AI Story & Poem Generator", page_icon="✨")

st.title("✨ AI Story & Poem Generator")
st.write("Generate creative stories and poems using AI!")

# API Key input
api_key = st.text_input("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", type="password", placeholder="sk-...")

st.divider()

# Choose what to generate
option = st.selectbox("What do you want to generate?", ["Story", "Poem"])

# User prompt
prompt = st.text_area("Enter your idea or topic", placeholder="e.g. A dragon who is afraid of fire...")

# Extra options
if option == "Story":
    genre = st.selectbox("Choose a genre", ["Fantasy", "Mystery", "Romance", "Horror", "Adventure"])
    length = st.selectbox("Story length", ["Short", "Medium", "Long"])
else:
    style = st.selectbox("Choose poem style", ["Rhyming", "Haiku", "Free Verse", "Limerick"])

# Generate button
if st.button("Generate"):

    # Check inputs
    if not api_key:
        st.warning("Please enter your OpenAI API Key.")
    elif not prompt:
        st.warning("Please enter a topic or idea.")
    else:
        # Build the prompt
        if option == "Story":
            word_map = {"Short": "100", "Medium": "250", "Long": "400"}
            words = word_map[length]
            user_prompt = f"Write a {genre} story of about {words} words based on this idea: {prompt}"
        else:
            user_prompt = f"Write a {style} poem about: {prompt}"

        # Call OpenAI API
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=600
            )

            result = response.choices[0].message.content

            # Show the result
            st.subheader("Generated Output")
            st.write(result)

            # Download button
            st.download_button(
                label="Download as Text File",
                data=result,
                file_name="output.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")