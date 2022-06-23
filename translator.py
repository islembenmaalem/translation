from googletrans import Translator
import gradio as gr
#from playsound import playsound
#import pyttsx3
translator= Translator()
#engine = pyttsx3.init()

def greet(text_to_translate,lang):
    if lang=="English":
        s=translator.translate(text_to_translate, dest="en").text
    if lang=="French":
        s=translator.translate(text_to_translate, dest="fr").text
    if lang=="Arabic":
        s=translator.translate(text_to_translate, dest="ar").text
    if lang=="German":
        s=translator.translate(text_to_translate, dest="DE").text
   # engine.say(s)
   # a=engine.runAndWait()
    return s #,gr.Audio(s)

demo = gr.Interface(fn=greet,inputs=[gr.Textbox(lines=4, placeholder="Text Here..."),
                    gr.Radio(["English", "French", "Arabic", "German"])],
                    outputs=[gr.Textbox(lines=4)])

demo.launch()



