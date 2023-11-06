## Quality of Life

```sql
apt update

apt install zsh zsh-syntax-highlighting zsh-autosuggestions zsh-theme-powerlevel10k

apt install python3-pip python3-dev python3-venv npm nodejs git curl wget
chsh -s $(which zsh)

 sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

 zsh -c "$(curl -fsSL https://raw.githubusercontent.com/MurtadhaM/.dotfiles/main/oh-my-zsh-plugins.sh)"

omz theme set agnoster
omz theme use agnoster
```

## Certificates

```bash
echo "-----BEGIN CERTIFICATE-----
MIIEqjCCA5KgAwIBAgIURlAzb8cRZ5ieAYBQEynGO2QEpHswDQYJKoZIhvcNAQEL
BQAwgYsxCzAJBgNVBAYTAlVTMRkwFwYDVQQKExBDbG91ZEZsYXJlLCBJbmMuMTQw
MgYDVQQLEytDbG91ZEZsYXJlIE9yaWdpbiBTU0wgQ2VydGlmaWNhdGUgQXV0aG9y
aXR5MRYwFAYDVQQHEw1TYW4gRnJhbmNpc2NvMRMwEQYDVQQIEwpDYWxpZm9ybmlh
MB4XDTIzMTEwNDE5NDQwMFoXDTM4MTAzMTE5NDQwMFowYjEZMBcGA1UEChMQQ2xv
dWRGbGFyZSwgSW5jLjEdMBsGA1UECxMUQ2xvdWRGbGFyZSBPcmlnaW4gQ0ExJjAk
BgNVBAMTHUNsb3VkRmxhcmUgT3JpZ2luIENlcnRpZmljYXRlMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7YnNsVwD1hDQJhrOK01AcM7HU8YUSKo0V0Ld
SOEr1LsgHp1K4p6geRWAZsQD31rESDN4dlrF1NocdkmvC4Rf5QgMHfhgv+faLPUC
uRYENqRBj4pIhXXF+jxaSI35PKTIKroDH3EzAFpSWuW8wzSSZK95r5Z9/JE2DJi7
6+MD1dFlTue1mO9ciVjNo1NrYjlOFtToXZUTi+mGuOS0RLR5xc4G2KNt29HeKHW2
94oQ4GqccgD9Q8wFwTpF0IrJ50vNrXNeBdTDMpd+5HemWd3nU5kYR6RWwF1Hb7gQ
598Z8bIgfuhuTq/l69M2ykb51wTJ+TE6p/444FhBS9BZ82mGxQIDAQABo4IBLDCC
ASgwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcD
ATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBQYJGHIQTpgwpPN0TMkWHK6k64aKzAf
BgNVHSMEGDAWgBQk6FNXXXw0QIep65TbuuEWePwppDBABggrBgEFBQcBAQQ0MDIw
MAYIKwYBBQUHMAGGJGh0dHA6Ly9vY3NwLmNsb3VkZmxhcmUuY29tL29yaWdpbl9j
YTAtBgNVHREEJjAkghEqLmFueXdoZXJlcnBhLmNvbYIPYW55d2hlcmVycGEuY29t
MDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly9jcmwuY2xvdWRmbGFyZS5jb20vb3Jp
Z2luX2NhLmNybDANBgkqhkiG9w0BAQsFAAOCAQEAn4Hs/ofrYihSYerpOXh751o6
NED/it75ZtlmVy5Yw78haYiDqdHXoGZ4uNWVV9DqZHJOLAByjIPhvUn37uqpuAw2
WBiD1bfyTLGXYz/OL1SEJkN/EkE7ApoEsgstlqtg8nIlA/rbRo1dSpLPSxZJlTnZ
sW6PCJvOhPly1AB8H0t5ltL9fqM7tR7R1Se/msNSNF5BoFZYErgTtCsS+FykYeHE
a6sE9E751kdHIaLkTLlmCWrlJCa5xUPIKC99brDnxKKlLPUGsQ0d1MAJAfak1LLJ
1LXAhcRh76sLndfeFv01YF1T4WKI4WVhlvZlHOJvXzJCTRxjomNG+YhXtX1k2A==
-----END CERTIFICATE-----" > /opt/server.crt

echo "-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDtic2xXAPWENAm
Gs4rTUBwzsdTxhRIqjRXQt1I4SvUuyAenUrinqB5FYBmxAPfWsRIM3h2WsXU2hx2
Sa8LhF/lCAwd+GC/59os9QK5FgQ2pEGPikiFdcX6PFpIjfk8pMgqugMfcTMAWlJa
5bzDNJJkr3mvln38kTYMmLvr4wPV0WVO57WY71yJWM2jU2tiOU4W1OhdlROL6Ya4
5LREtHnFzgbYo23b0d4odbb3ihDgapxyAP1DzAXBOkXQisnnS82tc14F1MMyl37k
d6ZZ3edTmRhHpFbAXUdvuBDn3xnxsiB+6G5Or+Xr0zbKRvnXBMn5MTqn/jjgWEFL
0FnzaYbFAgMBAAECggEAB3qoytZSWpmh7Ck4550hk8u28/jPJ7CQQFUfIY3RcvvH
WZ9rPbJv7BAUwGeYlZ5Ggt14BAX8p6SMc98DD3JGELCNrR3mcfRrZrH6OXirfkry
s4HPocAhES14TEOIHvQzR0EfGwzV5cNyR2FnbaAIofnyc2hiJCMwV/oxJI67zq4f
Io71eUxP4X3rOZsairkBggDAmgGdanUtsb1sp2Tz9IYUGY31ZMIiUaxkz1CNMMoz
dx2XMB6OQ6zcFqAjoA4SzO0d1ddfHLjkF+r7qXePXQCtS8U0bjfNAaAaS71GqDd0
7NSuoy9+16Oq2LbD/Ng0pvq6/buQHPk+H7jgcqyhSwKBgQD3SDWf8mMwqWdrZIF1
9LkOOVRZ+s0fqmYtira5Oiodye1ythzQszhCZzvkeOCtefbkQIwd3/ZCTriQj8ke
4mt+uyFGnJxeYuQvrDU9zLMbGKx0dAHhkl3hAd2yLeKmQHG7Unro1wPJ1br6bDMl
A5gnBvK5A8KWDxz4OyHMhrQ00wKBgQD16adZawZZbfSk/LeD7vPoZq5yIT/9y/oO
UdUaox9QM3PS5KyVQPl/fiT7aLhWRPgPnfDlYYJ4jDvkFnxJa8KdGuYgOX4+9gjv
OF+9KtI9PfV5J/77fEBhWg0+rSMMOfPk29Y7mwNiGiAdjZQ1pFG3NRDLJvyR8MLP
XZmAw5p3BwKBgCLMx7ctvmXPwV0stMdr3EszKDrNf+aP7XdFSTfCBsFQdJkrJdz9
C9LUgmpB1KS1QFiY+N8PcLGeMH0vrwcoqCYaobE1QxBJbIGFA60hzKbojwSIeudK
2OlcgN2ddYMeGKNbFS8Fa2QRLxIk/gGcguIjKS9+ZvkFQXdxou0Mm/m/AoGAbci0
R306Rm6KS6XvH91r0pMUyisB8IJBzmbGJrAwaJOv37TrP27UdBCS3hJwSUNdI0u1
ohIYN00T584KCpUrOwwpNLW2INGiR3n5c/BMD787ea1bblaYP13+j76n6OtucPub
9txLdF6Je+gbBJ+pQ4tTRf7Pvy+nKQB2aT/qE70CgYEA7w0hIVG3/lwSaHHWa6AA
opvbJQZC0NLWj/kciaHfxBs2HPLyJXLoXe5JiUa3gAUDRsRRcs+JOYegYS/B22SB
+soEdLRWs2BqBCyFmZqHak6qeENs9bWR+Zf6xX7s07mcyyWSXVub2D2g0M5X5nLd
yTDVR6sRYVZK+9mbNLqfuH0=
-----END PRIVATE KEY-----" > /opt/server.key

```

