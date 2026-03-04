import streamlit as st
from huggingface_hub import InferenceClient

# Page config
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Planner for Students")
st.write("Generate a smart travel itinerary using AI.")

# User inputs
destination = st.text_input("Destination")
budget = st.number_input("Budget (₹)", min_value=1000)
duration = st.number_input("Trip Duration (Days)", min_value=1)
preferences = st.text_area("Travel Preferences")

# Generate button
if st.button("Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
    else:

        prompt = f"""
Create a detailed student travel itinerary.

Destination: {destination}
Budget: ₹{budget}
Duration: {duration} days
Preferences: {preferences}

Include:
- Day wise itinerary
- Budget accommodation
- Cheap food options
- Transport suggestions
- Cost breakdown
- Money saving tips
"""

        try:
            client = InferenceClient(
                token=st.secrets["HF_API_KEY"]
            )

            with st.spinner("Generating travel plan..."):

                response = client.chat_completion(
                    model="meta-llama/Meta-Llama-3-8B-Instruct",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500
                )

            result = response.choices[0].message.content

            st.subheader("🌍 Your Travel Plan")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")