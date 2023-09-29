from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import testdb
from . import openai_test 

import os
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = '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'
llm = OpenAI(temperature=0.9) 


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
        # response = openai_test.med_req(med, time)
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
        prompt = f""" In french language tell a resident of an retirement house that we have an activity with this details: activity: {activity} 
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
        response = f'Il y a  le repas du  "{data[0]}" a {data[1]}'
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