import tkinter as tk

updateTimeMS = 100

def Update():
    print("Looping")
    errorValue['text'] = "0"
    root.after(updateTimeMS, Update)

def Close():
    root.destroy()

root = tk.Tk()
root.title("Max Dash")
root.geometry('{}x{}'.format(1024, 540))

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

bgColor = "#121212"
borderColor = "#151515"
borderThickness = 2

objectWidth = (1024/3)
objectHeight = (540/4)

Error = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
RPM = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
IA = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)

Error.grid(row=0, column=1, sticky="new")
RPM.grid(row=0, column=2, sticky="new")
IA.grid(row=0, column=3, sticky="new")

OP = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
OT = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
IAT = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)

OP.grid(row=1, column=1, sticky="new")
OT.grid(row=1, column=2, sticky="new")
IAT.grid(row=1, column=3, sticky="new")

CT = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
AFR = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
TPS = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)

CT.grid(row=2, column=1, sticky="new")
AFR.grid(row=2, column=2, sticky="new")
TPS.grid(row=2, column=3, sticky="new")

MAP = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
BV = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)
EXIT = tk.Frame(root, bg=bgColor, width=objectWidth, height=objectHeight, pady=3, highlightbackground=borderColor, highlightthickness=borderThickness)

MAP.grid(row=3, column=1, sticky="new")
BV.grid(row=3, column=2, sticky="new")
EXIT.grid(row=3, column=3, sticky="new")

