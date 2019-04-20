# =============================================================================
#            IMPORTING THE DEPENDENCIES

#tkinter for preparing the GUI
#requests for making GET request to the web
#Beautiful Soup for parsing the HTML code and scraping information
# =============================================================================

import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


# =============================================================================
#               MAIN FUNCTION
# =============================================================================

def getinfo(name):
# =============================================================================
#       Calling two functions. One function will fetch the intro, the other
#       will fetch the birthday
# =============================================================================
    getcelebintro(name)
    getcelebbirthday(name)


# =============================================================================
#            CELEBRITY INTRO FUNCTION
# =============================================================================

def getcelebintro(name):


    base_url = "https://en.wikipedia.org/wiki/"
    famous = name.split()
    famous_person_url = ""

    for i in range(len(famous)):
        last_index = len(famous) - 1

        if (i==0):
            famous_person_url = famous[i] + "_"

        elif (i == last_index):
            famous_person_url = famous_person_url + famous[i]

        else:
            famous_person_url = famous_person_url + famous[i] + "_"

    final_url = base_url + famous_person_url


    try:
        print(final_url)
        source_code = requests.get(final_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)


        paragraphs = soup.select("p")
        intro = '\n'.join([ para.text for para in paragraphs[1:2]])
        print ("Intro : " + intro)


        if not any(c.isalpha() for c in intro):
            print("in if condition")
            intro = '\n'.join([ para.text for para in paragraphs[2:4]])


        print ("Intro : " + intro)
        label['text'] = intro_format_response(intro)


    except:
        label['text'] = "Error : Either no such person exist or spelling is incorrect. Try again."

# =============================================================================
#              CELEBRITY BIRTHDAY FUNCTION
# =============================================================================

def getcelebbirthday(name):

    base_url = "https://en.wikipedia.org/wiki/"
    famous = name.split()

    famous_person_url = ""

    for i in range(len(famous)):
        last_index = len(famous) - 1

        if (i==0):
            famous_person_url = famous[i] + "_"

        elif (i == last_index):
            famous_person_url = famous_person_url + famous[i]

        else:
            famous_person_url = famous_person_url + famous[i] + "_"

    final_url = base_url + famous_person_url


    try:
        source_code = requests.get(final_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        birthday = soup.find("span",{"class":"bday"}).string
        info = birthday.split("-")
        year = info[0]
        month = info[1]
        day = info[2]

        str = "Birthday : " + birthday
        label2['text'] = birthday_format_response(year, month, day)


    except:
        label2['text'] = "Error : Either no such person exist or spelling is incorrect. Try again."



# =============================================================================
#            FORMATTING THE INTRO RESPONSE
# =============================================================================

def intro_format_response(intro):

# =============================================================================
#     Depending on the length of the paragraph, the intro can get very long. This
#     simple formatting logic ensures that it breaks into a new line after every
#     15 words so that I can properly display the returned string in the text field.
# =============================================================================

    words = intro.split()
    new_text = ""
    word_count = 0

    for word in words:
        new_text += word +" "
        word_count += 1

        if word_count == 15:
            new_text+= "\n"
            word_count = 0

    return new_text


# =============================================================================
#            FORMATTING THE BIRTHDAY RESPONSE
# =============================================================================

def birthday_format_response(year, month, day):

    str = 'Birth Year: %s \n Birth Month : %s \n Birth Day : %s' % (year, month, day)
    return str


# =============================================================================
#              BUILDING THE GUI

#    the function names of the tkinter is pretty intuitive. Refer to the
#    documenation to understand the parameters available for customization.
# =============================================================================


root = tk.Tk()

root.title('Get Information Program')

HEIGHT = 900
WIDTH = 900

root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pic.png', master=root)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg = 'white')
entry.place(relwidth=0.65, relheight=1)

button_1 = ttk.Button(frame, text="Get Info", command=lambda: getinfo(entry.get()))
button_1.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame2 = tk.Frame(root, bg='white', bd=5)
lower_frame2.place(relx=0.5, rely=0.22, relwidth=0.9, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='white', bd=5)
lower_frame.place(relx=0.5, rely=0.34, relwidth=0.9, relheight=0.6, anchor='n')

# =============================================================================
# I have an extra text field positioned perfectly in case I want to add an extra
# feature in the future.
# =============================================================================

#lower_frame3 = tk.Frame(root, bg='white', bd=5)
#lower_frame3.place(relx=0.5, rely=0.76, relwidth=0.9, relheight=0.1, anchor='n')

label = tk.Label(lower_frame, bg='white')
label.place(relwidth=1, relheight=1)

label2 = tk.Label(lower_frame2, bg='white')
label2.place(relwidth=1, relheight=1)


root.mainloop()