## Configuring the server

```python
# Install requirements
apt install pip python3-pip python3-dev python3-venv npm nodejs
pip3 install opencv-python flask flask-cors
pip install -r YOLOv6/requirements.txt
cat <<EOF > /opt/requirments.txt
# pip install -r requirements.txt
# python3.8 environment
psutil
torch>=1.8.0
torchvision>=0.9.0
numpy>=1.24.0
opencv-python>=4.1.2
PyYAML>=5.3.1
scipy>=1.4.1
tqdm>=4.41.0
addict>=2.4.0
tensorboard>=2.7.0
pycocotools>=2.0
onnx>=1.10.0  # ONNX export
onnx-simplifier>=0.3.6 # ONNX simplifier
thop  # FLOPs computation
pytorch_quantization>=2.1.1
EOF
pip3 install -r /opt/requirments.txt


FLASK="FLASK_ENV=production FLASK_APP=app.py  flask run  --cert=/opt/server.crt --key=/opt/server.key --host=0.0.0.0 --port 443  --with-threads"
FLASK2="FLASK_ENV=production FLASK_APP=app.py  flask run   --host=0.0.0.0 --port 80  --with-threads"
# Install pm2
npm install pm2@latest -g
# Run the server
pm2 start $FLASK --name "flask:443"
pm2 start $FLASK2 --name "flask:80"
pm2 save
pm2 startup



```
