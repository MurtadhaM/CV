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



##### <p align="center"> <img src="https://img.shields.io/badge/Computer--Vision-YOLOv6 Research-ff0000?style=for-the-badge" width="100%"/> </p>

## Table of Contents
- [Description](#description)
- [Counting Students](#counting-students)
- [Stitching Images Together](#stitching-images-together)
- [Demo](#demo)
- [Sequence Diagram](#sequence-diagram)
- [Technologies](#technologies)
- [Authors](#authors)
- [Credits](#credits)


## Description
This is a research project for the course Computer Vision at the University of North Carolina in Charlotte. The goal of this project is to implement student counting using an image. The model that was used is YOLOv6 and the dataset used is the [COCO dataset](https://cocodataset.org/#home). The model was trained on Google Colab and the results were tested on a local machine. The model was trained on 100 epochs and the results were tested on 100 images. The results were not as expected and the model was not able to detect students in the images. The model was able to detect people in the images but not students. The model was able to detect students.

---

##### <a href="https://drive.google.com/file/d/1JD6vNxip-ClIy_E0Xozcf_Hlz6KXsxek/view"><p align="center"> <img src="https://img.shields.io/badge/Report-Paper-yellow?style=for-the-badge" width="200px"/> </p></a>
---

##### <a href="https://docs.google.com/presentation/d/1KBtMGO36j1XabQgP3KVJK-smWe0HXILbsCPrjrXQbWE/edit#slide=id.g2968f33f89f_0_0"><p align="center"> <img src="https://img.shields.io/badge/Presentation-PDF-blue?style=for-the-badge" width="200px"/> </p></a>
---

#### Counting Students
---

<p align=center><img src="../Counting.gif" width="100%"/></p>

####  Stitching Images Together 

<p align=center><img src="../Stitch.gif" width="100%"/></p>


---

## Demo
##### <p align="center"><a href=https://ml.anywhererpa.com> <img src="https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge" width="200px"/> </a></p>

<p align=center style="font-size:25px"><a href="https://ml.anywhererpa.com">Demo</a></p>



##### <p align="center"><a href=https://cv.anywhererpa.com> <img src="https://img.shields.io/badge/Live-Demo--Backup-purple?style=for-the-badge" width="200px"/> </a></p>

<p align=center style="font-size:25px"><a href="https://cv.anywhererpa.com">Demo Backup Server</a></p>



---
## Sequence Diagram
##### <p align="center"> <img src="https://img.shields.io/badge/Sequence-Diagram-purple?style=for-the-badge" width="200px"/> </p>

<p align=center><img src="../assets/sequence.png" width="100%"/></p>

## Technologies
- [Ubuntu Server 20.04 LTS](https://ubuntu.com/download/server)
- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [YOLOv6](https://github.com/meituan/YOLOv6)
- [COCO dataset](https://cocodataset.org/#home)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [OpenCV](https://opencv.org/)
- [Stitching](https://github.com/OpenStitching/stitching)



---
## Authors
##### <p align="center"> <img src="https://img.shields.io/badge/Authors-Contributors-ff0000?style=for-the-badge" width="200px"/> </p>


<table center>
  <thead allign=center>
    <tr>
      <th align=center > <img src="https://img.shields.io/badge/-Murtadh-red" href="findasnake.com" width="100%"/></th>
      <th align=center><img src="https://img.shields.io/badge/Param-orange" width="75%"/></th>
      <th align=center><img src="https://img.shields.io/badge/-Nick-yellow" width="75%"/>  </th>
      <th align=center><img src="https://img.shields.io/badge/-Haochen-green" width="75%"/> </th>
      <th align=center><img src="https://img.shields.io/badge/-Sam-Blue" width="75%"/>  </th>
    </tr>
  </thead>
  <tbody >
    <tr>
      <td>
        <a href="">
          <img src="https://avatars.githubusercontent.com/u/45076915?s=200&v=4"  alt="Murtadha Marzouq" width="384" />
        </a>
      </td>
      <td>
        <a href="">
          <img src="../Proposal/images/Param.png" alt="Param" width="384"/>
        </a>
      </td>
      <td>
        <a href="">
          <img src="../Proposal/images/Yuepei.png" alt="Param" width="384"/>
        </a>
      </td>
      <td>
        <a href="">
          <img src="../Proposal/images/Haochen.png" alt="Sam" width="384"/>
        </a>
      </td>
   <td>
        <a href="">
          <img src="../Proposal/images/Sam.png" alt="Sam" width="384"/>
        </a>
      </td>
  


  </tbody>
</table>

## Credits
- [Research Paper](https://arxiv.org/abs/2301.05586)
- [Research Paper](https://arxiv.org/abs/2209.02976)
- [YOLOv6](https://github.com/meituan/YOLOv6)
- [COCO dataset](https://cocodataset.org/#home)
- [Stitiching Library](https://github.com/OpenStitching/stitching)
- [Stitching Paper For the Bonus](http://hdl.handle.net/20.500.11970/112696)

      @misc{li2022yolov6,
            title={YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications}, 
            author={Chuyi Li and Lulu Li and Hongliang Jiang and Kaiheng Weng and Yifei Geng and Liang Li and Zaidan Ke and Qingyuan Li and Meng Cheng and Weiqiang Nie and Yiduo Li and Bo Zhang and Yufei Liang and Linyuan Zhou and Xiaoming Xu and Xiangxiang Chu and Xiaoming Wei and Xiaolin Wei},
            year={2022},
            eprint={2209.02976},
            archivePrefix={arXiv},
            primaryClass={cs.CV}
      }

      @misc{li2023yolov6,
            title={YOLOv6 v3.0: A Full-Scale Reloading}, 
            author={Chuyi Li and Lulu Li and Yifei Geng and Hongliang Jiang and Meng Cheng and Bo Zhang and Zaidan Ke and Xiaoming Xu and Xiangxiang Chu},
            year={2023},
            eprint={2301.05586},
            archivePrefix={arXiv},
            primaryClass={cs.CV}
      }



