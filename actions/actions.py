# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
import re


# class ActionIntroductionForm(FormAction):
#     def name(self) -> Text:
#         return "action_introduction_form"
    
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["name", "money_spent", "reasons_for_change", "length_of_addiction"]
#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {
#             "name": self.from_text(),
#             "money_spent": self.from_text(),
#             "reasons_for_change": self.from_text(),
#             "length_of_addiction": self.from_text(),
#         }
    
    # def submit(self, slot_value: Any,
    #                          dispatcher: CollectingDispatcher,
    #                          tracker: Tracker,
    #                          domain: DomainDict,) -> List[Dict]:
    #     name = tracker.get_slot("name")
    #     dispatcher.utter_message(text=f"Thank you {name}! It's great to meet you. As said earlier, my name is paul and just like you struggled with smoking for a long time.")
    #     return []

# class ActionSessionStart(Action):
#     def name(self) -> str:
#         return "action_session_start"
    
#     async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, any]) -> List[EventType]:
#         events = [SessionStarted(), ActionExecuted("action_listen")]
#         commitment = tracker.get_slot("commitment")
#         if commitment:
#             dispatcher.utter_message(text="Welcome back! You remember your promise to yourself?")
#             dispatcher.utter_message(commitment)
#             return events

class ValidateIntroductionForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_introduction_form"
    
    def validate_name(self, slot_value: Any,
                             dispatcher: CollectingDispatcher,
                             tracker: Tracker,
                             domain: DomainDict, ) -> Dict[Text, Any]:
       if slot_value.isalpha():
           return {"name": slot_value}
       else:
           dispatcher.utter_message(text="Please enter a valid name")
           return {"name": None} 
    
    def validate_money_spent(self, slot_value: Any,
                             dispatcher: CollectingDispatcher,
                             tracker: Tracker,
                             domain: DomainDict, ) -> Dict[Text, Any]:
       amount = float(slot_value)
       if amount >= 0:
           return {"money_spent": amount}
       else:
           dispatcher.utter_message(text="Please enter a valid number. Ignore currency signs (e.g £, $, etc.)")
           return {"money_spent": None}
    
    def validate_length_of_addiction(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict,) -> Dict[Text, Any]:
        length_of_time = {
            "days": r"\b\d\s*day(s?)\b",
            "weeks": r"\b\d\s*week(s?)\b",
            "months": r"\b\d\s*month(s?)\b",
            "years": r"\b\d\s*years(s?)\b"
        }
        length = str(slot_value).lower()
        match_found =None

        for unit, pattern in length_of_time.items():
            if re.search(pattern, length):

                match = re.search(r"(\d+)\s*({})".format(unit[:-1]), length)
                if match:
                    clean_value = f"{match.group(1)} {unit}"
                    return {"length_of_addiction": clean_value}
                
                if not match_found:
                    dispatcher.utter_message(text="Please specify duration with a number and time unit. e.g. '3 months'")
                    return {"length_of_addiction": None}
                
                return {"length_of_addiction": slot_value}




class ActionSaveCommitment(Action):
    def name(self) -> str:
        return "action_save_commitment"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, any]) -> List[Dict[str, Any]]:
        commitment = tracker.latest_message.get('text')
        dispatcher.utter_message(text = "Awesome commitment! You can write it down, but I'll be sure to remind you.")
        return [SlotSet("set_commitment", commitment)]

class ActionShowCommitment(Action):
    def name(self):
        return "action_show_commitment"
    
    def run(self, dispatcher, tracker, domain):
        commitment = tracker.get_slot("set_commitment")
        if commitment:
            dispatcher.utter_message(text=f"Your current commitment is: {commitment}")
        else:
            dispatcher.utter_message(text="You haven't set a commitment yet.")
        return []

