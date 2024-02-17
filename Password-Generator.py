import random 
import streamlit as st
import string
import tempfile



def landingpage():
    st.header("Password Generator (Very Secure!)")
    st.image("images/hackerman.jpg")
    st.write("------")
    st.subheader("Please select the below parameters for your password and press the submit button below to generate your password!")
    numofpasswords = st.number_input("How many unique passwords would you like?",0,10000) #NEW
    passwordlength = st.number_input("How long do you want your password to be?",8,40)
    caps = st.checkbox("Do you want your password to contain capital letters?",False)
    nums = st.checkbox("Do you want your password to contain numbers?",False)
    specialchars = st.checkbox("Do you want special characters in your password?",False) #NEW
    listofspecialcars = False
    allspecialchars = False
    if specialchars:
        listofspecialcars = st.text_input("Which special characters do you want in your textbox? Eg.!@#$%^&*()-=+_") #NEW
        allspecialchars = st.checkbox("Or alternatively, do you want to use all special characters?",False)
    generatorbutton = st.button("(Re)generate Passwords")
    st.write("------")
    if generatorbutton:
        pwfile = tempfile.TemporaryFile("wb+")
        st.header("Generated Passwords:")
        passwordstr = getpassstr(caps,nums,specialchars,listofspecialcars,allspecialchars)
        for password in range(numofpasswords):
            currentpw = passwordgenerator(passwordlength,passwordstr)
            if password <=5:
                st.markdown("```  "+currentpw+"  ```")
            pwfile.write(bytes(currentpw + "\n\n", "utf-8"))
        st.write("All passwords have been generated! Up to the first 5 are displayed above, if you would like the rest click the download button!")
        pwfile.seek(0)
        st.download_button(
                label="Download Password File",data=pwfile.read(),key='temp_file_download',file_name='SUPER_DUPER_SECURE_PASSWORDS.txt',mime='text/plain')
        st.write("-----")
        st.image("images/finished.jpg",caption="Thank you for using our service! :D")

def getpassstr(caps,nums,specialchars,listofspecialchars,allspecialchars):
    chararray = string.ascii_lowercase
    if caps:
        chararray += string.ascii_uppercase
    if nums:
        chararray += "0123456789"
    if specialchars:
        if allspecialchars:
            chararray += string.punctuation.replace(" ","")
        else:
            chararray+=listofspecialchars
    return chararray
def passwordgenerator(passwordlen,passwordstr):
    password = ""
    while len(password) < passwordlen:
        password += random.choice(passwordstr)
    return password

landingpage()