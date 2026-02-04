# astrology/utils.py


# ----------------------------------
# ZODIAC SIGN CALCULATION
# ----------------------------------
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"


# ----------------------------------
# BIRTH TIME CATEGORY
# ----------------------------------
def time_category(birth_time):
    hour = int(birth_time.split(":")[0])

    if 4 <= hour < 6:
        return "Brahma Muhurat Born (Highly intuitive and calm)"
    elif 6 <= hour < 12:
        return "Morning Born (Active and positive mindset)"
    elif 12 <= hour < 16:
        return "Afternoon Born (Practical and hardworking)"
    elif 16 <= hour < 20:
        return "Evening Born (Creative and social)"
    else:
        return "Night Born (Deep thinker and emotional)"


# ----------------------------------
# PERSONAL PREDICTION (RESULT PAGE)
# ----------------------------------
def get_prediction(zodiac):
    predictions = {
        "Aries": (
            "You are bold, energetic, and full of confidence. "
            "Today is a good day to take leadership roles and start new tasks. "
            "Avoid acting in haste and think before making important decisions."
        ),
        "Taurus": (
            "You are calm, patient, and practical by nature. "
            "This is a favorable time to focus on financial stability and long-term planning. "
            "Avoid unnecessary arguments and stay grounded."
        ),
        "Gemini": (
            "You are communicative, curious, and adaptable. "
            "Your ideas and communication skills will help you succeed today. "
            "Try to stay focused and avoid distractions."
        ),
        "Cancer": (
            "You are emotional, caring, and intuitive. "
            "Family and personal relationships play an important role today. "
            "Trust your instincts but do not let emotions overpower logic."
        ),
        "Leo": (
            "You are confident, creative, and enthusiastic. "
            "This is a good day to express your talents and take center stage. "
            "Be mindful of ego and listen to others as well."
        ),
        "Virgo": (
            "You are analytical, organized, and detail-oriented. "
            "Planning and discipline will bring positive results today. "
            "Avoid overthinking and give yourself time to relax."
        ),
        "Libra": (
            "You value balance, harmony, and fairness. "
            "Relationships and partnerships improve with honest communication. "
            "Try not to delay decisions for too long."
        ),
        "Scorpio": (
            "You are intense, focused, and determined. "
            "This is a good time to work on goals that require deep concentration. "
            "Avoid conflicts and channel your energy positively."
        ),
        "Sagittarius": (
            "You are optimistic, adventurous, and open-minded. "
            "Learning something new or exploring fresh ideas will benefit you today. "
            "Stay realistic while making future plans."
        ),
        "Capricorn": (
            "You are disciplined, responsible, and hardworking. "
            "Your efforts will slowly bring success and recognition. "
            "Do not ignore your health while focusing on work."
        ),
        "Aquarius": (
            "You are innovative, independent, and forward-thinking. "
            "Creative ideas and unique approaches will help you stand out. "
            "Stay connected with people who support your vision."
        ),
        "Pisces": (
            "You are imaginative, sensitive, and intuitive. "
            "Creative activities and emotional connections bring peace today. "
            "Avoid over-trusting others and stay practical when needed."
        ),
    }

    return predictions.get(zodiac, "Have a calm and positive day.")
