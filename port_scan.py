from scapy.all import IP, TCP ,ICMP , Ether , srp1
import time




print("    MINI NMAP - CONFIGURACIÓN DEL RANGO")


ip_objetivo = input("[>] Ingrese la IP objetivi (ej: 192.168.1.1): ")


#Captura del rango numerio
puerto_inicio = int(input("[>] Ingrese el puerto de INICIO (ej: 20): "))
puerto_fin = int(input("[>] Ingrese el puerto de FIN (ej: 85): "))

#Captura de latencia por puertp
tiempo_espera=float(input("[>] Ingrese el tiempo de espera por puerto en seg (ej: 0.5): "))
print("===========================================================\n")

#Estrucura del rango numérico de puertos a escanear
puertos_a_escanear = range(puerto_inicio,puerto_fin+1)

print(f"[+] Iniciando escaneo de seguridad sobre {ip_objetivo}... ")
print("[+] Analizando puertos del 20 al 85...Por favor espere")

tiempo_inicio = time.time()

for puerto in puertos_a_escanear:
    
    #fabricamos el paquete metiendo la variable 'puerto'  en dport
    paquete = Ether() / IP(dst=ip_objetivo) / TCP(dport=puerto, flags="S") 
            #con eEther evitamos bloqueo de windows / ip destino / puerto destino , flags="S" significa sincronizacion . saludo inicial q se usa para simular q nos queremos conectar de manera amigable
    
    #enviamos en capa 2 un timeput corto para que sea rápido
    respuesta = srp1(paquete, timeout=tiempo_espera, verbose=False)
                    #timeout = 0.5 nos dice espera la respuesta del router solo por medio segunbdo , sino contesta pasa de largo / apaga los tectos internos de scapy y deja la terminal limpia
    
    #evaluamos la respuesta en la red
    if respuesta is None:
        #si es none no hacemos nada el bucle sigue con el proximo puerto
        pass
    else:
        #si el sistema responde con SYC-ACK (SA) el puerto está abierto
        if respuesta.haslayer(TCP) and respuesta[TCP].flags == "SA":  #.hasflayer(TCP) verifica que el paquete devuelto sea protovlo TCP 
#respuesta[TCP].flags== "SA" , singifica SYN-ACK(sincronizacion y aceptación)si el router contesto un 'SA' , esta diceindo ¡Hola recini tu saludo y mi puerto esta listo para recibir conexiones!
            print(f"[+] PUERTO ABIERTO detectado : {puerto} | Servicio probable: {respuesta[TCP].sport}")
tiempo_total = time.time() - tiempo_inicio
print(f"\nEscaneo finalizado con exito en {tiempo_total:.2f} segundos")
