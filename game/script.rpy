define week = ['Monday','Teusday','Wednesday','Thursday','Friday','Saturday','Sunday']

python:

    day = week[0]

define d = Character("Danae")







#navigation menu




label start:

    "⍴⍲☊ℍℇ⎾⎾ℇ☊⟟⍧ ⍲⍧⍲⟄ℇ⍓⍦ 🜅⌾☈ ⍑ℍℇ ⍲☈⍑⎎ ⍲☊⟄ ⎎⍧⟟ℇ☊⍧ℇ⎎"

    "Where are you going today?"

menu:

    "Ground floor":
        jump ground_floor

    "First floor":
        jump first_floor








#ground floor




label ground_floor:

    "You stay in the ground floor, examining your options."

menu:

    "Dormintories":
        jump dormintories 

    "Campus":
        jump campus 

    "Basement":
        jump basement

    "Event Hall":
        jump event_hall

    "Select floor.":
        jump start



label dormintories:

    "You are at the dormintories."

    "Where do you want to go?"

menu:

    "Ionian dorm":
        jump ionian_dorm

    "Dorian dorm":
        jump dorian_dorm
    
    "Back to the ground floor.":
        jump ground_floor


label ionian_dorm:

    "You are at the Ionian dorm."

    "Where do you want to go?"

menu:

    "Secretariat":
        jump i_secretariat

    "Room 68":
        jump room_68

    "Room 15":
        jump room_15

    "Room 24":
        jump room_24

    "Back to the dormintories.":
        jump dormintories

label i_secretariat:

    "You are at the secretariat."
    jump menu_done

    
label room_68:

    "You are at room 68."
    jump menu_done

label room_15:

    "You are at room 15."
    jump menu_done

label room_24:

    "You are at room 24."
    jump menu_done

label dorian_dorm:

    "You are at the Dorian dorm."

    "Where do you want to go?"

menu:

    "Secretariat.":
        jump d_secretariat

    "Room 49.":
        jump room_49

    "Room 31.":
        jump room_31

    "Room 90.":
        jump room_90

    "Back to the dormintories.":
        jump dormintories

label d_secretariat:

    "You are at the secretariat."
    jump menu_done

label room_49:

    "You are at room 49."
    jump menu_done

label room_31:

    "You are at room 31."
    jump menu_done

label room_90:

    "You are at room 90."
    jump menu_done



label campus:

    "You are at the campus."

    "Where do you want to go?"


menu:

    "Garden.":
        jump garden

    "Gymnasium." if day!=week[6]:
        jump gymnasium

    "Back to the ground floor.":
        jump ground_floor

label garden:

    "You are at the garden."
    jump menu_done

label gymnasium: 

    "You are at the gymnasium."

    "Where do you want to go?"

menu:

    "Track field.":
        jump track_field
    
    "Archery range.":
        jump archery_range

    "Swimming pool.":
        jump swimming_pool

    "Wrestling ring.":
        jump wrestling_ring

    "Go back to the campus.":
        jump campus


label track_field:

    "You are at the track field."
    jump menu_done

label archery_range:

    "You are at the archery range."
    jump menu_done

label swimming_pool:

    "You are at the swimming pool."
    jump menu_done

label wrestling_ring:

    "You are at the wrestling ring."
    jump menu_done

label library:

    "You are at the library."
    jump menu_done

label cafeteria:

    "You are at the cafeteria."
    jump menu_done

label event_hall:

    "You are at the event hall."
    jump menu_done




#first floor





label first_floor:

menu:

    "Classrooms":
        jump classrooms 

    "Cafeteria":
        jump cafeteria

    "Senate":
        jump senate 
    
    "Treatment Room":
        jump treatment_room

    "Select floor.":
        jump start

label classrooms:

    "You are at the classrooms."

    "Where do you want to go?"

menu:

    "Art class.":
        jump art_class

    "Music class.":
        jump music_class

    "Go back to the first floor.":
        jump first_floor

label art_class:

    "You are at the art class."
    jump menu_done

label music_class:

    "You are at the music class."
    jump menu_done

label senate: 

    "You are at the senate."
    jump menu_done

label basement:

    "You are at the basement."
    jump menu_done

label treatment_room:

    "You are at the treatment room."
    jump menu_done




#navigation menu end




label menu_done:

    "Hi."

    return
