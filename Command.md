# List of commands to start the server




## Génération du certicat
sudo bash -c "openssl genrsa -out /etc/ssl/private/selfsign.key 2048 && openssl req -new -x509 -key /etc/ssl/private/selfsign.key -out /etc/ssl/private/selfsign.crt -sha256"

## Démarrage du server

Last command that works
sudo uv4l -f   --auto-video_nr  --reset --driver uvc  --device-id 045e:076f --usb-debug 3 --enable-server --server-option '--use-ssl=yes' --server-option '--ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--enable-webrtc-datachannels=yes' --server-option '--webrtc-receive-datachannels=yes'  --server-option '--enable-www-server=yes' --server-option '--www-root-path=/home/pi/iot-webrtc/web/' --server-option '--www-index-file=index.html' --server-option '--www-webrtc-signaling-path=/webrtc' --server-option '--www-use-ssl=yes'  --server-option '--www-ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--www-ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--www-port=8888' --server-option '--janus-gateway-url=https://janus.diverse-team.fr' --server-option '--janus-gateway-root=/janus' --server-option '--janus-room=2' --server-option '--janus-username=rpi0' --server-option '--janus-publish=yes' --server-option '--janus-subscribe=yes' --server-option '--janus-reconnect=yes' --server-option '--webrtc-datachannel-label=JanusDataChannel' --server-option '--webrtc-received-datachannel-socket=/tmp/uv4l.socket' --server-option '--webrtc-datachannel-socket=/tmp/uv4l.socket' --server-option '--webrtc-stun-url=stun:stun.l.google.com:19302' --server-option '--webrtc-stun-server=yes'

microsoft 045e:076f
monpc 04f2:b477

    sudo uv4l -f   --auto-video_nr  --reset --driver uvc  --device-id 045e:076f --usb-debug 3 --enable-server --server-option '--use-ssl=yes' --server-option '--ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--enable-webrtc-datachannels=yes' --server-option '--webrtc-receive-datachannels=yes'  --server-option '--enable-www-server=yes' --server-option '--www-root-path=/home/pi/iot-webrtc/web/' --server-option '--www-index-file=index.html' --server-option '--www-webrtc-signaling-path=/webrtc' --server-option '--www-use-ssl=yes'  --server-option '--www-ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--www-ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--www-port=8888' --server-option '--janus-gateway-url=https://janus.diverse-team.fr' --server-option '--janus-gateway-root=/janus' --server-option '--janus-room=2' --server-option '--janus-username=rpi0' --server-option '--janus-publish=yes' --server-option '--janus-subscribe=yes' --server-option '--janus-reconnect=yes' --server-option '--webrtc-datachannel-label=JanusDataChannel' --server-option '--webrtc-received-datachannel-socket=/tmp/uv4l.socket' --server-option '--webrtc-datachannel-socket=/tmp/uv4l.socket'

sudo uv4l -f -v   --auto-video_nr   --driver mjpegstream --uri http://olivier:olivier@192.168.2.235/videostream.cgi --enable-server --server-option '--use-ssl=yes' --server-option '--ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--enable-webrtc-datachannels=yes' --server-option '--webrtc-receive-datachannels=yes'  --server-option '--enable-www-server=yes' --server-option '--www-root-path=/tmp/www' --server-option '--www-index-file=index.html' --server-option '--www-webrtc-signaling-path=/webrtc' --server-option '--www-use-ssl=yes'  --server-option '--www-ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--www-ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--www-port=8888' --server-option '--janus-gateway-url=https://janus.diverse-team.fr' --server-option '--janus-gateway-root=/janus' --server-option '--janus-room=2' --server-option '--janus-username=rpi0' --server-option '--janus-publish=yes' --server-option '--janus-subscribe=yes' --server-option '--janus-reconnect=yes' --server-option '--webrtc-datachannel-label=JanusDataChannel' --server-option '--webrtc-received-datachannel-socket=/tmp/uv4l.socket' --server-option '--webrtc-datachannel-socket=/tmp/uv4l.socket'


Stop
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=1

Droite 
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=6

Gauche
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=4

Haut
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=0

Bas
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=2

Bas droite
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=93

Haut droite
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=91

Bas gauche
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=92

Haut droite
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=90

centre
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=25


Patrouille vertical
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=26

Arret Patrouille vertical
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=27


Patrouille horizontal
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=28

Arret Patrouille horizontal
http://olivier:olivier@192.168.2.220/decoder_control.cgi?command=29


## Récupération des id de camera si webcamusb

lsusb -v | grep -E '\<(Bus|iProduct|bDeviceClass|bDeviceProtocol)' 2>/dev/null





curl  --insecure -X PUT https://localhost:8080/api/janus/client/settings -d @config.json --header "Content-Type: application/json"



# routing from linux PC
change enp0s25 with your ethernet interface name and wl01 with your wireless interface name.

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -A FORWARD --in-interface enp0s25 -j ACCEPT
sudo iptables --table nat -A POSTROUTING --out-interface wlo1 -j MASQUERADE


# Connexion au routeur
Depuis celui qui sert de routeur
http://192.168.1.3:8080


En Wifi
http://192.168.3.1
