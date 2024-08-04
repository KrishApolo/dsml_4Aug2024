import pickle
import streamlit as st

Diabetes = st.selectbox(" Are you having Diabetes ",
['Yes','No',])
BPProblems = st.selectbox(" Are you having BP ",
['Yes','No',])
AnyTransplants = st.selectbox(" Did you have any Transplants ",
['Yes','No',])
AnyChronicDiseases = st.selectbox(" Are you having AnyChronic Diseases ",
['Yes','No',])
KnownAllergies = st.selectbox(" Are you having Any Known Allergies ",
['Yes','No',])
HistoryOfCancer = st.selectbox(" Are you having Any History of Cancer in your Family ",
['Yes','No',])
Age = st.number_input('Age', 18, 100)
Height = st.number_input('Height', 130, 200)
Weight = st.number_input('Weight', 50, 300)
NumberofMajorSurgeries = st.slider('no of major surgeries', 0, 3)

encode_values = {
"Diabetes": {"Yes":1,"No":0},
"BPProblems": {"Yes":1,"No":0},
"AnyTransplants": {"Yes":1,"No":0},
"AnyChronicDiseases": {"Yes":1,"No":0},
"KnownAllergies": {"Yes":1,"No":0},
"HistoryOfCancer": {"Yes":1,"No":0}
}

def model_pred(Diabetes_e, BPProblems_e, AnyTransplants_e, AnyChronicDiseases_e,
                    KnownAllergies_e, HistoryOfCancer_e, Age, Height, Weight, NumberofMajorSurgeries):
 with open('IA.pkl','rb') as file:
  model = pickle.load(file)
  new_X = [[Age,Diabetes_e,BPProblems_e,AnyTransplants_e,AnyChronicDiseases_e,Height,
            Weight,KnownAllergies_e,HistoryOfCancer_e,NumberofMajorSurgeries]]
  return model.predict(new_X)


if(st.button("Predict Premium Price")):
 Diabetes_e=encode_values["Diabetes"][Diabetes]
 BPProblems_e = encode_values["BPProblems"][BPProblems]
 AnyTransplants_e = encode_values["AnyTransplants"][AnyTransplants]
 AnyChronicDiseases_e = encode_values["AnyChronicDiseases"][AnyChronicDiseases]
 KnownAllergies_e = encode_values["KnownAllergies"][KnownAllergies]
 HistoryOfCancer_e = encode_values["HistoryOfCancer"][HistoryOfCancer]

 price = model_pred(Diabetes_e, BPProblems_e, AnyTransplants_e, AnyChronicDiseases_e,
                    KnownAllergies_e, HistoryOfCancer_e, Age, Height, Weight, NumberofMajorSurgeries)
 st.text("Precited Premium Price is: "+str(price))







