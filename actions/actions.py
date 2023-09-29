# Après chaque message de l'utilisateur, le modèle prévoira une action que l'assistant devrait effectuer ensuite. Ici, nous définissons ces actions.




from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import testdb


import os
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = 'your Api key'
llm = OpenAI(temperature=0.7) 


def req2llm(llm, prompt):
    response = llm(prompt)
    return response


class ActionMed(Action):
    def name(self):
        return 'action_Med'

    def run(self, dispatcher, tracker, domain):
        n = tracker.get_slot('nom')

        med, time = testdb.medication(n)
        prompt =  f'Generate a question for a person asking him if he have taken the medecine {med} at the time {time}, in a casual way, in french.'
        response = req2llm(llm, prompt)
        dispatcher.utter_message(text=response)
        return []
    
class ActionRDV(Action):
    def name(self):
        return 'action_RDV'

    def run(self, dispatcher, tracker, domain):
        n = tracker.get_slot('nom')
        data = testdb.get_apppointment(n)
        date = data[0][1]
        time = data[0][2]
        reason = data[0][0]
        location = data[0][-1]
        prompt = f"""You are a nurse in a retirement house,
        generate a phrase to inform an aged patient in front of you about his upcoming appointment.
        appointment details:
        date: {date}
        time: {time}
        reason: {reason}
        location: {location}
        in french
        your unswer should not start with greeting
        """
        response = req2llm(llm, prompt)
        dispatcher.utter_message(text=response)
        return []
    

class ActionACT(Action):
    def name(self):
        return 'action_ACT'

    def run(self, dispatcher, tracker, domain):
        n = tracker.get_slot('nom')
        data = testdb.get_activity(n)
        activity = data[0][0]
        location = data[0][3]
        prompt = f""" In french language with an excitment tone of voice tell a resident of an retirement house that we have an activity with this details: activity: {activity} 
        location: {location} 
        make sure to not to use greeting words.
        in a casual way 
        """
        response = req2llm(llm, prompt)
        dispatcher.utter_message(text=response)
        return []
    


class ActionMeal(Action):
    def name(self):
        return 'action_meal'

    def run(self, dispatcher, tracker, domain):
        n = tracker.get_slot('nom')
        data = testdb.get_meal(n)
        prompt = f'act like a nurse and inform a patient about the meal that he will have with this details in french: meal: {data[0]}, time: {data[1]}'
        # response = f'Il y a  le repas du  "{data[0]}" a {data[1]}'
        response = req2llm(llm, prompt)
        dispatcher.utter_message(text=response)
        return []



class ActionMal(Action):
    def name(self):
        return 'action_call'

    def run(self, dispatcher, tracker, domain):
        n = tracker.get_slot('nom')
        last_msg = tracker.latest_message['text']
        prompt = f"""inform the nurse that a patient is sick and give her details from what the patient says folowing this template in french in a casual way:
        'message a l'infirmière: le patient {n} est malade, il a dit qu'il a du ...'
        patient says :{last_msg}
        """
        response = req2llm(llm, prompt)

        dispatcher.utter_message(text=response)
        return []
    

class ActionFallback(Action):
    def name(self):
        return 'action_fallback'

    def run(self, dispatcher, tracker, domain):

        last_msg = tracker.latest_message['text']
        prompt =  f'''### Context ###
                      You are a nurse in a french retirement house. An elderly patient randomly asked you.
                      If the patient asks something emotional act like a therapist and try to conduct a coversation with him
                      Your unswer should be one sentence
                      elder patient said {last_msg}
                      answer with one phrase
                '''
        response = req2llm(llm, last_msg)
        dispatcher.utter_message(text=response)
        return []