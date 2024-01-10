#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Harsh Verma
#
# Created:     10-01-2024
# Copyright:   (c) Harsh Verma 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
def reocord_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)

                audio2=r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText
        except sr.RequestError as e:
            print("could not request as result{0}".format(e))

        except sr.unknownValueError:
            print("unkonwn error occured")


    return


def output_text(text):
    f = open("output.Txt","a")
    f.write(text)
    f.write("\n")
    f.close()

    return

while(1):
    text=record_text()
    output_text(text)


    print("wrote text")