#Error FIELD
Error.grid_propagate(False)
errorTextF = tk.Frame(Error,background=bgColor, width=336, height=70)
errorTextF.grid(row=0, column=0, sticky="NW")
errorText = tk.Label(errorTextF, text="Errors", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

errorValueF = tk.Frame(Error,background=bgColor, width=336, height=70)
errorValueF.grid(row=1, column=0, sticky="SW")
errorValue = tk.Label(errorValueF, text="4", bg=bgColor, fg="white", font=("Arial", 40))
errorValue.place(relx=0.5, rely=0.5, anchor="center")

#RPM FIELD
RPM.grid_propagate(False)
rpmTextF = tk.Frame(RPM,background=bgColor, width=336, height=70)
rpmTextF.grid(row=0, column=0, sticky="NW")
rpmText = tk.Label(rpmTextF, text="RPM", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

rpmValueF = tk.Frame(RPM,background=bgColor, width=336, height=70)
rpmValueF.grid(row=1, column=0, sticky="SW")
rpmValue = tk.Label(rpmValueF, text="8000", bg=bgColor, fg="white", font=("Arial", 40))
rpmValue.place(relx=0.5, rely=0.5, anchor="center")

#IA FIELD
IA.grid_propagate(False)
iaTextF = tk.Frame(IA,background=bgColor, width=336, height=70)
iaTextF.grid(row=0, column=0, sticky="NW")
iaText = tk.Label(iaTextF, text="Ignition Angle", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

iaValueF = tk.Frame(IA,background=bgColor, width=336, height=70)
iaValueF.grid(row=1, column=0, sticky="SW")
iaValue = tk.Label(iaValueF, text="10.5btd", bg=bgColor, fg="white", font=("Arial", 40))
iaValue.place(relx=0.5, rely=0.5, anchor="center")

#OP FIELD
OP.grid_propagate(False)
opTextF = tk.Frame(OP,background=bgColor, width=336, height=70)
opTextF.grid(row=0, column=0, sticky="NW")
opText = tk.Label(opTextF, text="Oil Pressure", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

opValueF = tk.Frame(OP,background=bgColor, width=336, height=70)
opValueF.grid(row=1, column=0, sticky="SW")
opValue = tk.Label(opValueF, text="300.5kpa", bg=bgColor, fg="white", font=("Arial", 40))
opValue.place(relx=0.5, rely=0.5, anchor="center")

#OT FIELD
OT.grid_propagate(False)
otTextF = tk.Frame(OT,background=bgColor, width=336, height=70)
otTextF.grid(row=0, column=0, sticky="NW")
otText = tk.Label(otTextF, text="Oil Temp", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

otValueF = tk.Frame(OT,background=bgColor, width=336, height=70)
otValueF.grid(row=1, column=0, sticky="SW")
otValue = tk.Label(otValueF, text="70.5°C", bg=bgColor, fg="white", font=("Arial", 40))
otValue.place(relx=0.5, rely=0.5, anchor="center")

#OT FIELD
IAT.grid_propagate(False)
iatTextF = tk.Frame(IAT,background=bgColor, width=336, height=70)
iatTextF.grid(row=0, column=0, sticky="NW")
iatText = tk.Label(iatTextF, text="Intake Air Temp", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

iatValueF = tk.Frame(IAT,background=bgColor, width=336, height=70)
iatValueF.grid(row=1, column=0, sticky="SW")
iatValue = tk.Label(iatValueF, text="20.5°C", bg=bgColor, fg="white", font=("Arial", 40))
iatValue.place(relx=0.5, rely=0.5, anchor="center")

#CT FIELD
CT.grid_propagate(False)
ctTextF = tk.Frame(CT,background=bgColor, width=336, height=70)
ctTextF.grid(row=0, column=0, sticky="NW")
ctText = tk.Label(ctTextF, text="Coolant Temp", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

ctValueF = tk.Frame(CT,background=bgColor, width=336, height=70)
ctValueF.grid(row=1, column=0, sticky="SW")
ctValue = tk.Label(ctValueF, text="89.5°C", bg=bgColor, fg="white", font=("Arial", 40))
ctValue.place(relx=0.5, rely=0.5, anchor="center")

#AFR FIELD
AFR.grid_propagate(False)
afrTextF = tk.Frame(AFR,background=bgColor, width=336, height=70)
afrTextF.grid(row=0, column=0, sticky="NW")
afrText = tk.Label(afrTextF, text="Air Fuel Ratio", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

afrValueF = tk.Frame(AFR,background=bgColor, width=336, height=70)
afrValueF.grid(row=1, column=0, sticky="SW")
afrValue = tk.Label(afrValueF, text="13.85", bg=bgColor, fg="white", font=("Arial", 40))
afrValue.place(relx=0.5, rely=0.5, anchor="center")

#TPS FIELD
TPS.grid_propagate(False)
tpsTextF = tk.Frame(TPS,background=bgColor, width=336, height=70)
tpsTextF.grid(row=0, column=0, sticky="NW")
tpsText = tk.Label(tpsTextF, text="Throttle positon", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

tpsValueF = tk.Frame(TPS,background=bgColor, width=336, height=70)
tpsValueF.grid(row=1, column=0, sticky="SW")
tpsValue = tk.Label(tpsValueF, text="100.0%", bg=bgColor, fg="white", font=("Arial", 40))
tpsValue.place(relx=0.5, rely=0.5, anchor="center")

#MAP FIELD
MAP.grid_propagate(False)
mapTextF = tk.Frame(MAP,background=bgColor, width=336, height=70)
mapTextF.grid(row=0, column=0, sticky="NW")
mapText = tk.Label(mapTextF, text="MAP", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

mapValueF = tk.Frame(MAP,background=bgColor, width=336, height=70)
mapValueF.grid(row=1, column=0, sticky="SW")
mapValue = tk.Label(mapValueF, text="99.9kpa", bg=bgColor, fg="white", font=("Arial", 40))
mapValue.place(relx=0.5, rely=0.5, anchor="center")

#BV FIELD
BV.grid_propagate(False)
bvTextF = tk.Frame(BV,background=bgColor, width=336, height=70)
bvTextF.grid(row=0, column=0, sticky="NW")
bvText = tk.Label(bvTextF, text="Battery", bg=bgColor, fg="white", font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

bvValueF = tk.Frame(BV,background=bgColor, width=336, height=70)
bvValueF.grid(row=1, column=0, sticky="SW")
bvValue = tk.Label(bvValueF, text="12.00V", bg=bgColor, fg="white", font=("Arial", 40))
bvValue.place(relx=0.5, rely=0.5, anchor="center")

#Exit
EXIT.pack_propagate(False)
exitButton = tk.Button(EXIT, text="Exit!", fg="white", bg="#d11919", font=("Arial", 40), command=Close)
exitButton.pack(expand=True, fill="both")

Update()

tk.mainloop()