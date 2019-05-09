"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zixin Fan.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding = 10)
    frame.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button1 = ttk.Button(frame, text = 'Button 1')
    button1.grid()

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    button1['command'] = (lambda : print_Hello_on_the_Console())

    # -------------------------------------------------------------------------
    # TODO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry1 = ttk.Entry(frame)
    entry1.grid()

    button2 = ttk.Button(frame, text = 'Button 2')
    button2.grid()

    entrybox1 = entry1.get()
    if str(entrybox1) == str('ok'):
        button2['command'] = (lambda : print_Hello_on_the_Console())
    else:
        button2['command'] = (lambda : print_Goodbye_on_the_Console())

    # -------------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry2 = ttk.Entry(frame)
    entry2.grid()

    button3 = ttk.Button(frame, text='Button 2')
    button3.grid()

    # -------------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------



    root.mainloop()



def print_Hello_on_the_Console():
    print('Hello')


def print_Goodbye_on_the_Console():
    print('Goodbye')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
