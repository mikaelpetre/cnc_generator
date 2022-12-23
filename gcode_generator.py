from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lathe Gcode generator")
root.iconbitmap('C:/Users/mikae/OneDrive/Dokument/Programmering/bimex_cnc_generator/brush.ico')
root.geometry("400x400")

# Create function to show program

def show():
    show_program = Tk()
    show_program.title("Visa program")
    show_program.iconbitmap('C:/Users/mikae/OneDrive/Dokument/Programmering/bimex_cnc_generator/brush.ico')
    show_program.geometry("400x400")

    # Create label which will show program

    listToStr = " ".join(map(str, program))

    program_label = Label(show_program, text= "% \n O4536 \n G50 S5000 \n P1 M98 \n" + listToStr + "M30 \n %")
    program_label.pack()

# Create function to add operation

def add():
    global op_specs
    global specify_operation
    global tool_box
    global start_dia_box
    global end_dia_box
    global start_z_box
    global doc_x_box
    global doc_z_box
    global leave_x_box
    global leave_z_box
    global no_of_passes_box
    global selected_operation
    op_specs = Tk()
    op_specs.title("Parametrar")
    op_specs.iconbitmap('C:/Users/mikae/OneDrive/Dokument/Programmering/bimex_cnc_generator/brush.ico')
    op_specs.geometry("400x400")

    # Remember selected operation

    selected_operation = variable.get()

    # Create labels and entry boxes common for all operations
    
    # Tool

    tool_label = Label(op_specs, text="Verktyg")
    tool_label.grid(row=0, column=0)

    tool_box = Entry(op_specs, width=10)
    if selected_operation == "Planing":
        tool_box.insert(END, "0303")
    if selected_operation == "Grov utv G71":
        tool_box.insert(END, "0303")
    if selected_operation == "Grov utv G73":
        tool_box.insert(END, "0303")
    if selected_operation == "Finplaning":
        tool_box.insert(END, "0101")
    tool_box.grid(row=0, column=1)

    # Start dia

    start_dia_label = Label(op_specs, text="Positionering i X")
    start_dia_label.grid(row=1, column=0)

    start_dia_box = Entry(op_specs, width=10)
    start_dia_box.grid(row=1, column=1)

    # Start Z

    start_z_label = Label(op_specs, text="Positionering i Z")
    start_z_label.grid(row=2, column=0)

    start_z_box = Entry(op_specs, width=10)
    if selected_operation == "Planing":
        start_z_box.insert(END, "0.2")
    if selected_operation == "Finplaning":
        start_z_box.insert(END, "2")
    if selected_operation == "Grov utv G71":
        start_z_box.insert(END, "2")
    if selected_operation == "Grov utv G73":
        start_z_box.insert(END, "2")
    start_z_box.grid(row=2, column=1)

    # Create entry boxes and labels for some operations

    if selected_operation == "Planing":

        # End dia

        end_dia_label = Label(op_specs, text="Slut dia")
        end_dia_label.grid(row=3, column=0)
        
        end_dia_box = Entry(op_specs, width=10)
        end_dia_box.insert(END, "-1")
        end_dia_box.grid(row=3, column=1)

        # Depth of cut

        doc_z_label = Label(op_specs, text="Skärdjup i Z")
        doc_z_label.grid(row=4, column=0)

        doc_z_box = Entry(op_specs, width=10)
        doc_z_box.insert(END, "0.1")
        doc_z_box.grid(row=4, column=1)

        # Leave Z

        leave_z_label = Label(op_specs, text="Lämna i Z")
        leave_z_label.grid(row=5, column=0)
    
        leave_z_box = Entry(op_specs, width=10)
        leave_z_box.insert(END, "0.05")
        leave_z_box.grid(row=5, column=1)

    if selected_operation == "Grov utv G71":

        # Depth of cut X

        doc_x_label = Label(op_specs, text="Skärdjup i X")
        doc_x_label.grid(row=3, column=0)

        doc_x_box = Entry(op_specs, width=10)
        doc_x_box.insert(END, "0.2")
        doc_x_box.grid(row=3, column=1)

        # Leave X

        leave_x_label = Label(op_specs, text="Lämna i X")
        leave_x_label.grid(row=4, column=0)
    
        leave_x_box = Entry(op_specs, width=10)
        leave_x_box.insert(END, "0.08")
        leave_x_box.grid(row=4, column=1)

        # Leave Z

        leave_z_label = Label(op_specs, text="Lämna i Z")
        leave_z_label.grid(row=5, column=0)
    
        leave_z_box = Entry(op_specs, width=10)
        leave_z_box.insert(END, "0.05")
        leave_z_box.grid(row=5, column=1)

    if selected_operation == "Grov utv G73":

        # Depth of cut X

        doc_x_label = Label(op_specs, text="Skärdjup i X")
        doc_x_label.grid(row=3, column=0)

        doc_x_box = Entry(op_specs, width=10)
        doc_x_box.insert(END, "0.2")
        doc_x_box.grid(row=3, column=1)

        # Depth of cut Z

        doc_z_label = Label(op_specs, text="Skärdjup i Z")
        doc_z_label.grid(row=4, column=0)

        doc_z_box = Entry(op_specs, width=10)
        doc_z_box.insert(END, "0.2")
        doc_z_box.grid(row=4, column=1)

        # Number of passes

        no_of_passes_label = Label(op_specs, text="Antal passeringar")
        no_of_passes_label.grid(row=5, column=0)
    
        no_of_passes_box = Entry(op_specs, width=10)
        no_of_passes_box.insert(END, "3")
        no_of_passes_box.grid(row=5, column=1)

        # Leave X

        leave_x_label = Label(op_specs, text="Lämna i X")
        leave_x_label.grid(row=6, column=0)
    
        leave_x_box = Entry(op_specs, width=10)
        leave_x_box.insert(END, "0.08")
        leave_x_box.grid(row=6, column=1)

        # Leave Z

        leave_z_label = Label(op_specs, text="Lämna i Z")
        leave_z_label.grid(row=7, column=0)
    
        leave_z_box = Entry(op_specs, width=10)
        leave_z_box.insert(END, "0.05")
        leave_z_box.grid(row=7, column=1)

        

    # Create Submit Button

    save_op = Button(op_specs, text="Spara", command=save)
    save_op.grid(row=10, column=0, columnspan=2)

