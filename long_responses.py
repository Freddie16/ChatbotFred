import random

R_EATING = "I dont like eating anything because I am a bot!"

def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response