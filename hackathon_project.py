# import libraries
import streamlit as st
from PIL import Image
image1 = Image.open('quote1.jpg')
image2 = Image.open('quote2.jpg')
image3 = Image.open('quote3.jpg')
image4 = Image.open('floods.jpg')
image5 = Image.open('hurricane.jpg')
image6 = Image.open('earthquake.jpg')
image7 = Image.open('tornado.jpg')
image8 = Image.open('volcano.jpg')



#navigation
st.sidebar.title('Navigation')
nav = st.sidebar.radio('Go to: ',('Home', 'Offer/Need-help', 'Disaster-information', 'Precautions'))
#Offer/need help page
if nav == "Offer/Need-help":
    st.title('Offer/Need-help')
    
    # ask if they want notification
    st.write("Would you like to be informed of upcoming natural disasters?")
    # TAKE HEIGHT INPUT
    # radio button to choose notification
    status = st.radio('Enter your response: ',
                                    ('Yes', 'No'))
    message = """From: From <ishaan007verma@gmail.com>
    Subject: Email confirmation

    You will get disaster notification on this mail.
    """

    # compare status value
    if(status == 'Yes'):
            # take email input
            email = st.text_input('Email ID : ')
            receivers = email
            
            
    help_status = st.radio(
         "Select option",
         ('Offer help', 'Need help'))

                    

    # check if the button is pressed or not
    if(help_status=="Offer help"):
            st.write("What type of help would you like to offer:")
            alimentary_status = st.checkbox("Alimentary")
            medical_status = st.checkbox("Medical")
            clothing_status = st.checkbox("Clothing")
            other_status = st.checkbox("Other")
            if medical_status or alimentary_status or clothing_status or other_status:
                
                with st.form("information_form", clear_on_submit=True):
                    st.write("Fill the form : ")
                    name1 = st.text_input("Enter your name : ")
                    number1 = st.text_input("Enter your phone number: ")
                    address1 = st.text_input("Enter your current address: ")
                    desc1 = st.text_area("Give a description on the type of help you can provide: ")
                    # Submit button
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        st.success("Success! We will reach out to you as soon as possible")
                        file = open('offer_help.txt','a')
                        file.write(name1 + '\n')
                        file.write(number1 + '\n')
                        file.write(address1 + '\n')
                        file.write(desc1 + '\n')
                        file.write("--------------------\n")
                        file.close()
                        st.balloons()
    elif(help_status=="Need help"):
        st.write("What type of help do you need:")
        alimentary_status2 = st.checkbox("Alimentary")
        shelter_status = st.checkbox("Shelter")
        clothing2 = st.checkbox("Clothing")
        med1 = st.checkbox("Medical assistance")
        other_status = st.checkbox("Other")
        if shelter_status or alimentary_status2 or other_status:
                
            with st.form("information_form", clear_on_submit=True):
                st.write("Fill the form : ")
                name2 = st.text_input("Enter your name : ")
                number2 = st.text_input("Enter your phone number: ")
                country1 = st.selectbox('Country', ('Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'))
                address2 = st.text_input("Enter your current address: ")
                desc2 = st.text_area("Give a description on the type of help you need: ")
                file = open('need_help.txt','a')
                file.write(name2 + '\n')
                file.write(number2 + '\n')
                file.write(country1 + '\n')
                file.write(address2 + '\n')
                file.write(desc2 + '\n')
                file.write("--------------------\n")
                file.close()
                # Submit button
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.success("Success! We will provide you help as soon as possible")
                    st.balloons()


#home page
elif nav == "Home":
    st.title('Welcome to Disaster Management App')
    st.write('''Hello there, welcome to our website! This website provides you basic
    information about natural disasters and also it provides you the option to offer or get help along with precautions you can take during a disaster.''')
    st.image(image1, caption='Quote by Petra Němcová')
    st.image(image2, caption='Quote by Leon Panetta')
    st.image(image3, caption='Quote by Ian Davis')
