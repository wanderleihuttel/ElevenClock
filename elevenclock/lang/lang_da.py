# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_2_1 = {
    "Open online help to troubleshoot problems": "",
    "Reset ElevenClock preferences to defaults": "",
    "Specify a minimum width for the clock": "",
    "Search on the settings": "",
    "No results were found": "",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "",
    "Enable low-cpu mode": "",
    "You might lose functionalities, like the notification counter or the dynamic background": "",
    "Clock position and size:": "",
    "Clock size preferences, position offset, clock at the left, etc.": "",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "",
    "View": "",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "",
    "Ok": "",
    "More Info": "",
    "About Qt": "",
    "Success": "",
    "The monitors were unblacklisted successfully.": "",
    "Now you should see the clock everywhere": "",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "",
    "Change date and time": "",
    "Notification settings": "",
    "Updates, icon tray, language": "",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "",
    'Add the "Show Desktop" button on the left corner of every clock': '',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '',
    "Clock's font, font size, font color and background, text alignment": "",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "",
    "Testing features and error-fixing tools": "",
    "Language pack author(s), help translating ElevenClock": "",
    "Info, report a bug, submit a feature request, donate, about": "",
    "Log, debugging information": "",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "",
    "Show the clock on the primary screen": "",
    "Use a custom font color": "",
    "Use a custom background color": "",
    "Align the clock text to the center": "",
    "Select custom color": "",
    "Hide the clock when a program occupies all screens": "",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Brug en brugerdefineret skrifttype",
    "Use a custom font size": "Brug en brugerdefineret skriftstørrelse",
    "Enable hide when multi-monitor fullscreen apps are running": "Aktiver skjul når multi-skærm fuldskærm apps kører",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> skal være slået til for at ændre denne indstilling",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> skal være slået fra for at ændre denne indstilling",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Denne funktion er blevet slået fra, fordi den burde virke som standard. Hvis den ikke er, så rapporter venligst en fejl)",
    "ElevenClock's language": "ElevenClocks sprog"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (PySide6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativ ikke-SSL opdateringsserver (Dette kan muligvis hjælpe med SSL fejl)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Rettelser og andre eksperimentelle funktioner: (Brug KUN hvis noget ikke virker)",
    "Show week number on the clock": ""
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Skjul uret når RDP Client eller Citrix Workspace kører",
    "Clock Appearance:": "Urstil",
    "Force the clock to have black text": "Tving uret til at have sort tekst",
    " - It is required that the Dark Text checkbox is disabled": " - Det er påkrævet at Mørk Tekst afkrydsningsfeltet er slået fra",
    "Debbugging information:": "Fejlretningsinformation",
    "Open ElevenClock's log": "Åben ElevenClocks log",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Vis uret på den primære skærm (Brugbart hvis uret er indstillet til venstre)",
    "Show weekday on the clock"  :"Vis dag på uret",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock indstillinger", # Also settings title
    "Reload Clocks"             :"Genindlæs ure",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Genstart ElevenClock",
    "Hide ElevenClock"          :"Skjul ElevenClock",
    "Quit ElevenClock"          :"Afslut ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Generelle indstillinger:",
    "Automatically check for updates"                                                   :"Kig automatisk efter opdateringer",
    "Automatically install available updates"                                           :"Installér automatisk tilgængelige opdateringer",
    "Enable really silent updates"                                                      :"Aktiver virkelig stille opdateringer",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Omgå opdateringsleverandør autenticitets tjek (IKKE ANBEFALET, BRUG PÅ EGET ANSVAR)",
    "Show ElevenClock on system tray"                                                   :"Vis ElevenClock under skjulte ikoner",
    "Alternative clock alignment (may not work)"                                        :"Alternativ urplacering (virker muligvis ikke)",
    "Change startup behaviour"                                                          :"Ændr startup adfærd",
    "Change"                                                                            :"Ændr",
    "<b>Update to the latest version!</b>"                                             :"<b>Opdater til den nyeste version!</b>",
    "Install update"                                                                    :"Installér opdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Urindstillinger",
    "Hide the clock in fullscreen mode"                            :"Skjul uret i fuldskærmstilstand",
    "Hide the clock when RDP client is active"                     :"Skjul uret når RDP klient er aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tving uret til at være på bunden af skærmen",
    "Show the clock when the taskbar is set to hide automatically" :"Vis uret når proceslinjen er sat til at skjule automatisk",
    "Fix the hyphen/dash showing over the month"                   :"Fiks bindestregen/tankestregen viser over måneden",
    "Force the clock to have white text"                           :"Tving uret til at have hvid tekst",
    "Show the clock at the left of the screen"                     :"Vis uret til venstre på skærmen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Dato- og tidsindstillinger",
    "Show seconds on the clock"                         :"Vis sekunder på uret",
    "Show date on the clock"                            :"Vis dato på uret",
    "Show time on the clock"                            :"Vis tid på uret",
    "Change date and time format (Regional settings)"   :"Ændr dato- og tidsformat (Regionale indstillinger)",
    "Regional settings"                                 :"Regionale indstillinger",
    
    #About the language pack
    "About the language pack:"                  :"Om sprogpakken",
    "Translated to English by martinet101"      :"Oversat til dansk af Sebblich", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Oversæt ElevenClock til dit sprog",
    "Get started"                               :"Kom i gang",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Vis ElevenClocks hjemmeside",
    "Open"                                      :"Åben",
    "Report an issue/request a feature"         :"Rapportér et problem/anmod om en funktion",
    "Report"                                    :"Rapportér",
    "Support the dev: Give me a coffee☕"       :"Støt skaberen: Giv dem en kaffe☕",
    "Open page"                                 :"Åben side",
    "Icons by Icons8"                           :"Ikoner af Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Hjemmeside",
    "Close settings"                            :"Luk indstillinger",
    "Close"                                     :"Luk",
}

lang = lang2_3
