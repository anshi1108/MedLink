import pyttsx3
import datetime

def chat_about_disease(query):
    # Add your logic to handle different types of diseases and their information
    # For simplicity, categorize based on common disease types
    if 'flu' in query:
        return "The flu, or influenza, is a contagious respiratory illness caused by influenza viruses. Symptoms include fever, cough, sore throat, body aches, and fatigue."

    elif 'diabetes' in query:
        return "Diabetes is a chronic condition that affects how your body turns food into energy. There are different types of diabetes, including type 1 and type 2. Management involves medication, diet, and lifestyle changes."

    elif 'hypertension' in query or 'high blood pressure' in query:
        return "Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is consistently too high. It can lead to serious health issues, so it's important to manage it through lifestyle changes and medication."

    elif 'asthma' in query:
        return "Asthma is a chronic respiratory condition that causes difficulty in breathing. It is often triggered by factors like allergies or environmental factors. Treatment involves medications and lifestyle management."

    elif 'arthritis' in query:
        return "Arthritis is a condition that causes inflammation in the joints, leading to pain and stiffness. There are different types of arthritis, and treatment options include medications, physical therapy, and lifestyle changes."

    elif 'migraine' in query:
        return "A migraine is a type of headache characterized by severe pain, nausea, and sensitivity to light and sound. Migraines can be triggered by various factors, and treatment may include medications and lifestyle adjustments."

    elif 'osteoporosis' in query:
        return "Osteoporosis is a condition characterized by weakened bones, making them more prone to fractures. It is more common in older adults, especially women. Treatment involves medications, a healthy diet, and weight-bearing exercises."

    elif 'pneumonia' in query:
        return "Pneumonia is an infection that inflames the air sacs in one or both lungs. Symptoms include cough, fever, and difficulty breathing. Treatment typically involves antibiotics and supportive care."

    elif 'anemia' in query:
        return "Anemia is a condition where there is a deficiency of red blood cells or hemoglobin in the blood, leading to fatigue and weakness. Treatment depends on the underlying cause and may include iron supplements or other medications."

    elif 'cancer' in query:
        return "Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. Treatment options vary depending on the type and stage of cancer and may include surgery, chemotherapy, and radiation therapy."

    elif 'alzheimer' in query or 'dementia' in query:
        return "Alzheimer's disease is a progressive neurodegenerative disorder that affects memory and cognitive function. There is no cure, but treatment may involve medications and supportive care."

    elif 'heart disease' in query:
        return "Heart disease refers to a variety of conditions that affect the heart, including coronary artery disease and heart failure. Management involves lifestyle changes, medications, and, in some cases, surgery."

    elif 'stroke' in query:
        return "A stroke occurs when there is a disruption of blood flow to the brain, leading to damage. Symptoms include sudden numbness, confusion, and difficulty speaking. Treatment depends on the type of stroke but may involve medication or surgery."

    elif 'chronic kidney disease' in query:
        return "Chronic kidney disease is a condition where the kidneys gradually lose their function over time. Treatment involves managing underlying conditions, medications, and sometimes dialysis or kidney transplant."

    elif 'liver cirrhosis' in query:
        return "Liver cirrhosis is a late stage of scarring of the liver caused by many forms of liver diseases and conditions. It can lead to liver failure. Management includes lifestyle changes and treatment of underlying causes."

    elif 'parkinson' in query:
        return "Parkinson's disease is a progressive nervous system disorder that affects movement. Symptoms include tremors, stiffness, and difficulty with balance. Treatment involves medications and, in some cases, surgery."

    elif 'thyroid' in query:
        return "Thyroid disorders, such as hypothyroidism or hyperthyroidism, affect the thyroid gland's function. Treatment may involve medication to regulate thyroid hormones."

    elif 'ulcerative colitis' in query:
        return "Ulcerative colitis is a chronic inflammatory bowel disease that causes inflammation and ulcers in the colon. Treatment involves medications and, in severe cases, surgery."

    elif 'osteoarthritis' in query:
        return "Osteoarthritis is a degenerative joint disease that occurs when the protective cartilage that cushions the ends of bones wears down over time. Treatment includes pain management and lifestyle modifications."

    elif 'fibromyalgia' in query:
        return "Fibromyalgia is a disorder characterized by widespread musculoskeletal pain, fatigue, and sleep disturbances. Treatment involves pain management, exercise, and stress reduction."

    else:
        return "I'm sorry, I don't have information on that specific disease. It's recommended to consult with a healthcare professional for accurate advice."

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    say("I am JARVIS, your Virtual Artificial Intelligence")
    say("JARVIS at your service, please tell me how can I help you?")

    while True:
        query = input("User: ").lower()

        if 'offline' in query or 'bye' in query:
            say("Thank you! Goodbye")
            break
        else:
            print("Chatting....")
            response = chat_about_disease(query)
            print(response)
            say(response)