# Create function to save program

def save():
    global tool
    global start_dia
    global end_dia
    global start_z
    global doc_z
    global leave_z
    global selected_operation
    global drop_selected_ops
    global variable_1
    global program

    # Get the values from the boxes

    tool = tool_box.get()
    start_dia = start_dia_box.get()
    start_z = start_z_box.get()

    end_dia = "?"
    doc_x = "?"
    doc_z = "?"
    leave_x = "?"
    leave_z = "?"
    no_of_passes = "?"


    if selected_operation == "Planing":
        end_dia = end_dia_box.get()
        doc_z = doc_z_box.get()
        leave_z = leave_z_box.get()
    
    if selected_operation == "Grov utv G71":
        doc_x = doc_x_box.get()
        leave_x = leave_x_box.get()
        leave_z = leave_z_box.get()

    if selected_operation == "Grov utv G73":
        doc_x = doc_x_box.get()
        doc_z = doc_z_box.get()
        no_of_passes = no_of_passes_box.get()
        leave_x = leave_x_box.get()
        leave_z = leave_z_box.get()

    operation_formulas = {
        "planing_formula": "G96 S140 T" + str(tool) + " M14 \n G0 X" + str(start_dia) + " Z" + str(start_z) + "\n G72 W" + str(doc_z) + " R1 \n G72 P3 Q4 U0 W" + str(leave_z) + " F0.1 \n N3 G1 Z0 \n G1 X" + str(end_dia) + "\n N4 G0 Z2 \n P1 M98 \n",
        "finplaning_formula": "G96 S140 T" + str(tool) + " M14 F0.04 \n G0 X" + str(start_dia) + " Z" + str(start_z) + " \n G70 P3 Q4 \n P1 M98 \n",
        "G71_formula": "G96 S140 T" + str(tool) + " M14 \n G0 X" + str(start_dia) + " Z" + str(start_z) + "\n G71 U" + str(doc_x) + " R2 \n G71 P1 Q2 U" + str(leave_x) + " W" + str(leave_z) + " F0.1 \n N1 G0 " + "hejhej" + "\n P1 M98 \n",
        "G73_formula": "G96 S140 T" + str(tool) + " M14 \n G0 X" + str(start_dia) + " Z" + str(start_z) + "\n G73 U" + str(doc_x) + " W" + str(doc_z) + " R" + str(no_of_passes) + "\n G71 P1 Q2 U" + str(leave_x) + " W" + str(leave_z) + " F0.1 \n N1 G0 " + "hejhej" + "\n P1 M98 \n",
    }
    

    selected_operations.append(selected_operation)

    # Show error message if no planing is selected. This is not working, please fix.
    # if "Planing" not in selected_operations:
    #    messagebox.error("Error", "Du måste ha en planing för att kunna ha en finplaning")

    if selected_operation == "Planing":
        operation_formula = operation_formulas.get("planing_formula")
    if selected_operation == "Finplaning":
        operation_formula = operation_formulas.get("finplaning_formula")
    if selected_operation == "Grov utv G71":
        operation_formula = operation_formulas.get("G71_formula")
    if selected_operation == "Grov utv G73":
        operation_formula = operation_formulas.get("G73_formula")

    program.append(operation_formula)

    # Update main window 

    variable_1 = StringVar()
    variable_1.set(selected_operations[0]) # Default value
    
    
    # Create a button in main window to show operation specs

    edit_op_button = Button(root, text=selected_operation, state=DISABLED)
    edit_op_button.grid(row=len(selected_operations), column=0)

    # Create a button in main window to show program

    show_program_button = Button(root, text="Visa program", command=show)
    show_program_button.grid(row=0, column=4)


    op_specs.destroy()

# Main window

# Create list for your program

program = []

# Create list for available operations

operations = [
    "Planing",
    "Finplaning",
    "Grov utv G71",
    "Grov utv G73"
]

# Create list for selected operations

selected_operations = []

# Create a dropdown menu to choose operation

variable = StringVar()
variable.set("Planing") # Default value

drop_ops = OptionMenu(root, variable, *operations)
drop_ops.grid(row=0, column=1)

# Create labels for dropdown menus

select_op_label = Label(root, text="Välj operation:")
select_op_label.grid(row=0, column=0)

# Create a button to select operation

op_button = Button(root, text="Lägg till", command=add)
op_button.grid(row=0, column=2)

root.mainloop()