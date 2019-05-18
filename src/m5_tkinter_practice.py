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
    button1['command'] = lambda: print_Hello_on_the_Console()

    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
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

    button2['command'] = lambda : print_Hello_or_Goodbye_on_the_Console(entry1)

    # -------------------------------------------------------------------------
    # DONE: 7.
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

    button3 = ttk.Button(frame, text='Button 3')
    button3.grid()

    button3['command'] = lambda: print_N_times(entry1, entry2)

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    '''
    Button 4: print the string in the FIRST Entry box for N times in diagonal, where N is the integer input in the 
              SECOND Entry Box, but no letters are in the same column.
    '''
    button4 = ttk.Button(frame, text = 'Print in diagonal')
    button4.grid()

    button4['command'] = lambda: print_in_diagonal(entry1, entry2)


    root.mainloop()



def print_Hello_on_the_Console():
    print('Hello')


def print_Hello_or_Goodbye_on_the_Console(entry1):
    content = entry1.get()
    if content == 'ok':
        print('Hello')
    else:
        print('Goodbye')


def print_N_times(entry1, entry2):
    string = entry1.get()
    N = int(entry2.get())
    print(string * N)


def print_in_diagonal(entry1, entry2):
    string = entry1.get()
    N = int(entry2.get())

    for k in range(N):
        print(' ' * len(string) * k + string)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
