%%writefile app.py
import streamlit as st
st.write('Group 1 Project')
st.header("Investment Risk Tolerance Quiz")
# Quiz questions, options, and scores
questions = {
    "1. In general, how would your best friend describe you as a risk taker?": {
        "options": ["A real gambler", "Willing to take risks after completing adequate research", "Cautious", "A real risk avoider"],
        "scores": [4, 3, 2, 1]  # Score for each option
    },
    "2. You are on a TV game show and can choose one of the following.  Which would you take?": {
        "options": ["$1,000 in cash", "A 50% chance at winning $5,000", "A 25% chance at winning $10,000", "A 5% chance at winning $100,000"],
        "scores": [1, 2, 3, 4]  # Score for each option
    },
    "3. You have just finished saving for a “once-in-a-lifetime” vacation.  Three weeks before you plan to leave, you lose your job.  You would:": {
        "options": ["Cancel the vacation", "Take a much more modest vacation", "Go as scheduled, reasoning that you need the time to prepare for a job search", "Extend your vacation, because this might be your last chance to go first-class"],
        "scores": [1, 2, 3, 4]  # Score for each option
    },
    "4. If you unexpectedly received $20,000 to invest, what would you do?": {
        "options": ["Deposit it in a bank account, money market account, or an insured CD", "Invest it in safe high quality bonds or bond mutual funds", "Invest it in stocks or stock mutual funds"],
        "scores": [1, 2, 3]  # Score for each option
    },
    "5. In terms of experience, how comfortable are you investing in stocks or stock mutual funds?": {
        "options": ["Not at all comfortable", "Somewhat comfortable", "Very comfortable"],
        "scores": [1, 2, 3]  # Score for each option
    },
    "6. When you think of the word “risk” which of the following words comes to mind first? ": {
        "options": ["Loss", "Uncertainty", "Opportunity", "Thrill"],
        "scores": [1, 2, 3,4]  # Score for each option
    },
    "7. Some experts are predicting prices of assets such as gold, jewels, collectibles, and real estate (hard assets) to increase in value; bond prices may fall, however, experts tend to agree that government bonds are relatively safe. Most of your investment assets are now in high interest government bonds. What would you do?": {
        "options": ["Hold the bonds", "Sell the bonds, put half the proceeds into money market accounts, and the other half into hard assets", "Sell the bonds and put the total proceeds into hard assets", "Sell the bonds, put all the money into hard assets, and borrow additional money to buy more"],
        "scores": [1, 2, 3,4]  # Score for each option
    },
    "8. Given the best and worst case returns of the four investment choices below, which would you prefer?": {
        "options": ["$200 gain best case; $0 gain/loss worst case", "$800 gain best case; $200 loss worst case", "$2,600 gain best case; $800 loss worst case", "$4,800 gain best case; $2,400 loss worst case"],
        "scores": [1, 2, 3,4]  # Score for each option
    },
    "9. In addition to whatever you own, you have been given $1,000.  You are now asked to choose between:": {
        "options": ["A sure gain of $500", "A 50% chance to gain $1,000 and a 50% chance to gain nothing"],
        "scores": [1, 3]  # Score for each option
    },
    "10. In addition to whatever you own, you have been given $2,000.  You are now asked to choose between:": {
        "options": ["A sure loss of $500", "A 50% chance to lose $1,000 and a 50% chance to lose nothing"],
        "scores": [1, 3]  # Score for each option
    },
    "11. Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL the money in ONE of the following choices.  Which one would you select?": {
        "options": ["A savings account or money market mutual fund", "A mutual fund that owns stocks and bonds", "A portfolio of 15 common stocks", "Commodities like gold, silver, and oil"],
        "scores": [1, 2, 3, 4]  # Score for each option
    },
    "12. If you had to invest $20,000, which of the following investment choices would you find most appealing?": {
        "options": ["60% in low-risk investments 30% in medium-risk investments 10% in high-risk investments", "30% in low-risk investments 40% in medium-risk investments 30% in high-risk investments", "10% in low-risk investments 40% in medium-risk investments 50% in high-risk investments"],
        "scores": [1, 2, 3]  # Score for each option
    },
    "13. Your trusted friend and neighbor, an experienced geologist, is putting together a group of investors to fund an exploratory gold mining venture. The venture could pay back 50 to 100 times the investment if successful.  If the mine is a bust, the entire investment is worthless.  Your friend estimates the chance of success is only 20%.  If you had the money, how much would you invest? ": {
        "options": ["Nothing", "One month’s salary", "Three month’s salary", "Six month’s salary"],
        "scores": [1, 2, 3,4]  # Score for each option
    }
}

# Store user's responses
user_answers = {}

# Display questions and get user input
for question, data in questions.items():
    st.subheader(question)
    user_answers[question] = st.radio("Select your answer:", data["options"])

# Check answers and display score
if st.button("Submit"):
    score = 0
    for question, data in questions.items():
        selected_answer = user_answers[question]
        selected_index = data["options"].index(selected_answer)
        score += data["scores"][selected_index]
    st.write("Thank you for taking the quiz!")
    st.write(f"Your score: {score}")

    # Define risk tolerance categories
    risk_tolerance_categories = {
        (0, 18): "Low risk tolerance (i.e., conservative investor)",
        (19, 22): "Below-average risk tolerance",
        (23, 28): "Average/moderate risk tolerance",
        (29, 32): "Above-average risk tolerance",
        (33, float('inf')): "High risk tolerance (i.e., aggressive investor)"
    }

    # Determine risk tolerance level
    for score_range, risk_tolerance in risk_tolerance_categories.items():
        if score_range[0] <= score <= score_range[1]:
            st.write(f"Your risk tolerance level: {risk_tolerance}")
            break