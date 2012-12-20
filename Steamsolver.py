import gtk
import thermo

class SteamSolver:
    def __init__(self):
        '''Initial window which has a combo box from which the user can choose either of     temperature and pressure''' 


        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(500 , 500)
        self.window.set_title('Steam Solver')
        self.window.connect('delete-event' , gtk.main_quit)
        self.window.modify_bg(gtk.STATE_NORMAL , gtk.gdk.Color(red = 20000, blue = 20000 , green = 20000))
        self.TableCreator()       

    def TableCreator(self):
        self.PropertyList =['Pressure' , 'Temperature' , 'Volume(v)' , 'Energy(u)' ,'Enthalpy(h)' , 'Entropy(s)' , 'Quality(x)']
        self.FinalList = []
        self.table = gtk.Table(500 ,500 , True) 
        self.label = gtk.Label('Choose any one')
        self.table.attach(self.label , 25 , 225 , 25 , 60 )
        self.box = gtk.combo_box_new_text()
        self.box.append_text('Pressure')
        self.box.append_text('Temperature')
        self.box.connect('changed' , self.PresTemp)   
        self.table.attach(self.box , 275 , 450 , 25 , 60)
        self.window.add(self.table) 
        self.window.show_all() 



     

    def _helper(self , FinalList):
        try:
           
            Property1 = self.PresTempEnt.get_text() 
            Property2 = self.PropertyEntry.get_text()
            if FinalList[0] == 'P':
                if FinalList[1] == 'Temperature':
                    a = thermo.State(P = float(Property1), T  = float(Property2))   
                    return a

                elif FinalList[1] == 'Volume(v)':
                    a = thermo.State(P = float(Property1), v  = float(Property2))   
                    return a 

                elif FinalList[1] == 'Energy(u)':
                    a = thermo.State(P = float(Property1), u  = float(Property2))   
                    return a

                elif FinalList[1] == 'Enthalpy(h)':
                    a = thermo.State(P = float(Property1), h = float(Property2))   
                    return a

                elif FinalList[1] == 'Entropy(s)':
                    a = thermo.State(P = float(Property1), s  = float(Property2))   
                    return a
   
                elif FinalList[1] == 'Quality(x)':
                    a = thermo.State(P = float(Property1), x  = float(Property2))   
                    return a 

            if FinalList[0] == 'T':
                if FinalList[1] == 'Volume(v)':
                    a = thermo.State(P = float(Property1), v  = float(Property2))   
                    return a 

                elif FinalList[1] == 'Energy(u)':
                    a = thermo.State(P = float(Property1), u  = float(Property2))   
                    return a

                elif FinalList[1] == 'Enthalpy(h)':
                    a = thermo.State(P = float(Property1), h = float(Property2))   
                    return a

                elif FinalList[1] == 'Entropy(s)':
                    a = thermo.State(P = float(Property1), s  = float(Property2))   
                    return a
   
                elif FinalList[1] == 'Quality(x)':
                    a = thermo.State(P = float(Property1), x  = float(Property2))   
                    return a 



        except ValueError:
            a = 'Error'
            return a 

    def PresTemp(self , widget):
        '''Function called when the combo box is changed , the window gets another label and an
        entry into which the user can tpe the required value of temperature and pressure'''      
        index = widget.get_active()
        widget.destroy()
        self.Entry1 = gtk.Entry()
        self.table.attach(self.Entry1 , 275 , 450 , 25 , 60) 
        self.PresTempLab = gtk.Label()
        self.PresTempEnt = gtk.Entry()
        self.table.attach(self.PresTempLab , 25 , 225 , 120 , 155)
        self.table.attach(self.PresTempEnt , 275 , 450 , 120 , 155) 
        if index == 0:
            self.FinalList.append('P') 
            self.PropertyList.remove('Pressure')
            self.PresTempLab.set_text('Enter Pressure')
            self.Entry1.set_text('Pressure')
            self.Entry1.set_editable(False)                        
        else:
            self.FinalList.append('T')
            self.PropertyList.remove('Temperature')
            self.PresTempLab.set_text('Enter Temperature')
            self.Entry1.set_text('Temperature')
            self.Entry1.set_editable(False)  
        self.button = gtk.Button('Process')
        self.button.connect('clicked' , self.Process , index)
        self.table.attach(self.button , 200 , 300 , 420 , 480)  
        self.window.show_all()

    def Process(self , widget , index):
        '''Function called by the button Process , Checks whether the input is valid or not
        If the input is valid , then another label and a combo box are added. The user can
        choose any other property other then temperature or pressure which was entered'''
        UserEntry = self.PresTempEnt.get_text()                
        self.PresTempEnt.set_editable(False)               
        widget.destroy()
        self.SecondStateLab = gtk.Label('Enter Second Property') 
        self.Combo = gtk.combo_box_new_text()
        for Property in self.PropertyList:
            self.Combo.append_text(Property)
        self.Combo.connect('changed' , self.SecState) 
        self.table.attach(self.SecondStateLab , 25 , 225 , 215 , 250)  
        self.table.attach(self.Combo , 275 , 450 , 215 , 250)                               
        self.window.show_all()     

    def SecState(self , widget):
        self.index = widget.get_active()    
        self.PropertyEntry = gtk.Entry()
        self.PropertyLabel = gtk.Label('Enter ' + self.PropertyList[self.index])
        self.FinalList.append(self.PropertyList[self.index])
        widget.destroy()
        self.OptionsLabel = gtk.Entry()
        self.OptionsLabel.set_text(self.PropertyList[self.index])
        self.OptionsLabel.set_editable(False)   
        self.table.attach(self.OptionsLabel , 275 , 450 , 215 , 250)  
        self.table.attach(self.PropertyLabel , 25 , 225 , 310 , 345)
        self.table.attach(self.PropertyEntry , 275 , 450 , 310 , 345)
        self.button2= gtk.Button('Process')
        self.button2.connect('clicked' , self.FinalState)
        self.table.attach(self.button2 , 200 , 300 , 420 , 480) 
        self.window.show_all()
      

    def FinalState(self , widget):
        widget.set_label('Reset')
        a = self._helper(self.FinalList)
        self.label.destroy() 
        self.PresTempLab.destroy()
        self.PresTempEnt.destroy()
        self.Entry1.destroy()
        self.PropertyEntry.destroy()
        self.PropertyLabel.destroy()
        self.OptionsLabel.destroy()
        self.SecondStateLab.destroy()
        if a == 'Error':
            self.warning = gtk.Label('P L E A S E  E N T E R  V A L I D  I N P U T')
            self.table.attach(self.warning , 25 , 475 , 25 , 375)
            self.window.show_all()
  
        else:
            
            self.TemperatureEntry = gtk.Entry()
            self.TemperatureLabel = gtk.Label('Temperature')
            self.PressureEntry = gtk.Entry()
            self.PressureLabel = gtk.Label('Pressure')  
            self.table.attach(self.TemperatureLabel, 25 , 225 , 25 , 55)
            self.table.attach(self.TemperatureEntry , 275 , 450 , 25 , 55)
            self.TemperatureEntry.set_text(str(a.GetTemp()))
            self.TemperatureEntry.set_editable(False) 
            self.table.attach(self.PressureLabel, 25 , 225 , 75 , 105)
            self.table.attach(self.PressureEntry , 275 , 450 , 75 , 105)
            self.PressureEntry.set_text(str(a.GetPressure()))
            self.PressureEntry.set_editable(False) 
            self.VolumeEntry = gtk.Entry()
            self.VolumeLabel = gtk.Label('Volume(v):')               
            self.table.attach(self.VolumeLabel, 25 , 225 , 125 , 155)
            self.table.attach(self.VolumeEntry , 275 , 450 , 125 , 155)
            self.VolumeEntry.set_text(str(a.GetVolume()))
            self.VolumeEntry.set_editable(False) 
            self.EnergyEntry = gtk.Entry()
            self.EnergyLabel = gtk.Label('Internal Energy(U):')
            self.table.attach(self.EnergyLabel, 25 , 225 , 175 , 205)
            self.table.attach(self.EnergyEntry , 275 , 450 , 175 , 205)
            self.EnergyEntry.set_text(str(a.GetEnergy()))
            self.EnergyEntry.set_editable(False)   
            self.EnthalpyEntry = gtk.Entry()
            self.EnthalpyLabel = gtk.Label('Enthalpy(H):')
            self.table.attach(self.EnthalpyLabel, 25 , 225, 225 , 255)
            self.table.attach(self.EnthalpyEntry , 275 , 450 , 225 , 255)
            self.EnthalpyEntry.set_text(str(a.GetEnthalpy()))
            self.EnthalpyEntry.set_editable(False) 
            self.EntropyEntry = gtk.Entry()
            self.EntropyLabel = gtk.Label('Entropy(s):')
            self.table.attach(self.EntropyLabel, 25 , 225 , 275 , 305)
            self.table.attach(self.EntropyEntry , 275 , 450 , 275 , 305)
            self.EntropyEntry.set_text(str(a.GetEntropy()))
            self.EntropyEntry.set_editable(False)    
            self.QualityEntry = gtk.Entry()
            self.QualityLabel = gtk.Label('Quality(x):')
            self.table.attach(self.QualityLabel, 25 , 225 , 325 , 355)
            self.table.attach(self.QualityEntry , 275 , 450 ,325 , 355)
            self.QualityEntry.set_text(str(a.GetQuality()))
            self.QualityEntry.set_editable(False) 
            self.window.show_all()

        widget.connect('clicked' , self.destroy)


    def destroy(self , widget):
        self.table.destroy()
        self.TableCreator()

class main:    
    SteamSolver()
    gtk.main()


if __name__ == '__main__':    
    main()
