import streamlit as st
from transformers import pipeline

# -------------------------------------------------
# PAGE TITLE
# -------------------------------------------------

st.set_page_config(
    page_title="LLM Playground",
    page_icon="🤖"
)

st.title("🤖 LLM Playground")
st.write("Enter a Hugging Face model and prompt to generate a response.")

# -------------------------------------------------
# MODEL NAME
# -------------------------------------------------

model_name = st.text_input(
    "Hugging Face Model Name",
    value="Qwen/Qwen2.5-1.5B-Instruct"
)

# -------------------------------------------------
# PIPELINE
# -------------------------------------------------

pipeline_type = st.selectbox(
    "Transformers Pipeline",
    ["text-generation"]
)

# -------------------------------------------------
# SYSTEM PROMPT
# -------------------------------------------------

system_prompt = st.text_area(
    "System Prompt",
    value="""You are a friendly AI tutor.
Explain technical concepts in simple language.
Use real-world examples."""
)

# -------------------------------------------------
# USER PROMPT
# -------------------------------------------------

user_prompt = st.text_area(
    "User Prompt",
    value="Explain Machine Learning to a beginner."
)

# -------------------------------------------------
# GENERATE BUTTON
# -------------------------------------------------

if st.button("🚀 Generate Response"):

    if model_name.strip() == "":
        st.error("Please enter a Hugging Face model name.")

    elif user_prompt.strip() == "":
        st.error("Please enter a user prompt.")

    else:

        with st.spinner("Loading model and generating response..."):

            try:

                # Load selected Hugging Face model
                generator = pipeline(
                    pipeline_type,
                    model=model_name
                )

                # Create chat-style messages
                messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

                # Generate response
                response = generator(
                    messages,
                    max_new_tokens=150,
                    temperature=0.7,
                    do_sample=True
                )

                # Extract final response
                answer = response[0]["generated_text"][-1]["content"]

                # Display result
                st.subheader("🤖 AI Response")
                st.write(answer)

            except Exception as e:

                st.error("Something went wrong.")

                st.code(str(e))
```