#disaster information page
elif nav == "Disaster-information":
    st.title('Disasters')
    st.header("Types of disasters : ")
    st.subheader("1. Floods")
    st.image(image4)
    st.write('''A flood is a rise of water with no place to go. Floods come in all depths, from just a couple inches to many feet. The power of floodwater is extraordinary and lethal. In less than an hour, strong rain can turn an ankle deep creek into an unstoppable 30-foot-high swell that overpowers everything in its path.

Floods occur all over the world. Causes of floods include hurricanes, broken levees or dams, rapidly thawing snow, ice jams, and heavy slow moving rain or repeated rains. A flood can happen in a few minutes, hours, days, or over weeks.

No matter how quickly it happens or the cause, flooding is deadly. Floods kill more people and causes more damage than other severe weather related events. Many die trying to drive or walk through a flooded area. Just six inches of water can knock a person off their feet. Just two feet of water can carry a car away.''')
    st.subheader("2. Hurricanes")
    st.image(image5)
    st.write('''Hurricane — a swirling mass of wind, rain, thunder, and chaos—will intrigue you. Hurricanes begin over tropical and subtropical ocean water. They start when warm water, moist air, and strong winds collide and create a rotating bundle of thunderstorms and clouds. A hurricane might last a few hours or several days.
    Some hurricanes roar onto land bringing punishing wind, torrential rain, walls of water, even tornados. The wind, rain, and water surge wreak havoc on the coastline and damage hundreds of miles inland.

Violent winds flip cars, sink boats, and rip houses apart. Hurricane winds range from 74 miles an hour to 150 ​miles an hour​ or more. Wind creates high waves and pushes the water onto shore. The water surge can be 30 feet high. That's as high as a 3-story building. Storm surges cause most of the fatalities and damage.''')
    st.subheader("3. Earthquakes")
    st.image(image6)
    st.write('''The surface of the earth, called the "crust," is not one solid piece. It's more like a 20 piece puzzle. Each puzzle piece is called a "plate." The plates constantly move. Fortunately for us, they don't move fast. Geologists estimate the fastest plate might shift 6 inches a year (15 centimeters). That's about as fast as your hair grows.

Earthquakes happen when a plate scrapes, bumps, or drags along another plate. When does this happen? Constantly. About a half-million quakes rock the Earth every day. That's millions a year. People don't feel most of them because the quake is too small, too far below the surface, or deep in the sea. Some, however, are so powerful they can be felt thousands of miles away.


A powerful earthquake can cause landslides, tsunamis, flooding, and other catastrophic events. Most damage and deaths happen in populated areas. That's because the shaking can cause windows to break, structures to collapse, fire, and other dangers.

Geologists cannot predict earthquakes. They hope they will in the future through continued research and improved technology.

Earthquakes can happen anytime or anywhere. But you can prepare for the unpredictable with a family safety plan, emergency kit, and supplies.''')
    st.subheader("4. Tornado")
    st.image(image7)
    st.write('''Tornadoes demolish houses, flip cars, cross rivers, dig 3 foot (0.9 meter) trenches, and lift lightweight objects 10,000 feet (3048 meters) into the air. A tornado is a lethal combination of wind and power. Tornadoes touch down all over the world, though most often in the United States.

A tornado is often a funnel cloud—a rotating column of air— that stretches from a storm to the ground. To be a tornado it must touch the ground. It can touch down for a few seconds or grind across the earth for miles. Tornadoes usually last less than 10 minutes.

Most tornadoes start from a supercell. A supercell is a rotating thunderstorm (called a mesocyclone). Supercells create the deadliest tornadoes.

The formation of a tornado is so complex, scientists have yet to understand it. The unpredictable and deadly nature of tornadoes also makes them difficult to study. No matter what movies show, scientists have had little success measuring or getting equipment into tornadoes. Not only is it dangerous, a tornado demolishes everything in its path, including measuring equipment. So, speeds and other factors remain a mystery.''')

    st.subheader("5. Volcanic Eruption")
    st.image(image8)
    st.write('''When magma finds a way to escape from beneath the earth's surface, it creates a volcano.

Volcanoes erupt in different ways. Some, like Mount St. Helens, explode. Explosive eruptions are so powerful, they can shoot particles 20 miles up (32 kilometers), hurl 8-ton boulders more than a half mile (0.8 kilometers) away, and cause massive landslides. Explosive eruptions also create an avalanche of hot volcanic debris, ash, and gas that bulldozes everything in its path. Explosive volcanoes cause most of the volcano-related fatalities.



Volcanoes prove that beneath its calm surface, Earth remains a living planet.

Volcanoes, like Mauna Loa in Hawaii, are effusive. Rather than a violent explosion, lava pours or flows out. Fatalities from effusive volcanoes are rare because people can usually outrun the lava. However, some people get too close or become trapped with no escape. The flowing lava burns, melts, and destroys everything it touches including farms, houses, and roads.

A volcanic eruption forever changes the landscape. Though volcanoes destroy, they also create mountains, islands, and, eventually, incredibly fertile land.''')


