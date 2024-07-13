#Travel Planner

import PySimpleGUI as psg;

#Theme
psg.theme("LightBlue1");

#First Layout
def createFirstWindow():
      layout = [
            [psg.Text("Give a name to your travel!")],
            [psg.InputText(size=45)],
            [psg.Text("Where will be the start point?")],
            [psg.InputText(size=45)],
            [psg.Text("Where are your destine?")],
            [psg.InputText(size=45)],
            [psg.Button("Next"), psg.Button("Restore"), psg.Button("Cancel")]
      ];

      return psg.Window("Travel Planner", layout, finalize=True);

#Second Layout
def createSecondWindow():
      layout = [
            [psg.Text("When do you will travel?")],
            [psg.Input()],
            [psg.Text("When your travel will gone?")],
            [psg.Input()],
            [psg.Text("Do you will travel with animal?")],
            [psg.Checkbox("")],
            [psg.Text("How do you go to travel?")],
            [psg.Checkbox("Car"), psg.Checkbox("Bus"), psg.Checkbox("Motocicle"), psg.Checkbox("Walking")],
            [psg.Button("Before"), psg.Button("Ok"), psg.Button("Discart")]
      ];

      return psg.Window("Travel Planner", layout, finalize=True);

window1 = createFirstWindow();

while True:
      events, values = window1.read();

      if (events == psg.WIN_CLOSED or events == "Cancel"):
            window1.close();
            break;
      elif (events == "Restore"):
            window1.close();
            window1 = createFirstWindow();
      elif (events == "Next"):
            window1.disappear();
            window2 = createSecondWindow(); #Create the second window
            events2, values2 = window2.read(); 
            if (events2 == psg.WIN_CLOSED) or (events2 == "Discart"):
                  window2.close();
            elif (events2 == "Ok"):
                  window1.close();
                  window2.close();
                  psg.popup("Your travel has been planed. Congratulations!");
            elif (events2 == "Before"):
                  window2.close();
                  window1.reappear();
