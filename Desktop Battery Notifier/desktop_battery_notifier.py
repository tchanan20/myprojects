from plyer import notification 
import psutil

battery = psutil.sensors_battery()

plugged = battery.power_plugged

if __name__=="__main__": 
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify( 
            #title of notification
            title = "Plugged In", 

            #message of notification
            message=" For better battery life, charge upto 80%" , 
            
            #path to icon
            app_icon="plug_in_icon.ico",
            
            # displaying time 
            timeout=2 
            )
           
        elif percent == 100: 
            notification.notify( 
            title = "Plugged In", 
            message=" Please plugged out the charger. Battery is charged" , 
            app_icon="full_icon.ico",
            timeout=2 
            )
           
        else :
            notification.notify( 
            title = "Plugged In", 
            message=" Remove the charger please. For better battery life charge up to 80%" ,
            app_icon="charging_icon.ico", 
            timeout=2 
            )

    else:
        percent = battery.percent
        if percent <=20:
            notification.notify( 
            title = "Battery Reminder", 
            message="Your battery is running low. You might want to plug in your PC " , 
            app_icon="empty_battery.ico",
            timeout=2 
            )
       
        elif percent <=50:
            notification.notify( 
            title = "Battery Reminder", 
            message=f" Battery is {percent}." ,
            timeout=2 
            )
        
        elif percent == 100:
            notification.notify( 
            title = "Battery Reminder", 
            message="Fully charged" , 
            app_icon="full_battery.ico",
            timeout=2 
            )

        else:
            notification.notify( 
            title = "Battery Reminder", 
            message=f"Battery is {percent}" , 
            timeout=2
            ) 