class ActionHandleMeditationtypesNoAudio(Action):
    def name(self):
        return "action_handle_meditation_type_no_audio"
    
    def run(self, dispatcher, tracker, domain):
        meditation_type = tracker.get_slot("meditation_type")
        if meditation_type == "focused meditation":
            dispatcher.utter_message(text="Let's begin focused meditation.")
            dispatcher.utter_message(text="Choose a focal point, such as your breath, a candle flame, or a sound.")
            dispatcher.utter_message(text="Bring your attention to the focal point, noticing its sensations.")
            dispatcher.utter_message(text="When your mind wanders, gently bring it back to the focal point.")
            dispatcher.utter_message(text="Continue for a few minutes, maintaining your focus.")
        elif meditation_type == "progressive relaxation":
            dispatcher.utter_message(text="Let's begin progressive relaxation.")
            dispatcher.utter_message(text="Find a comfortable position.")
            dispatcher.utter_message(text="Start by tensing the muscles in your toes for 5 seconds, then release them.")
            dispatcher.utter_message(text="Move up your body, tensing and releasing each muscle group: feet, calves, thighs, buttocks, abdomen, chest, hands, arms, shoulders, neck, and face.")
            dispatcher.utter_message(text="Focus on the feeling of relaxation as you release each muscle group.")
            dispatcher.utter_message(text="Continue for a few minutes, allowing your body to fully relax.")
        elif meditation_type == "mindfulness meditation":
            dispatcher.utter_message(text="Let's begin mindfulness meditation.")
            dispatcher.utter_message(text="Find a comfortable position, either sitting or lying down.")
            dispatcher.utter_message(text="Close your eyes or keep them softly focused on a point in front of you.")
            dispatcher.utter_message(text="Bring your attention to your breath, noticing the sensation of each inhale and exhale.")
            dispatcher.utter_message(text="When your mind wanders, gently bring it back to your breath.")
            dispatcher.utter_message(text="Continue for a few minutes, allowing yourself to simply observe your thoughts and feelings without judgment.")
            dispatcher.utter_message(text="When you're ready, slowly open your eyes.")
        else: dispatcher.utter_message(text="Sorry we haven't got that available.")

        return []
    
class ActionHandleBreathworktypesNoAudio(Action):
    def name(self):
        return 'action_handle_breathwork_types_no_audio'
    
    def run(self, dispatcher, domain, tracker):
        breathwork_type = Tracker.get_slot("breathwork_type")
        if breathwork_type == "box breathing":
            dispatcher.utter_message(text="Let's try box breathing, also known as square breathing.")
            dispatcher.utter_message(text="Exhale completely, pushing all the air out of your lungs.")
            dispatcher.utter_message(text="Inhale slowly and deeply through your nose to a count of four.")
            dispatcher.utter_message(text="Hold your breath for a count of four.")
            dispatcher.utter_message(text="Exhale slowly through your mouth to a count of four.")
            dispatcher.utter_message(text="Hold your breath again for a count of four.")
            dispatcher.utter_message(text="Repeat this cycle for a few minutes.")
            dispatcher.utter_message(text="Take a moment to observe how you feel.")
        elif breathwork_type == "4-7-8 breathing":
            dispatcher.utter_message(text="Let's try the 4-7-8 breathing technique.")
            dispatcher.utter_message(text="First, exhale completely through your mouth, making a whooshing sound.")
            dispatcher.utter_message(text="Close your mouth and inhale quietly through your nose to a count of four.")
            dispatcher.utter_message(text="Hold your breath for a count of seven.")
            dispatcher.utter_message(text="Exhale completely through your mouth, making a whooshing sound to a count of eight.")
            dispatcher.utter_message(text="This is one breath. Now repeat the cycle three more times for a total of four breaths.")
            dispatcher.utter_message(text="Notice any changes in how you feel.")
        elif breathwork_type == "abdominal breathing":
            dispatcher.utter_message(text="Let's try abdominal breathing. Place one hand on your chest and the other on your belly.")
            dispatcher.utter_message(text="Inhale slowly and deeply through your nose, feeling your belly rise more than your chest.")
            dispatcher.utter_message(text="Exhale slowly through your mouth, feeling your belly fall.")
            dispatcher.utter_message(text="Continue this for a few minutes, focusing on your breath.")
            dispatcher.utter_message(text="How do you feel now?")
        else:
            dispatcher.utter_message(text="Sorry we haven't got that available.")
        return []
    

class ActionHandleMeditationType(Action):
    def name(self):
        return 'action_handle_meditation_type'
    
    def run(self, dispatcher: CollectingDispatcher, domain, tracker: Tracker):
        meditation_type = tracker.get_slot("meditation_type")
        if meditation_type == "focused meditation":
            dispatcher.utter_message("Now Playing... (audio: box_breathing)")
        elif meditation_type == "progressive relaxation":
            dispatcher.utter_message("Now playing... (audio: progressive_relaxation)")
        elif meditation_type == "mindfulness meditation":
            dispatcher.utter_message("Now playing... (audio: mindfulness_meditation)")

        else:
            dispatcher.utter_message(text="Sorry, don't have audio for that.")
        return []


class ActionHandleBreathworkTypesAudio(Action):
    def name(Self):
        return 'action_handle_breathwork_type_audio'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        breathwork_type = tracker.get_slot("breathwork_type")





