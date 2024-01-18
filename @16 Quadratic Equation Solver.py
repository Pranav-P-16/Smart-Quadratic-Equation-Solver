# IMPORTING MODULES

import PySimpleGUI as sg
import random

# SETTING EXCEPTION HANDLING DIALOGUES

typeerr=["For Solving Numbers,not alphabets","Seriously ?","Learn basic maths first",
         "You are kidding me","Nah Bro","Oh... Not Again","Trying experiments, huh ?",
         "Kindly Consult nearest hospital","My Algorithm broke :(","I'm even Smarter :]",
         "All you want to do was to learn basic Maths","I'm 100% Bugless ;)","Challenging Mathematics, huh ?",
         "Don't mess with me !","#StudyBasicMaths"]
zrdvserr=["How can I divide by Zero, tell me Bro","You Mathematics Genius !","Division by Zero Can't be done",
          "How about inventing a new way of division ?","You broke my algorithm :(","I'm even smarter than you ;)",
          "#StudyBasicMaths","'a' shouldn't be zero !"]
err=["An Error had Occured !","Oops, I broke :(","Unfortunately, Execution has been terminated",
     "ERROR 404 : Brain Missing","ERROR 404 : Error handler Missing","404 Not Again","ERROR 404 : I'm a machine too :(",
     "Why do you insist on me ?","#WhyShouldHumanshaveallthefun","Tea Break,Come again later",
     "Sleeping Beauty","Don't Disturb Me","Why always Me :?","Am I a maths genius to you  ?"]

# FUNCTION FOR DISPLAYING SOLUTION + FINAL TOUCHUP OF SOLUTION

def solution(s1,s2):
    try:
        s1=round(s1,3)
    except:
        s1=round(s1.real, 2) + round(s1.imag, 2) * 1j
    try:
        s2=round(s2,3)
    except:
        s2=round(s2.real, 3) + round(s2.imag, 3) * 1j
    sg.theme("black")
    layout2=[[sg.Text("\n")],[sg.Text("\tThe Solutions are ")]+[sg.Text(str(s1),text_color="green2",font=("Helvetica",15))]+[sg.Text(" and ")]+[sg.Text(str(s2),text_color="green2",font=("Helvetica",15))]+[sg.Text("\t")],[sg.Text("\n")],
             [sg.Button("OK",size=(10,1))]]
    window2=sg.Window("Solution",layout2,element_justification="c")
    event,values=window2.read()
    window2.close()

# FUNCTION FOR DISPLAYING ERROR MESSAGES

def fail(text):
    sg.theme("black")
    layout2=[[sg.Text("\n")],[sg.Text("\t"+text)]+[sg.Text("\t")],[sg.Text("\n")],
             [sg.Button("OK",size=(10,1))]]
    window2=sg.Window("Not Again",layout2,element_justification="c")
    event,values=window2.read()
    window2.close()


# MAIN PROGRAM LAYOUT AND AI DATA INTERPRETOR

sg.theme("black")
layout=[[sg.Text("@16 Quadratic Equation Solver",font=("Pricedown",25))],
        [sg.Text("a ",font=("Pricedown",25))]+[sg.Input(key="-a-",size=(10,1))]+[sg.Text("",key="cb1")],
        [sg.Text("b ",font=("Pricedown",25))]+[sg.Input(key="-b-",size=(10,1))]+[sg.Text("",key="cb2")],
        [sg.Text("c ",font=("Pricedown",25))]+[sg.Input(key="-c-",size=(10,1))]+[sg.Text("",key="cb3")],
        [sg.Text("",key="display",font=("Helvetica",25))],
        [sg.Button("Calculate",size=(40,1))]]
window=sg.Window("@16 Quadratic Equation Solver",layout)
while True:
    event,values=window.read(timeout=100)
    if event==None:
        window.close()
        break
    if len(values["-a-"])>10:
        values["-a-"]=values["-a-"][:10]
    if len(values["-b-"])>10:
        values["-b-"]=values["-b-"][:10]
    if len(values["-c-"])>10:
        values["-c-"]=values["-c-"][:10]
    try:
        d1=eval(values["-a-"])
        if d1==0:
            window.find_element("cb1").Update(text_color="red")
            window.find_element("cb1").Update("✖")
        else:
            window.find_element("cb1").Update(text_color="green2")
            window.find_element("cb1").Update("✔")
        if d1<0:
            sgn1=""
        else:
            sgn1=""
    except:
        window.find_element("cb1").Update(text_color="red")
        window.find_element("cb1").Update("✖")
        d1="a"
        sgn1=""
    try:
        d2=eval(values["-b-"])
        window.find_element("cb2").Update(text_color="green2")
        window.find_element("cb2").Update("✔")
        if d2<0:
            sgn2=""
        else:
            sgn2="+"
    except:
        window.find_element("cb2").Update(text_color="red")
        window.find_element("cb2").Update("✖")
        d2="b"
        sgn2="+"
    try:
        d3=eval(values["-c-"])
        window.find_element("cb3").Update(text_color="green2")
        window.find_element("cb3").Update("✔")
        if d3<0:
            sgn3=""
        else:
            sgn3="+"
    except:
        window.find_element("cb3").Update(text_color="red")
        window.find_element("cb3").Update("✖")
        d3="c"
        sgn3="+"
    window.find_element("display").Update(sgn1+str(d1)+"x²"+sgn2+str(d2)+"x"+sgn3+str(d3)+"=0")
    if event==None:
        window.close()
        break
    elif event=="Calculate":
        acres=values["-a-"]
        beaches=values["-b-"]
        court=values["-c-"]
        try:
            window.find_element("Calculate").Update(disabled=True)
            a9=eval(acres)
            b99=eval(beaches)
            c999=eval(court)
            discrim=((b99**2)-(4*a9*c999))**0.5
            s1=(-b99+discrim)/(2*a9)
            s2=(-b99-discrim)/(2*a9)
            solution(s1,s2)
            window.find_element("Calculate").Update(disabled=False)
            window.find_element("-a-").Update("")
            window.find_element("-b-").Update("")
            window.find_element("-c-").Update("")
            window.Element('-a-').SetFocus()
        except TypeError:
            fail(random.choice(typeerr))
            window.find_element("Calculate").Update(disabled=False)
        except NameError:
            fail(random.choice(typeerr))
            window.find_element("Calculate").Update(disabled=False)
        except SyntaxError:
            fail(random.choice(typeerr))
            window.find_element("Calculate").Update(disabled=False)
        except ZeroDivisionError:
            fail(random.choice(zrdvserr))
            window.find_element("Calculate").Update(disabled=False)
        except:
            fail(random.choice(err))
            window.find_element("Calculate").Update(disabled=False)
