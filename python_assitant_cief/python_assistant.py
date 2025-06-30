import speech_recognition as sr
import io
import pyttsx3
import pyjokes
import datetime
import webbrowser
import pywhatkit

nombre_asistente = "Aura"  # Nombre del asistente

# Función para que escuche la máquina y muestre el texto reconocido
def audio_pc():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        # delay para la carga de la librería
        recognizer.pause_threshold = 0.7  # Ajusta el umbral de pausa 0.5 ~ 0.8
        # Mensaje para saber  que podemos empezar a hablar
        print("Ajustando el ruido del micrófono...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Has dicho ...", text) # print("Has dicho: {text}")
        return text
    except: # sr.UnknownValueError:
        print("Lo siento, no pude entender lo que dijiste.")
    # except sr.RequestError as e:
    #     print(f"Error al conectar con el servicio de reconocimiento de voz: {e}")

# audio_pc()

# Función para que hable la máquina
def respuesta_pc(texto):
    
    try:
        engine = pyttsx3.init()
        # Configuración de la voz
        engine.setProperty('rate', 135)  # Velocidad de la voz
        engine.setProperty('volume', 0.9)  # Volumen de la voz (0.0 a 1.0)
        
        # preparación del motor de voz
        engine.say(texto)
        # que se quede en espera hasta que termine de hablar
        engine.runAndWait()
    except:
        print("Error al intentar hablar: ")

# respuesta_pc("Puedo hablar en este momento.")

def decir_dia_semana():
    # Obtiene el día
    dia = datetime.date.today()
    
    # 0 = Lunes, 1 = Martes, 2 = Miércoles, 3 = Jueves, 4 = Viernes, 5 = Sábado, 6 = Domingo
    nombres_dias = {
        0 : "Lunes",
        1 : "Martes",
        2 : "Miércoles",
        3 : "Jueves",
        4 : "Viernes",
        5 : "Sábado",
        6 : "Domingo"
    }
    respuesta_pc(f"Hoy es {nombres_dias[dia.weekday()]}.")
    

def decir_hora():
    # Obtiene la hora
    hora = datetime.datetime.now()
    
    # Formatea la hora
    hora_actual = hora.strftime("%H")
    minuto = hora.strftime("%M")
    
    respuesta_pc(f"Son las {hora_actual} y {minuto} minutos.")

# decir_hora()
def saludo_inicial():
    hora = datetime.datetime.now()
    hora_actual = hora.hour
    
    if 6 <= hora_actual < 14:
        respuesta_pc("Buenos días")
    elif 14 <= hora_actual < 20:
        respuesta_pc("Buenas tardes")
    else:
        respuesta_pc("Buenas noches")

    respuesta_pc(f"Mi nombre es {nombre_asistente}, ¿en qué puedo ayudarte?.")

# saludo_inicial()

def centro_de_peticiones():
    
    saludo_inicial()
    
    # Bucle para escuchar continuamente hasta que lo detengamos
    while True:

        peticion = audio_pc().lower()
        print(peticion)

        if f"{nombre_asistente} qué día es hoy" in peticion:
            decir_dia_semana()
            continue
        elif f"{nombre_asistente} qué hora es" in peticion:
            decir_hora()
            continue
        elif f"{nombre_asistente} cuéntame un chiste" in peticion:
            chiste = pyjokes.get_joke(language='es', category='all')
            respuesta_pc(chiste)
            continue
        elif f"{nombre_asistente} reproduce" in peticion:
            cancion = peticion.replace(f"{nombre_asistente} reproduce", "").strip()
            respuesta_pc(f"Reproduciendo {cancion}.")
            pywhatkit.playonyt(cancion)
            continue
        elif f"{nombre_asistente} abre" in peticion:
            sitio_web = peticion.replace(f"{nombre_asistente} abre", "").strip()
            respuesta_pc(f"Abriendo {sitio_web}.")
            webbrowser.open(sitio_web)
            continue
        elif "salir" in peticion or "adiós" in peticion or "eso es todo" in peticion:
            respuesta_pc("Hasta luego, que tengas un buen día.")
            break

centro_de_peticiones()