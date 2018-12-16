# List of commands to start the server




## Génération du certicat
sudo bash -c "openssl genrsa -out /etc/ssl/private/selfsign.key 2048 && openssl req -new -x509 -key /etc/ssl/private/selfsign.key -out /etc/ssl/private/selfsign.crt -sha256"

## Démarrage du server

sudo uv4l -f   --auto-video_nr  --reset --driver uvc  --device-id 04f2:b477 --usb-debug 3 --enable-server --server-option '--use-ssl=yes' --server-option '--ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--enable-webrtc-datachannels=yes' --server-option '--webrtc-receive-datachannels=yes'  --server-option '--enable-www-server=yes' --server-option '--www-root-path=/tmp/www' --server-option '--www-index-file=index.html' --server-option '--www-webrtc-signaling-path=/webrtc' --server-option '--www-use-ssl=yes'  --server-option '--www-ssl-private-key-file=/etc/ssl/private/selfsign.key' --server-option '--www-ssl-certificate-file=/etc/ssl/private/selfsign.crt' --server-option '--www-port=8888' --server-option '--janus-gateway-url=https://janus.diverse-team.fr' --server-option '--janus-gateway-root=/janus' --server-option '--janus-room=2' --server-option '--janus-username=rpi0' --server-option '--janus-publish=yes' --server-option '--janus-subscribe=yes' --server-option '--janus-reconnect=yes' --server-option '--webrtc-datachannel-label=JanusDataChannel' 


## Récupération des id de camera si webcamusb

lsusb -v | grep -E '\<(Bus|iProduct|bDeviceClass|bDeviceProtocol)' 2>/dev/null





curl  --insecure -X PUT https://localhost:8080/api/janus/client/settings -d @config.json --header "Content-Type: application/json"