elif nav == "Precautions":
    st.header("How to stay safe during a natural disaster")
    st.write('''To keep you and your family safe during a natural disaster, these preparedness safety tips can prevent injuries and make the difference in an emergency:\n

1.Stay informed.\n
2.Tune in to local authorities for information about evacuations and safety tips.\n
3.Have a plan for evacuation. Know where you will go during a natural disaster and how you will get there.\n
4.Keep emergency kits on hand. Stock kits with flashlights, batteries, first aid supplies, and important identification information.\n
5.Avoid unnecessary risks. Do not leave your home unless instructed to do so.\n
6.Go to the safest area in your home.\n
7.During a flood, go to a higher floor. If a tornado is in the area, go to a basement or inner room on the bottom floor of your home.\n''')

    st.subheader('How to stay safe during a flood')
    st.write('''Floods are among the earth’s most common and dangerous natural hazards, formed due to a flow of water on areas of land that are usually dry. Excessive rain, damage to nearby dams, and tsunamis are some of its causes. When faced with flooding, these tips are to be followed:

Do not attempt to walk, swim, or drive through the floods. Floodwater contains debris and contamination and can also be deadly due to fallen electrical lines in the water.
Stay clear of bridges over fast-moving water.
Keep an eye out for evacuation alerts.
Move to higher ground.
If your vehicle is trapped in flood and water starts filling inside the car, seek refuge on the roof.''')
    st.subheader('How to stay safe during a earthquake')
    st.write('''The shifting of tectonic plates causes earthquakes under the earth’s crust, and it is responsible for mass destruction. When faced with an earthquake, these tips can be of use:

If you are indoors,

Take cover under a sturdy table or other pieces of furniture, and hold on until the shaking stops.
Stay away from glass, windows, outside doors and walls, and anything that could fall, such as lighting fixtures or furniture.
Stay inside until the shaking stops, and it is safe to go outside. Most injuries occur to people trying to move a different location inside the building or try to leave.
Do not use the elevators.
If you are outdoors,

Stay away from buildings, streetlights, and utility wires.
Stand in open ground until the shaking stops. It’s dangerous to stay directly outside buildings, at exits, and alongside exterior walls. Ground movement during an earthquake is seldom the direct cause of death or injury. Most earthquake-related casualties result from collapsing walls, flying glass, and falling objects.''')
    st.subheader('How to stay safe during tornado or high winds')
    st.write('''While tornadoes often occur with little notice, there are some preventative measures you can take to prepare your home. Check out these disaster prevention tips:

Secure large appliances with cabling or metal strapping.
Reinforce your garage door by adding weight or replace if not in good repair.
Secure siding. This can be done with fasteners or other materials. Check out FEMA's recommendations for more information.
Arrange home so that heavy objects are close to floor.
Store hazardous chemicals in secured area away from food and water supplies.
Use covers to protect windows and doors.
Repair any roofing that may be loose or damaged.
Maintain EIFS (Exterior Insulation Finishing System) walls.
Remove or trim trees of other landscaping that could cause damage in high winds.''')
    st.subheader('How to stay safe during a Hurricane')
    st.write('''Monitor the radio or television for weather conditions and updates.
Stay away from all windows and exterior doors and seek shelter in a bathroom or basement. Bathtubs can provide some shelter if you cover yourself with plywood or other materials.
Evacuate to a shelter or a neighbor's home if your home is damaged or if you are instructed to do so by emergency personnel.
If power is lost, turn off all major appliances to reduce the chances of damage in the event of a power surge.
If flooding nears your home, turn off the electricity at the main breaker.

Do not handle electrical equipment and do not use the telephone except in an emergency.
Do not go outside, even if the storm appears to have subsided. The calm or the "eye" of the storm can pass quickly, leaving you outside when intense winds resume.
Do not use candles during the storm - they could cause a fire. Stick with battery operated flashlights.
Do not walk, swim or drive through flood waters. Six to twelve inches of water is all it takes to take you down or flood your car.''')
    
    

    st.header("Disaster Supply checklist")
    c1 = st.checkbox('''A supply of water (one gallon per
person per day). Store water in
sealed, unbreakable containers.
Identify the storage date and replace
every six months.''')
    c2 = st.checkbox('''A supply of non-perishable packaged
or canned food and a non-electric
can opener.
''')
    c3 = st.checkbox('''A change of clothing, rain gear and
sturdy shoes.''')
    c4 = st.checkbox('''Blankets or sleeping bags.''')
    c5 = st.checkbox('''A first aid kit and prescription
medications.''')
    c6 = st.checkbox('''A battery-powered radio, flashlight
and plenty of extra batteries.''')
    c7 = st.checkbox('''Important documents, Credit cards and cash''')
    c8 = st.checkbox('''Special items for infants, elderly or
disabled family members.''')
    b1 = st.button("Checklist complete")
    if b1:
        if c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8:
            st.success("Congratulations! Your supply kit is ready")
        else:
            st.error("Checklist is not complete")
    st.subheader("Download the Emergency Preparedness document from here : ")
    with open("EmergencyPreparednessChecklist.pdf", "rb") as file:
        st.download_button(
        label="Download",
        data=file,
        file_name="dowloaded.pdf",
        mime="application/octet-stream"
    )
        st.write("American Red Cross/Customer service number :  00 1 202-303-4498")
