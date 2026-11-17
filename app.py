
import streamlit as st

st.set_page_config(
    page_title="FitLife - Gym & Diet Planner",
    page_icon="💪",
    layout="wide"
)

st.title("💪 FitLife - Gym & Diet Planner")
st.write("Your personal fitness and nutrition assistant")

st.divider()

# PERSONAL DETAILS
st.header("👤 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name")
    age = st.number_input("Age", min_value=15, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=230.0, value=175.0)

with col2:
    weight = st.number_input("Weight (kg)", min_value=25.0, max_value=250.0, value=65.0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    activity = st.selectbox(
        "Activity Level",
        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
    )

goal = st.selectbox(
    "Your Fitness Goal",
    ["Muscle Gain", "Weight Loss", "Maintain Weight", "General Fitness"]
)

diet_type = st.selectbox(
    "Diet Preference",
    ["Vegetarian", "Vegetarian + Eggs", "Non-Vegetarian"]
)

if st.button("Generate My Fitness Plan", type="primary"):

    if not name.strip():
        st.error("Please enter your name.")
    else:

        # BMI CALCULATION
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.divider()
        st.header(f"Hello {name}! Your Fitness Report 🎯")

        c1, c2, c3 = st.columns(3)

        c1.metric("Your BMI", round(bmi, 2))
        c2.metric("Weight", f"{weight} kg")
        c3.metric("BMI Category", category)

        st.info(
            "BMI is a screening measure, not a complete assessment "
            "of body composition or health."
        )

        # CALORIE ESTIMATION
        activity_factor = {
            "Sedentary": 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725
        }

        if gender == "Male":
            bmr = 10*weight + 6.25*height - 5*age + 5
        elif gender == "Female":
            bmr = 10*weight + 6.25*height - 5*age - 161
        else:
            bmr = 10*weight + 6.25*height - 5*age - 78

        maintenance = bmr * activity_factor[activity]

        if goal == "Muscle Gain":
            calories = maintenance + 250
            protein = weight * 1.6
        elif goal == "Weight Loss":
            calories = maintenance - 300
            protein = weight * 1.6
        elif goal == "Maintain Weight":
            calories = maintenance
            protein = weight * 1.4
        else:
            calories = maintenance
            protein = weight * 1.2

        st.subheader("🔥 Daily Nutrition Targets")

        c1, c2 = st.columns(2)
        c1.metric("Estimated Calories", f"{calories:.0f} kcal")
        c2.metric("Protein Target", f"{protein:.0f} g")

        # EXERCISE PLAN
        st.divider()
        st.header("🏋️ Your Weekly Exercise Plan")

        exercises = {
            "Monday": "Chest + Triceps",
            "Tuesday": "Back + Biceps",
            "Wednesday": "Legs + Abs",
            "Thursday": "Shoulders + Cardio",
            "Friday": "Chest + Back",
            "Saturday": "Legs + Abs",
            "Sunday": "Rest / Active Recovery"
        }

        for day, workout in exercises.items():
            st.write(f"**{day}:** {workout}")

        # DIET PLAN
        st.divider()
        st.header("🥗 Your Indian Diet Plan")

        if diet_type == "Vegetarian":
            breakfast = "Oats with milk, banana and almonds"
            lunch = "4 Roti, Dal, Paneer and vegetables"
            snack = "Roasted chana and seasonal fruits"
            dinner = "Rice, Dal, Soy chunks and vegetables"

        elif diet_type == "Vegetarian + Eggs":
            breakfast = "4 Egg omelette, whole wheat bread and milk"
            lunch = "Roti, Dal, Paneer and vegetables"
            snack = "Banana, peanut butter and curd"
            dinner = "Rice, Dal, 2 boiled eggs and vegetables"

        else:
            breakfast = "3 Egg omelette, whole wheat bread and milk"
            lunch = "Roti, Chicken, Dal and vegetables"
            snack = "Greek yogurt, banana and almonds"
            dinner = "Rice, Chicken and vegetables"

        diet = {
            "Breakfast": breakfast,
            "Mid Morning": "Seasonal fruits and nuts",
            "Lunch": lunch,
            "Evening Snack": snack,
            "Dinner": dinner
        }

        for meal, food in diet.items():
            st.markdown(f"**{meal}**")
            st.write(food)

        st.divider()

        st.success("Your fitness plan has been generated!")

        st.caption(
            "Recommendations are general estimates. Adjust portions "
            "to your needs and consult a qualified dietitian or trainer "
            "for individualized advice."
        )
