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

# Create function to save program

def save():
    global tool
    global start_dia
    global end_dia
    global stock_z
    global doc_z
    global leave_z
    global selected_operation
    global drop_selected_ops
    global variable_1
    global program

    # Get the values from the boxes
    tool = tool_box.get()
    start_dia = start_dia_box.get()
    stock_z = stock_z_box.get()

    if selected_operation == "Planing":
        end_dia = end_dia_box.get()
        doc_z = doc_z_box.get()
        leave_z = leave_z_box.get()
    else:
        end_dia = "?"
        doc_z = "?"
        leave_z = "?"

    operation_formulas = {
        "planing_formula": "G96 S140 T" + str(tool) + " M14 \n G0 X" + str(start_dia) + " Z" + str(stock_z) + "\n G72 W" + str(doc_z) + " R1 \n G72 P3 Q4 U0 W" + str(leave_z) + " F0.1 \n N3 G1 Z0 \n G1 X" + str(end_dia) + "\n N4 G0 Z2 \n P1 M98 \n",
        "finplaning_formula": "G96 S140 T" + str(tool) + " M14 F0.04 \n G0 X" + str(start_dia) + " Z" + str(stock_z) + " \n G70 P3 Q4 \n P1 M98 \n"
    }
    

    selected_operations.append(selected_operation)

    # Show error message if no planing is selected. This is not working, please fix.
    # if "Planing" not in selected_operations:
    #    messagebox.error("Error", "Du måste ha en planing för att kunna ha en finplaning")

    if selected_operation == "Planing":
        operation_formula = operation_formulas.get("planing_formula")
    if selected_operation == "Finplaning":
        operation_formula = operation_formulas.get("finplaning_formula")

    program.append(operation_formula)

    # Update main window 

    variable_1 = StringVar()
    variable_1.set(selected_operations[0]) # Default value
    
    
    # Create a button in main window to show operation specs
    edit_op_button = Button(root, text=selected_operation, command=view_specs)
    edit_op_button.grid(row=len(selected_operations), column=0)

    # Create a button in main window to show program
    show_program_button = Button(root, text="Visa program", command=show)
    show_program_button.grid(row=0, column=4)


    op_specs.destroy()


# Create function to add operation

def add():
    global op_specs
    global specify_operation
    global tool_box
    global start_dia_box
    global end_dia_box
    global stock_z_box
    global doc_z_box
    global leave_z_box
    global selected_operation
    op_specs = Tk()
    op_specs.title("Parametrar")
    op_specs.iconbitmap('C:/Users/mikae/OneDrive/Dokument/Programmering/bimex_cnc_generator/brush.ico')
    op_specs.geometry("400x400")

    # Remember selected operation
    selected_operation = variable.get()

    # Create labels and entry boxes common for all operations
    tool_label = Label(op_specs, text="Verktyg")
    tool_label.grid(row=0, column=0)

    start_dia_label = Label(op_specs, text="Positionering i X")
    start_dia_label.grid(row=1, column=0)

    stock_z_label = Label(op_specs, text="Positionering i Z")
    stock_z_label.grid(row=2, column=0)

    tool_box = Entry(op_specs, width=10)
    if selected_operation == "Planing":
        tool_box.insert(END, "0303")
    if selected_operation == "Finplaning":
        tool_box.insert(END, "0101")
    tool_box.grid(row=0, column=1)

    start_dia_box = Entry(op_specs, width=10)
    start_dia_box.grid(row=1, column=1)

    stock_z_box = Entry(op_specs, width=10)
    if selected_operation == "Planing":
        stock_z_box.insert(END, "2")
    if selected_operation == "Finplaning":
        stock_z_box.insert(END, "2")
    stock_z_box.grid(row=2, column=1)

    # Create entry boxes and labels for some operations

    if selected_operation == "Planing":

        end_dia_label = Label(op_specs, text="Slut dia")
        end_dia_label.grid(row=3, column=0)
        
        end_dia_box = Entry(op_specs, width=10)
        end_dia_box.insert(END, "-1")
        end_dia_box.grid(row=3, column=1)
        
        doc_z_label = Label(op_specs, text="Skärdjup i Z") # Depth of Cut
        doc_z_label.grid(row=4, column=0)

        leave_z_label = Label(op_specs, text="Lämna i Z")
        leave_z_label.grid(row=5, column=0)

        doc_z_box = Entry(op_specs, width=10)
        doc_z_box.insert(END, "0.1")
        doc_z_box.grid(row=4, column=1)
    
        leave_z_box = Entry(op_specs, width=10)
        leave_z_box.insert(END, "0.05")
        leave_z_box.grid(row=5, column=1)

    # Create Submit Button

    save_op = Button(op_specs, text="Spara", command=save)
    save_op.grid(row=6, column=0, columnspan=2)
    
def view_specs():
    op_specs = Tk()
    op_specs.title("Parametrar")
    op_specs.iconbitmap('C:/Users/mikae/OneDrive/Dokument/Programmering/bimex_cnc_generator/brush.ico')
    op_specs.geometry("400x400")

    # Create labels and entry boxes common for all operations
    tool_label = Label(op_specs, text="Verktyg")
    tool_label.grid(row=0, column=0)

    start_dia_label = Label(op_specs, text="Positionering i X")
    start_dia_label.grid(row=1, column=0)

    stock_z_label = Label(op_specs, text="Positionering i Z")
    stock_z_label.grid(row=2, column=0)

    tool_box = Entry(op_specs, width=10)
    tool_box.grid(row=0, column=1)

    start_dia_box = Entry(op_specs, width=10)
    start_dia_box.grid(row=1, column=1)

    stock_z_box = Entry(op_specs, width=10)
    stock_z_box.grid(row=2, column=1)


    # Create labels for entry boxes for specific operations
    if selected_operation == "Planing":
        end_dia_label = Label(op_specs, text="Slut dia")
        end_dia_label.grid(row=3, column=0)

        doc_z_label = Label(op_specs, text="Skärdjup i Z") # Depth of Cut
        doc_z_label.grid(row=4, column=0)

        leave_z_label = Label(op_specs, text="Lämna i Z")
        leave_z_label.grid(row=5, column=0)

        end_dia_box = Entry(op_specs, width=10)
        end_dia_box.grid(row=3, column=1)

        doc_z_box = Entry(op_specs, width=10)
        doc_z_box.grid(row=4, column=1)
    
        leave_z_box = Entry(op_specs, width=10)
        leave_z_box.grid(row=5, column=1)

    # Create Submit Button

    save_op = Button(op_specs, text="Spara", command=save, state=DISABLED)
    save_op.grid(row=6, column=0, columnspan=2)

    # Insert values
    tool_box.insert(0, tool)
    start_dia_box.insert(0, start_dia)
    stock_z_box.insert(0, stock_z)

    if selected_operation == "Planing":
        end_dia_box.insert(0, end_dia)
        doc_z_box.insert(0, doc_z)
        leave_z_box.insert(0, leave_z)

# Main window
# Create a dropdown menu to choose operation

program = []

operations = [
    "Planing",
    "Finplaning",
]

selected_operations = []

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